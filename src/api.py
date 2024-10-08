from flask import Flask, request, jsonify
from predict import SentimentModel
from logger import log_request, log_response, log_error
from data_preprocessing import preprocess_data

app = Flask(__name__)

model_path = "../model"
tokenizer_path = "../tokenizer"
sentiment_model = SentimentModel(model_path, tokenizer_path)

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    data = request.get_json()
    texts = data.get('texts')

    if not texts or not isinstance(texts, list):
        log_error("Invalid input: No texts provided or invalid format")
        return jsonify({'error': 'No texts provided or invalid format'}), 400

    log_request(texts)
    cleaned_texts = preprocess_data(texts)
    sentiments = sentiment_model.predict_batch(cleaned_texts)
    log_response(sentiments)

    return jsonify({'sentiments': sentiments})

if __name__ == '__main__':
    app.run(debug=True, port=8080)  