# MedGemma Clinical Documentation Assistant

This project uses the `google/gemma-1.1-7b-it` model to generate structured SOAP clinical notes from doctor–patient conversations. 
You can paste a transcript or upload a `.txt`/`.docx` file and get a formatted note plus safety flags and a downloadable PDF.
---*

## Project Structure

```text
medgemma-project/
├── src/
│   ├── __init__.py
│   ├── constants.py      # System prompt + example conversations
│   ├── model.py          # Model loading + text generation
│   └── utils.py          # File handling, PDF generation, app logic
├── app/
│   ├── __init__.py
│   └── app.py            # Gradio UI
├── notebooks/
│   └── kaggle_experiment.ipynb   # Original Kaggle notebook (optional)
├── data/
│   └── README.md         # Instructions for data (no PHI in repo)
├── requirements.txt
├── README.md
└── LICENSE
