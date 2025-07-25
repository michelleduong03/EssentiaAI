from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum")

def generate_summary(text, max_length=50, min_length=20):
    if not text.strip():
        return "No input text provided."
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
