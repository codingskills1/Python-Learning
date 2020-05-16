# Translator
"""
hi
""" 

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation += "g"
            if letter.isupper():
                translation += "G"
            else:
                translation += letter
        else:
            translation += letter

    return translation
print(translate(input("Enter a phrase: ")))
