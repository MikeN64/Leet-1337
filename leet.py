import random
import json_file_control as jfc

def encode_free(text):
    result = ""
    letters_dict = jfc.load_cheatsheet('cheatsheet/letters.json')
    numbers_dict = jfc.load_cheatsheet('cheatsheet/numbers.json')
    
    for char in text:
        if char.isdigit():
            leet_list = numbers_dict[char]
            index = random.randint(0, len(leet_list) - 1)
            leet_str = leet_list[index]
            result += leet_str

        elif char.isalpha():
            leet_list = letters_dict[char.upper()]
            index = random.randint(0, len(leet_list) - 1)
            leet_str = leet_list[index]
            result += leet_str

        else:
            result += char

    return result

if __name__ == '__main__':
    print('Leet Program starts!')
    dummy = 'The fox eats 3 apples'
    print(dummy)
    test_str = encode_free(dummy)
    print(test_str)
