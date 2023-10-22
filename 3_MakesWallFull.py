import cv2
import numpy as np

# Wczytaj obraz
image = cv2.imread('Floor_1.png')  # Zastąp 'twoj_obraz.jpg' nazwą pliku z obrazem

# Przekształć obraz na odcienie szarości
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Zastosuj detekcję krawędzi (możesz dostosować parametry)
edges = cv2.Canny(gray, 50, 150)

# Wykryj linie na obrazie (możesz dostosować parametry)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=150, maxLineGap=30)

# Maksymalna długość linii
max_line_length = 500  # Dostosuj wartość według potrzeb

# Dorysuj wykryte linie na oryginalnym obrazie
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        line_length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if line_length <= max_line_length:
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 0), 1)  # Dorysuj czerwoną linię

# Zapisz obraz z narysowanymi liniami
cv2.imwrite('Floor_1.png', image)

# Wyświetl obraz z kreskami
#cv2.imshow('Obraz z kreskami', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()