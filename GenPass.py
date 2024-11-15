import requests
import random

url="https://raw.githubusercontent.com/Aiioonairr/Dict_fr-5-6-/refs/heads/main/dico_fr_min.txt"
# Download file contents
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Split file contents into lines
    lignes = response.text.splitlines()
    
    # checking the presence of lines
    if lignes:
        # choose a random line
        list_symbol=['+','!',"=","-","_"]
        word1= random.choice(lignes)
        word2= random.choice(lignes)
        number = random.randrange(10, 99)
        symbol = random.choice (list_symbol)

        print(f"{word1}{number}{word2}{symbol}")
    else:
        print("The file is empty")
else:
    print(f"Error downloading file: {response.status_code}")
