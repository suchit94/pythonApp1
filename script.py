import json
from difflib import get_close_matches

#load dictionary data into variable called 'data'
data = json.load(open("data.json"))

#create function 
def translation(w):
    #whenever words get passed into this function, it will convert all characters to lower case
    w = w.lower()
    #conditional if word passed into function is present in 'data.json'
    if w in data:
        #return key 'word' from the 'data.json' file
        return data[w]
    #condition used if word is incorrect but similar to keyword in dictionary
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("did you mean %s instead? Enter Y if yes, N if not: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist, Please double check word."
        else:
            return "We did not understand your input."
    #else condition used if word is not fount in 'data.json'
    else:
        return "The word does not exist, Please double check word."
#ask user to enter a word and assign it to the variable 'word'
word = input("Enter word: ")

#print out function with word as paramenter which will output the dictionary definition 
output = translation(word)

if type(output) == list:
    #create for loop to create a more readable output
    for item in output:
        print(item)
else:
    print(output)