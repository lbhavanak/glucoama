import cv2
import numpy as np

def extract_features(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mean = np.mean(gray)
    std = np.std(gray)

    return [mean, std]