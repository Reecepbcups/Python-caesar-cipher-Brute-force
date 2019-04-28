# caesar cipher Brute force attack - Reecepbcups
import string, re

letters = string.ascii_lowercase # English Alphabetical Letters

cipher = "Bpqa qa i bmab jqb wn kwlm epqkp pia jmmv omvmzibml nzwu i emjaqbm".lower() # String you wish to decrypt, all lowercase

def index(letter):
    '''Returns the index (int) of letters'''
    letterIndex = string.ascii_lowercase.find(letter)
    return int(letterIndex)

def run():
    for i in range(25): # Checks all possible letters (a->z)
        _string = ''
        
        for char in cipher:
            if char is not ' ': 
                _string += letters[index(char) - i]
            else:
                _string += char # punctuation will still glitch out and place a letter for some reason
                
        _string += f":{i}\n" # number of shifts that the cipher used
                
        # Popular english prepositions that are used in setences.
        popularPrepositions = r'the|this|and|because|there|after|against|along|among|around|before|behind|during'
        if any(re.findall(popularPrepositions, _string, re.IGNORECASE)):
            print(_string)


if __name__ == "__main__":
    run()
