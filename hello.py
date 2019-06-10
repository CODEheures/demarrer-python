import random
import json

response = "A"

### Return a random elem of a list ###
def get_random_elem(array: list):
    random_index = random.randrange(0, len(array)-1)
    return array[random_index]

### Return a list by a json file and key name ###
def loadJson(file_name: str, key_name: str):
    my_list = []
    with open(file_name,'r',1,"utf8") as file:
        data = json.load(file)
    for entry in data:
        my_list.append(entry[key_name])

    return my_list

### Return list of characters ###
def get_characters():
    return loadJson("characters.json", "character")

### Return list of characters ###
def get_random_character():
    return get_random_elem(get_characters())

### Return list of quotes ###
def get_quotes():
    return loadJson("quotes.json", "quote")

### Return list of characters ###
def get_random_quote():
    return get_random_elem(get_quotes())

while response != "b":
    printed = "{character} a dit: {quote}"
    print(printed.format(character=get_random_character(), quote=get_random_quote()))
    response = input("Appuyez sur Entrée pour continuer ou sur 'b' pour stopper")
