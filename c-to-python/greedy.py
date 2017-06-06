#!/usr/bin/env python3

##
#   Implements 'Greedy' in Python code (see pset1)
# 
#   Author: Julie Huang, julie@juliehuang.co.nz
#  
#   This file converts the solution of the Greedy algorithm problem written in C
#   to Python code.
# 
#   CS50x


import cs50

def main():
    
    #  prompt user for change that is > 0, else re-prompt
    while True:
        print("Please type in your change below for the number of coins")
        change = cs50.get_float()
        if change > 0:
            break
    
    change_cents = round((change * 100), 2)  # convert change to cents, round to nearest penny
    total_coins = 0  # coin tracker
    
    while change_cents > 0:  # deduct coins as long as change_cents not 0

        while change_cents > 24:
            change_cents = leftover(change_cents, coin = 25)  # deducts quarters
            total_coins = total_coins + 1  # update coin tracker
        
        while change_cents > 9:
            change_cents = leftover(change_cents, coin = 10)  # deducts dimes
            total_coins = total_coins + 1  # update coin tracker
           
        while change_cents > 4:
            change_cents = leftover(change_cents, coin = 5)  # deducts nickels
            total_coins = total_coins + 1  # update coin tracker
            
        break
    
    print("{}".format(total_coins))  # print result

# figures out remaining change after coin is deducted
def leftover(change_cents, coin):
    change_cents = change_cents - coin
    return change_cents

if __name__ == "__main__":
    main()
    
