import json

def load_cheatsheet(json_file):
    with open(json_file) as json_file:
        leet_dict = json.load(json_file)
        return leet_dict
