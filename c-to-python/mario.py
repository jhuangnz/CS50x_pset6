##
#   Implements 'Mario' in Python code (see pset1)
# 
#   Author: Julie Huang, julie@juliehuang.co.nz
#  
#   This file converts the solution of the Mario algorithm problem written in C
#   to Python code.
# 
#   CS50x

import cs50

def main():
    
    #  prompt user for positive integer <= 23, else re-prompt
    while True:
        height = cs50.get_int()
        if height > 23 or height < 0:
            print("Hi! To make Mario's pyramid, please provide a positive integer less than or equal to 23:")
        else: 
            break
        
    rows = 1 
    spaces = ((height -1)- rows)
    hashes = 24 - rows
    
    for rows in range(rows, height + 1):  #  for each row in pyramid:
        
        for spaces in range(height - rows, 0, -1):  # spaces algorithm
            print(" ", end = "")  # print spaces
            
        for hashes in range((24 - rows), 25):  # hashes algorithm
            print("#", end = "")  # print hashes
            
        print()  # print new line 
            
if __name__ == "__main__":
    main()
    
