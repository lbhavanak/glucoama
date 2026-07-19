import cv2
import os
import matplotlib.pyplot as plt

mask_path = r"C:\Users\HP\Downloads\REFUGE2\REFUGE2\train\mask"

files = os.listdir(mask_path)

mask = cv2.imread(os.path.join(mask_path, files[0]), 0)

print("Unique Pixel Values:", sorted(list(set(mask.flatten())))[:20])

plt.imshow(mask, cmap="gray")
plt.title(files[0])
plt.axis("off")
plt.show()