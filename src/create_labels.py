import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\final_features.csv"
)

df["Label"] = df["Image_Name"].apply(
    lambda x: 1 if x.startswith("g") else 0
)

df.to_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\final_features.csv",
    index=False
)

print(df[["Image_Name", "Label"]].head())
print("Total Records:", len(df))