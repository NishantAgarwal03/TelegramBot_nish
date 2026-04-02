from transformers import pipeline

def summarize_text(text):
    """
    Summarize long text using the facebook/bart-large-cnn model.
    """
    if not text or len(text.split()) < 20:
        return text
        
    try:
        # Initialize the summarization pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        
        # Summarize (adjust max_length and min_length as needed)
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Summarization error: {e}")
        return text
