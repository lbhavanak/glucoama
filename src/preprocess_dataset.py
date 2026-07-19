import os
import cv2
from preprocessing import preprocess_image

input_folder = r"C:\Users\HP\Downloads\REFUGE2\REFUGE2\train\images"
output_folder = r"C:\Users\HP\OneDrive\Desktop\GLUCOMA\datasets\processed_images"

os.makedirs(output_folder, exist_ok=True)

files = os.listdir(input_folder)

count = 0

for file in files:
    image_path = os.path.join(input_folder, file)

    processed = preprocess_image(image_path)

    save_path = os.path.join(output_folder, file)

    cv2.imwrite(save_path, processed)

    count += 1

print("Saved Images:", count)