import pandas as pd
import joblib

# Load mô hình và danh sách feature đã huấn luyện
model, feature_names = joblib.load("fraud_model.pkl")

def predict_fraud(new_transaction):
    """
    Hàm dự đoán gian lận hay không.
    """
    # Chuyển giao dịch mới thành DataFrame
    df = pd.DataFrame([new_transaction])

    # One-Hot Encoding cho các cột danh mục (giống lúc huấn luyện)
    df = pd.get_dummies(df, columns=["Loại giao dịch", "Địa điểm"])

    # Đồng bộ hóa feature: Nếu thiếu cột nào, điền giá trị 0
    df = df.reindex(columns=feature_names, fill_value=0)

    # Dự đoán
    prediction = model.predict(df)[0]
    return "Gian lận" if prediction == 0 else "Hợp lệ"

if __name__ == "__main__":
    # Ví dụ giao dịch mới cần dự đoán
    new_transaction = {
        "Ngày giao dịch": "2025-03-10",
        "Số tiền": 5000000,
        "Loại giao dịch": "Rút tiền",
        "Mã khách hàng": "KH001",  # Cột này có thể không dùng nếu không cần
        "Địa điểm": "Hà Nội"
    }

    print(predict_fraud(new_transaction))
