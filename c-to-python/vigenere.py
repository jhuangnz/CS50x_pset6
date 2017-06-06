##
#   Implements 'Vigenere' in Python code (see pset2)
# 
#   Author: Julie Huang, julie@juliehuang.co.nz
#  
#   This file converts the solution of the Vigenere algorithm problem written in C
#   to Python code.
# 
#   CS50x

import cs50
import sys

def main():
    
    if len(sys.argv) != 2:  # one encryption key allowed, reprompt if otherwise
        print("Command-line error, please try again")
        exit()
    
    key = sys.argv[1]  # store argv[1] as string
    key_length = len(sys.argv[1])  # store length of key 
    
    # key must contain only alphabets - exit if otherwise
    if key.isalpha() == False: 
        print("Use alpha characters only, please try again")
        exit()
    else:
        print("plaintext:")
        plaintext = cs50.get_string()  # get plain text from user
        plaintext_length = len(plaintext)  # store string length of plain text
        
    print("ciphertext:")
    
    x = 0  # tracks modulo wrap of key length
    for i in range(0, plaintext_length):  # iterate through plain text
        
        if key[x].islower():
            modulo = ord(key[x]) - 97  # finds modulo of lowercase character in ASCII
        else:
            modulo = ord(key[x]) - 65  # finds modulo of uppercase character in ASCII
            
        shift = ord(plaintext[i]) + modulo # temporary encryption
        
        if plaintext[i].isalpha():  # if i'th character of plain text is alphabetical
            
            x = x + 1  # increment x counter 
            if x == key_length:  # if x encounters a wrap, reset counter
                x = 0
                
            if plaintext[i].islower:
                print_character(x = shift, y = 122, z = 97)  # if i'th of plain text is ASCII lowercase 
            else:      
                print_character(x = shift, y = 90, z = 65)  # if i'th of plain text is ASCII uppercase
        else:
            print("{}".format(plaintext[i]), end = "")  # if i'th of plain text is not alphabetical, print as is
            
    print()  # new line
    exit()
                
#  determines final encryption             
def print_character(x, y, z):
    
    # if temporary encryption > upper bounds of ASCII alphabets (i.e 'Z' or 'z'), apply modulo for final encryption
    if x > y:
        character = (z - 1) + (x - y) 
        print("{}".format(chr(character)), end = "")
        return character
    else:
        print("{}".format(chr(x)), end = "")  # if temporary encryption is below upper bounds, encryption stays the same
        return x

if __name__ == "__main__":
    main()