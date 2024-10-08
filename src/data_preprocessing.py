import re

def clean_text(text):
    text = re.sub(r'[^\w\s,]', '', text)
    text = re.sub(r'[:;]+[)]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def preprocess_data(texts):
    return [clean_text(text) for text in texts]
