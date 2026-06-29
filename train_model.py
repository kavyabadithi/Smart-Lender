import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import joblib

# Load Dataset
data = pd.read_csv("templates/static/dataset.csv")

# Encode categorical columns
le_dict = {}

for col in data.select_dtypes(include=["object", "string"]).columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col].astype(str))
    le_dict[col] = le

X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"].astype(int)

# Convert target labels to numeric values for XGBoost
if y.dtype == object:
    y = le_dict["Loan_Status"].transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "loan_model.pkl")
joblib.dump(le_dict, "label_encoders.pkl")

print("Model Saved Successfully")