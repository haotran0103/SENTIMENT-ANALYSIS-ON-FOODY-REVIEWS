import unittest
from src.predict import SentimentModel

class TestSentimentModel(unittest.TestCase):
    def setUp(self):
        self.model = SentimentModel("./model", "./tokenizer")

    def test_single_prediction(self):
        result = self.model.predict("Sản phẩm này rất tốt!")
        self.assertIn(result, ["Positive", "Negative"])

    def test_batch_prediction(self):
        results = self.model.predict_batch(["Sản phẩm này rất tốt!", "Dịch vụ không tốt!"])
        self.assertEqual(len(results), 2)
        self.assertTrue(all(r in ["Positive", "Negative"] for r in results))

if __name__ == "__main__":
    unittest.main()
