from fraud_detection.predict import predict_fraud
import pandas as pd

# Đọc file CSV với dấu phân cách là dấu chấm phẩy
df = pd.read_csv("Du_lieu_du_doan_gian_lan_ke_toan.csv", delimiter=";")

# In ra danh sách các cột trong DataFrame để kiểm tra
print(df.columns)


# Dự đoán cho tất cả các giao dịch
result = predict_fraud(df)

# In kết quả hoặc lưu vào file mới
print(result)
result.to_csv("result_predictions.csv", index=False)  # Lưu kết quả dự đoán vào file CSV mới
