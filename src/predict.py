import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class SentimentModel:
    def __init__(self, model_path, tokenizer_path):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=-1).item()
        return "Positive" if prediction == 0 else "Negative"

    def predict_batch(self, texts):
        inputs = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predictions = torch.argmax(logits, dim=-1).tolist()
        return ["Positive" if p == 0 else "Negative" for p in predictions]
