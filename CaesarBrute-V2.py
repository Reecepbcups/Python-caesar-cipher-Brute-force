import string
import re

# Reece W (V2 - 5/25/2020)
# Caesar Cipher Brute Force
# Fixed an issue with punctuation not being added correctly.


letters = string.ascii_lowercase # English Alphabetical Letters

# String to decrypt. 
cipher = "Bpqa qa i bmab jqb wn kwlm! epqkp pia jmmv omvmzibml nzwu i emjaqbm.".lower()

def index(letter):
    '''Returns the index (int) of the alphabet'''
    return int(letters.find(letter))

def run():
    # Checks all possible letters (a->z)
    for i in range(25): 
        _string = ''
        
        for char in cipher:        
            if char not in string.punctuation + ' ': 
                _string += letters[index(char) - i]
            else:
                _string += char
                
        _string += f":{i}\n" # number of shifts that the cipher used
                
        # Popular english prepositions that are used in setences.
        popularPrepositions = r'as|be|the|this|and|because|there|after|against|along|among|around|before|behind|during'
        if any(re.findall(popularPrepositions, _string, re.IGNORECASE)):
            print(_string)


if __name__ == "__main__":
    run()
