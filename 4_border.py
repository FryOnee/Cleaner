from PIL import Image, ImageOps

# Ścieżka do istniejącego pliku PNG
input_image_path = 'Floor_1.png'

# Wymiary ramki (np. 10 pikseli)
border_size = 10

# Wczytaj obraz
image = Image.open(input_image_path)

# Dodaj czarną ramkę
image_with_border = ImageOps.expand(image, border=border_size, fill='black')

# Zapisz obraz z ramką
output_image_path = 'Floor_1.png'
image_with_border.save(output_image_path)

#print(f'Zapisano obraz z ramką jako {output_image_path}')
