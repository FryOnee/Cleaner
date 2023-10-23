from PIL import Image, ImageDraw
import glob
import os
#zamienia biale na czarne px





input_image = Image.open(f'Floor_1.png')
# Konwertuj obraz na tryb RGBA
input_image = input_image.convert('RGBA')
# Zefiniuj kolory
color_black = (0, 0, 0, 255)  # Czarny w formacie RGBA
color_white = (255, 255, 255, 255)  # Biały w formacie RGBA
color_red = (255, 255, 255, 255)  # Czerwony w formacie RGBA
# Torzenie pustego obrazu RGBA o takim samym rozmiarze
boundary_image = Image.new('RGBA', input_image.size, (0, 0, 0, 0))
# Ieracja przez piksele obrazu (bez krawędzi)
for x in range(1, input_image.width - 1):
    for y in range(1, input_image.height - 1):
        pixel_color = input_image.getpixel((x, y))
        if pixel_color == color_black:
            # Sprawdź sąsiednie piksele
            neighbors = [
                input_image.getpixel((x - 1, y)),
                input_image.getpixel((x + 1, y)),
                input_image.getpixel((x, y - 1)),
                input_image.getpixel((x, y + 1)),
            ]
            if any(neighbor == color_white for neighbor in neighbors):
                boundary_image.putpixel((x, y), color_black)

boundary_image.save(f'Borders_To_Reapaire\\floor_1.png')
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Wczytaj obraz PNG
#input_image = boundary_image
input_image = boundary_image

# Utwórz nowy obraz o takich samych rozmiarach, ale przezroczysty
output_image = Image.new("RGBA", input_image.size, (0, 0, 0, 0))

# Przekształć obraz
draw = ImageDraw.Draw(output_image)
width, height = input_image.size

for x in range(width):
    for y in range(height):
        pixel = input_image.getpixel((x, y))
        if pixel == (0, 0, 0, 255):  # czarny piksel (RGBA)
            # Rysuj carne piksel o rozmiarze 9x9
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    draw.point((i, j), fill=(0, 0, 0, 255))

# Zapisz przekształcony obraz
output_image.save(f'Borders_To_Reapaire\\floor_1.png')