import warnings
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from .constants import SYSTEM_PROMPT

warnings.filterwarnings("ignore")

MODEL_ID = "google/gemma-1.1-7b-it"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True,
    trust_remote_code=True,
)
model.eval()

if torch.cuda.is_available():
    print(f"Model loaded | GPU: {torch.cuda.memory_allocated(0)/1e9:.2f} GB allocated")
else:
    print("Model loaded on CPU")


def run_model(conversation: str) -> str:
    if not conversation or not conversation.strip():
        return "No conversation provided."

    messages = [{
        "role": "user",
        "content": f"{SYSTEM_PROMPT}\n\nConversation:\n{conversation}\n\nGenerate the clinical documentation:"
    }]

    try:
        prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=2048,
        ).to(model.device)

        print(f"Input tokens: {inputs['input_ids'].shape[1]} | Generating...")

        with torch.no_grad():
            outputs = model.generate(
                inputs["input_ids"],
                max_new_tokens=400,
                temperature=0.0,      # deterministic
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )

        new_tokens_only = outputs[0][inputs["input_ids"].shape[1]:]
        response = tokenizer.decode(new_tokens_only, skip_special_tokens=True).strip()
        print("Generation complete")
        return response

    except Exception as e:
        traceback_str = "".join(traceback.format_exc())
        print("Error during generation:\n", traceback_str)
        return f"Generation failed: {str(e)}"
