# Accounting Fraud Detection AI Package - Phát hiện gian lận kế toán bằng AI

## Tác giả: Trần Minh Tâm

## Mô tả:
Đây là package AI phát hiện gian lận kế toán dựa trên các giao dịch. Sử dụng mô hình RandomForest để dự đoán gian lận từ các giao dịch.

## Cài đặt:
Sử dụng lệnh dưới để cài đặt package:
  pip install accounting-fraud-detector

## Chuẩn bị dữ liệu trên file .csv phải giống như vầy:
![image](https://github.com/user-attachments/assets/ebc6d4e2-3923-4cf6-a972-6a0a67d514dd)



## Cách sử dụng:
1. **Huấn luyện mô hình**:
   ```python
   from fraud_detection.model import train_fraud_model
   train_fraud_model()

2. **Du doan gian lan**
  ```python
  from fraud_detection.predict import predict_fraud
  import pandas as pd

  # Đọc file CSV với dấu phân cách là dấu chấm phẩy
  df = pd.read_csv("C:/Users/ADMIN/Documents/Du_lieu_du_doan_gian_lan_ke_toan.csv", delimiter=";")

  # In ra danh sách các cột trong DataFrame để kiểm tra
  print(df.columns)


  # Dự đoán cho tất cả các giao dịch
  result = predict_fraud(df)

  # In kết quả hoặc lưu vào file mới
  print(result)
  result.to_csv("result_predictions.csv", index=False)  # Lưu kết quả dự đoán vào file CSV mới

3. **API**
  ```python
  python fraud_detection\api.py 

