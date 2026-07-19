import pandas as pd
import joblib

model = joblib.load("models/glaucoma_model.pkl")

df = pd.read_csv("datasets/final_features.csv")

X = df[["Mean","Std","Cup_Area","Disc_Area","CDR"]]

pred = model.predict(X)

print("Predicted 0:", sum(pred == 0))
print("Predicted 1:", sum(pred == 1))