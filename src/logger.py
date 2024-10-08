import logging

logging.basicConfig(filename='../logs/api_log.log', level=logging.INFO)

def log_request(texts):
    logging.info(f"Received {len(texts)} texts for prediction")

def log_response(sentiments):
    logging.info(f"Processed texts with sentiments: {sentiments}")

def log_error(error_message):
    logging.error(f"Error: {error_message}")
