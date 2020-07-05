import json as js

data = js.load(open("S:\Edu\Python Data Structures and Algorithms\Python Fundamentals\data.json"))

def translet(word):

    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("\n\nNo entries found")


word = input("\n\nEnter the word you want to search\n")
output = translet(word)

if output is None:
    print("")
else:
    print("\nThe defination is as follows : \n\n", output)

