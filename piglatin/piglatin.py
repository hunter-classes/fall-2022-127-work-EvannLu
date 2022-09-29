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
    length = len(word)
    first = word[0].lower()
    if(first in 'aeiou'):
        if(word[length - 1] in '!,.?'):
            punc = word[length - 1]
            word = word[0:length - 1] + 'yay' + punc
            return word
        else:
            if word[length - 1] in '!,.?':
                punc = word[length - 1]
                nword = word[1:length - 1] + first + "ay" + punc
                return nword

print(piglatin("Aids!"))


