import pandas as pd
import joblib

model = joblib.load(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\models\glaucoma_model.pkl"
)

df = pd.read_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\final_features.csv"
)

X = df[["Mean", "Std", "Cup_Area", "Disc_Area", "CDR"]]

predictions = model.predict(X)

print("Total Predictions:", len(predictions))
print(predictions[:20])