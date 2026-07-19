import cv2
import numpy as np

def calculate_cdr(mask_path):

    mask = cv2.imread(mask_path, 0)

    disc_area = np.sum(mask == 128)
    cup_area = np.sum(mask == 255)

    cdr = cup_area / disc_area if disc_area != 0 else 0

    return cup_area, disc_area, cdr