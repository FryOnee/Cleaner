from PIL import Image

def czarno_biale_png(input_file, output_file, prog_czerni):
    # Otwarcie pliku PNG
    img = Image.open(input_file)
    
    # Konwersja obrazu do trybu odcieni szarości
    img = img.convert("L")
    
    # Pobranie danych pikseli
    piksele = img.load()
    
    # Rozmiary obrazu
    szerokosc, wysokosc = img.size
    
    # Przejście przez piksele i zastosowanie progowania
    for x in range(szerokosc):
        for y in range(wysokosc):
            if piksele[x, y] < prog_czerni:
                piksele[x, y] = 0  # Biały
            else:
                piksele[x, y] = 255    # Czarny
    
    # Zapis obrazu do pliku wyjściowego
    img.save(output_file)

if __name__ == "__main__":
    input_file = "Floor.png"  # Zmień na ścieżkę do swojego pliku wejściowego
    output_file = "Floor_1.png"  # Zmień na nazwę pliku wyjściowego
    prog_czerni = 70  # Prog czerni (0-255), można dostosować według potrzeb

    czarno_biale_png(input_file, output_file, prog_czerni)
