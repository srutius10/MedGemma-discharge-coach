import gradio as gr

from src.utils import ui_generate
from src.constants import EXAMPLES

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

:root {
  --bg: #f5ede0;
  --card: #fdf6ee;
  --border: #d9c9b4;
  --text: #3b2f20;
  --muted: #7a6652;
  --accent: #8b6343;
}

.gradio-container {
  font-family: 'Lora', 'Times New Roman', serif !important;
  background: var(--bg) !important;
  color: var(--text) !important;
}

/* Title */
h1 {
  color: var(--text) !important;
  font-weight: 600 !important;
  font-size: 1.6rem !important;
  border-bottom: 2px solid var(--border) !important;
  padding-bottom: 8px !important;
}

h2, h3, label, .label-wrap span {
  color: var(--muted) !important;
  font-family: 'Lora', serif !important;
  font-weight: 600 !important;
}

/* Text boxes */
textarea, input[type="text"] {
  background: var(--card) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: 12px !important;
  color: var(--text) !important;
  font-family: 'Lora', 'Times New Roman', serif !important;
  font-size: 15px !important;
  line-height: 1.7 !important;
  padding: 12px !important;
}

textarea:focus, input:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px rgba(139, 99, 67, 0.12) !important;
  outline: none !important;
}

/* Generate button */
button.primary, button[variant="primary"] {
  background: var(--accent) !important;
  color: #fdf6ee !important;
  border: none !important;
  border-radius: 10px !important;
  font-family: 'Lora', serif !important;
  font-weight: 600 !important;
  font-size: 15px !important;
  padding: 10px 28px !important;
  box-shadow: 0 2px 8px rgba(139, 99, 67, 0.2) !important;
}

button.primary:hover {
  background: #6e4d33 !important;
}

/* File upload */
.file-preview, [data-testid="file"] {
  background: var(--card) !important;
  border: 1.5px dashed var(--border) !important;
  border-radius: 12px !important;
  color: var(--muted) !important;
}

/* Panels and cards */
.block, .panel, .gr-box {
  background: var(--card) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: 14px !important;
  box-shadow: 0 2px 10px rgba(59, 47, 32, 0.06) !important;
}

/* Examples */
.examples td {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  font-family: 'Lora', serif !important;
  border-radius: 8px !important;
}

.examples td:hover {
  background: #ede0cf !important;
  cursor: pointer !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 999px; }
::-webkit-scrollbar-track { background: var(--bg); }
"""


def build_app():
    with gr.Blocks(
        title="Clinical Documentation Generator",
        css=CUSTOM_CSS,
    ) as demo:
        gr.Markdown("# 🏥 AI Clinical Documentation Assistant")
        gr.Markdown(
            "Paste a doctor-patient conversation or upload a file to generate a SOAP note."
        )

        with gr.Row():
            with gr.Column(scale=1):
                conversation_input = gr.Textbox(
                    label="Doctor-Patient Conversation",
                    placeholder="Doctor: What symptoms are you having?\nPatient: ...",
                    lines=12,
                )
                file_input = gr.File(
                    label="Upload transcript (.txt or .docx)",
                    file_types=[".txt", ".docx"],
                    type="filepath",
                )
                generate_btn = gr.Button(
                    "Generate Clinical Note",
                    variant="primary",
                )

            with gr.Column(scale=1):
                output_box = gr.Textbox(
                    label="Generated SOAP Note",
                    lines=18,
                )
                safety_box = gr.Textbox(
                    label="Safety Flags",
                    lines=3,
                )
                pdf_file_output = gr.File(
                    label="Download PDF",
                )

        generate_btn.click(
            fn=ui_generate,
            inputs=[conversation_input, file_input],
            outputs=[output_box, safety_box, pdf_file_output],
        )

        gr.Examples(
            examples=[[v, None] for v in EXAMPLES.values()],
            inputs=[conversation_input, file_input],
        )

    return demo


if __name__ == "__main__":
    demo = build_app()
    demo.launch()
