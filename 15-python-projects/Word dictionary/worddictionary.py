from pyDictionary import pyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break
    
    print(dictionary.meaning(word))