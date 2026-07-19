import os
import cv2
import numpy as np
import pandas as pd

mask_folder = r"C:\Users\HP\Downloads\REFUGE2\REFUGE2\train\mask"

data = []

for file in os.listdir(mask_folder):

    mask_path = os.path.join(mask_folder, file)

    mask = cv2.imread(mask_path, 0)

    cup_area = np.sum(mask == 0)
    disc_ring = np.sum(mask == 128)

    disc_area = cup_area + disc_ring

    cdr = cup_area / disc_area if disc_area > 0 else 0

    data.append([
        file,
        cup_area,
        disc_area,
        round(cdr, 4)
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Mask_Name",
        "Cup_Area",
        "Disc_Area",
        "CDR"
    ]
)

df.to_csv(
    r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\cdr_features.csv",
    index=False
)

print("CDR calculated for", len(df), "masks")
print(df.head())