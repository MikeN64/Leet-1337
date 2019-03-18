import json

with open('cheatsheet/letters.json') as json_file:
    letters = json.load(json_file)
    for letter in letters:
        for l in letters[letter]:
            print(l)
