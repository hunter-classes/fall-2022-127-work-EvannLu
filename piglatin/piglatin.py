def bondify(name):
    result = ""
    first = name[0]
    first = first.upper()
    result = result + first + "."
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result
  
print(bondify("Evan Lu"))


def piglatin(word):
    first = word[0].lower()
    if(first == "a" or first == "e" or first == "i" or first == "o" or first == "u"):
        return word + "yay"
    else:
        return word[1:] + word[0] + "ay"

print(piglatin("Oye"))
print(piglatin("piglatin"))


