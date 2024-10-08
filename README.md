
# AI-powered Sentiment Analysis for E-commerce

### Các tính năng chính:
- **Phân loại cảm xúc (tích cực/tiêu cực)**: Dự đoán cảm xúc của người dùng từ các đánh giá văn bản.
- **Batch Processing**: Hỗ trợ xử lý hàng loạt đánh giá trong một lần yêu cầu.
- **API Flask**: Cung cấp RESTful API để tích hợp vào các hệ thống khác.
- **Ghi log**: Ghi lại thông tin về các yêu cầu và phản hồi để theo dõi hiệu suất.
- **Dashboard**: Tạo báo cáo và trực quan hóa kết quả phân tích cảm xúc.

## Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/your-username/sentiment-analysis-ecommerce.git
cd sentiment-analysis-ecommerce
```

### 2. Tạo và kích hoạt môi trường ảo

```bash
python -m venv venv
source venv/bin/activate   # Đối với Linux/macOS
venv\Scripts\activate      # Đối với Windows
```

### 3. Cài đặt các package cần thiết

```bash
pip install -r requirements.txt
```

### 4. Tải mô hình và tokenizer
do kích thước mô hình folder model vui lòng tải link bên dưới
link: https://drive.google.com/drive/folders/1ut6ZCyON-Oofcmcqt8_zDS2oa7NP2QNf?usp=sharing

## Sử dụng

### 1. Chạy API Flask

Để khởi động API, chạy lệnh sau:

```bash
python src/api.py
```

API sẽ chạy trên địa chỉ: `http://127.0.0.1:5000`.

### 2. Gửi yêu cầu tới API bằng Postman hoặc cURL

#### Gửi yêu cầu POST qua cURL

```bash
curl -X POST http://127.0.0.1:5000/batch_predict \
-H "Content-Type: application/json" \
-d '{"texts": ["Sản phẩm rất tốt", "Dịch vụ quá tệ"]}'
```

#### Gửi yêu cầu POST qua Postman

- **URL**: `http://127.0.0.1:5000/batch_predict`
- **Method**: POST
- **Body**: Chọn `raw` và định dạng `JSON`, nội dung:
  ```json
  {
    "texts": [
      "Sản phẩm rất tốt",
      "Dịch vụ quá tệ"
    ]
  }
  ```

API sẽ trả về kết quả phân tích cảm xúc cho từng đánh giá:

```json
{
  "sentiments": [
    "Positive",
    "Negative"
  ]
}
```

### 3. Kiểm thử với `unittest`

Bạn có thể chạy kiểm thử dự án bằng cách sử dụng `unittest`. Chạy lệnh sau để kiểm thử tất cả các module trong thư mục `tests/`:

```bash
python -m unittest discover -s tests
```

### 4. Chạy dashboard

Chạy dashboard để xem trực quan dữ liệu và kết quả phân tích cảm xúc:

```bash
python dashboard.py
```

Dashboard sẽ chạy tại địa chỉ: `http://127.0.0.1:8050`.

## Ghi log

Mọi yêu cầu và phản hồi của API đều được ghi lại trong file log `logs/api_log.log`. Bạn có thể kiểm tra file log để theo dõi hiệu suất và lỗi.

## Cấu hình

Cấu hình dự án nằm trong file `config.py`:

```python
class Config:
    MODEL_PATH = "../model"
    TOKENIZER_PATH = "../tokenizer"
    MAX_SEQ_LENGTH = 128
    BATCH_SIZE = 32

    LOG_FILE = "logs/api_log.log"
```
## test với postman
![Alt text](/images/test_api.png)
