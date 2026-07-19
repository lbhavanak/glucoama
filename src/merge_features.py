import pandas as pd

features = pd.read_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\features.csv"
)

cdr = pd.read_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\cdr_features.csv"
)

features["Mask_Name"] = features["Image_Name"].str.replace(".jpg", ".bmp")

merged = pd.merge(features, cdr, on="Mask_Name")

merged.to_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\final_features.csv",
    index=False
)

print("Merged Records:", len(merged))
print(merged.head())