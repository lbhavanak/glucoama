import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\final_features.csv"
)

X = df[["Mean", "Std", "Cup_Area", "Disc_Area", "CDR"]]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = SVC(
    kernel="linear",
    class_weight="balanced"
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")

joblib.dump(
    model,
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\models\glaucoma_model.pkl"
)

print("Model Saved Successfully")