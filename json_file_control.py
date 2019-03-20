import json

with open('cheatsheet/numbers.json') as json_file:
    letters = json.load(json_file)
    for letter in letters:
        for l in letters[letter]:
            print(l)
