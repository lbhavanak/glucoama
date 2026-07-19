from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/glaucoma_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    image = request.files["image"]

    image_path = "uploads/" + image.filename
    image.save(image_path)

    df = pd.read_csv("datasets/final_features.csv")

    row = df[df["Image_Name"] == image.filename]

    if row.empty:
        return f"{image.filename} not found in final_features.csv"

    X = row[["Mean", "Std", "Cup_Area", "Disc_Area", "CDR"]]

    result = model.predict(X)[0]

    if result == 1:
        prediction = "⚠ Glaucoma Detected"
    else:
        prediction = "✅ Normal Eye"

    return render_template(
        "result.html",
        filename=image.filename,
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)