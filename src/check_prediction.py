import joblib
import pandas as pd

model = joblib.load("models/glaucoma_model.pkl")

X = pd.DataFrame(
    [[36.88008117675781,
      25.352446825259097,
      36895,
      88718,
      0.4159]],
    columns=["Mean","Std","Cup_Area","Disc_Area","CDR"]
)

prediction = model.predict(X)

print("Prediction:", prediction[0])