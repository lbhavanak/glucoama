import os
import cv2
import numpy as np
import pandas as pd

image_folder = r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\processed_images"

data = []

files = os.listdir(image_folder)

for file in files:
    image_path = os.path.join(image_folder, file)

    img = cv2.imread(image_path, 0)

    mean = np.mean(img)
    std = np.std(img)

    data.append([file, mean, std])

df = pd.DataFrame(data, columns=["Image_Name", "Mean", "Std"])

df.to_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\features.csv",
    index=False
)

print("Features extracted for", len(df), "images")
print(df.head())