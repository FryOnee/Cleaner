import os
import subprocess


# take path from your pc
#i know i could make one more function which make it and import this string to other files
biezacy_katalog = os.path.dirname(os.path.abspath(__file__))

# replace one '\' by '\\'
biezacy_katalog = biezacy_katalog.replace('\\', '\\\\')

# path to folder which included py files
folder_path = biezacy_katalog

# file list to run
file_names = [

    "1_Walls.py",
    "2_Delates.py",
    "3_MakesWallFull.py",
    "4_border.py",
    "5_furnitureDelate.py",
    "6_MakesWallFull.py",
    "7_StillWallCorection(1).py",
    "8_StillWallConector(2).py",
    "7_StillWallCorection(1).py",
    "8_StillWallConector(2).py",
    "9_furnitureDelate.py",


]

# look to run the functions
for file_name in file_names:
    full_path = os.path.join(folder_path, file_name)
    # print(f"Uruchamiam plik: {full_path}")
    
    # run and wait to compile this file
    result = subprocess.run(["python", full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
    # print result
    if result.returncode == 0:
        print(f"Plik {file_name} end work without errors")
    else:
        print(f"Plik {file_name} end work with error:")
        print(result.stderr)
        break