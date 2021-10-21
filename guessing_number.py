# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on September 2021
# This program is a number guessing game.

import constant


def main():
    # this function is to guessing the number
    # input
    random_number = int(input("Enter a random number from 0 to 9 here: "))

    # process
    if random_number == constant.ANSWER:
        # output
        print("")
        print("congratulations!")
        print("you got it right")
    
    else:
        print("")
        print("oops! you got it wrong")
        print("try again")
        
    print("\ndone")


if __name__ == "__main__":
    main()
