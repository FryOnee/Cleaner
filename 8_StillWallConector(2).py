from PIL import Image
import glob
import os






# Otwórz obraz czarno-biały
obraz_czarno_bialy = Image.open(f'Floor_1.png')
# Otwórz obraz z czarnymi kreskami (przezroczysty)
obraz_kreski = Image.open(f'Borders_To_Reapaire\\floor_{1}.png')
# Przytnij obraz z kreskami do rozmiaru obrazu czarno-białego
obraz_kreski = obraz_kreski.resize(obraz_czarno_bialy.size)
# Nałóż obraz z kreskami na obraz czarno-biały
obraz_czarno_bialy.paste(obraz_kreski, (0, 0), obraz_kreski)
# Zapisz wynikowy obraz
obraz_czarno_bialy.save(f'Floor_1.png')
# Zamknij oba obrazy (opcjonalnie)
obraz_czarno_bialy.close()
obraz_kreski.close()