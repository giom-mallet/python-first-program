import json
import difflib
from difflib import SequenceMatcher

with open("english_dic/data.json") as datafile : 
    data = json.load(datafile)

def find_match(word) :
    match = ""
    ratio = 0

    for key in data.keys(): 
        similarity = SequenceMatcher(None, key, word).ratio()
        if similarity > 0.5 and similarity > ratio :
            match = key
            ratio = similarity
    
    return match



def definition(word) : 
    word = word.lower()
    result = ""
    
    if word in data.keys() : 
        definitions = data[word]      

    elif word.capitalize() in data.keys() :
        definitions = data[word.capitalize()]
    elif word.upper() in data.keys() :
        definitions = data[word.upper()]
    else :
        new_word = find_match(word)
        if new_word == "" :
            return "This word is not in our Dictionary"
        else :
            prompt = "Did you mean {} ? Y/N :".format(new_word)
            response = input(prompt)
            if response == "Y" :
                return definition(new_word)
            else : 
                return "This word is not in our Dictionary"

    for text in definitions : 
        result = result + text + "\n"
    return result
        

word = input("Please Enter a word: ")
print(definition(word))
