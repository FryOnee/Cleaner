import cv2
import numpy as np
from PIL import Image
from scipy import ndimage
import glob
import os

# Określ minimalną dopuszczalną powierzchnię dla pola
minimalna_powierzchnia = 100  # Możesz dostosować tę wartość do swoich potrzeb



# Wczytaj obraz PNG
img = cv2.imread(f'Floor_1.png')
# Konwertuj obraz na tablicę NumPy, aby łatwiej manipulować pikselami
img_array = np.array(img)
# Znajdź największą figurę czarną

def find_largest_black_region(image_array):
    black_pixels = (image_array == [0, 0, 0]).all(axis=2)
    labels, num_features = ndimage.label(black_pixels)
    if num_features == 0:
        return None
    sizes = ndimage.sum(black_pixels, labels, range(num_features + 1))
    largest_label = np.argmax(sizes[1:]) + 1
    largest_black_region = (labels == largest_label)
    return largest_label, largest_black_region
largest_label, largest_black_region = find_largest_black_region(img_array)
# Znajdź obszary czarne, które mają powierzchnię mniejszą niż minimalna_powierzchnia

black_pixels = (img_array == [0, 0, 0]).all(axis=2)
labels, num_features = ndimage.label(black_pixels)
sizes = ndimage.sum(black_pixels, labels, range(num_features + 1))
# Usuń obszary, które mają powierzchnię mniejszą niż minimalna_powierzchnia, ale nie usuwaj największego obszaru

for label in range(1, num_features + 1):
    if sizes[label] < minimalna_powierzchnia and label != largest_label:
        img_array[labels == label] = [255, 255, 255]  # Kolor biały
# Konwertuj tablicę NumPy z powrotem na obraz Pillow
result_img = Image.fromarray(img_array)
# Zapisz zmodyfikowany obraz
result_img.save(f'Floor_1.png')
