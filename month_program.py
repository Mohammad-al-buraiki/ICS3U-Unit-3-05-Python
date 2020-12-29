# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a month program


def main():
    # this function shows the month that the user enters its number
    
    # input
    number = int(input("Enter the month number: "))
    print("")
    
    # process
    if number == 1:
        print("January")
    elif number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("December")
    else:
        print("There is no month with the number {}".format(number))


if __name__ == "__main__":
    main()