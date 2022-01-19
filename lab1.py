"""
Program to count up to a given max value.

author: Reis Gadsden
version: 18/01/2022
class: CS-5531 @ Appalachian State University
"""
import re


def main():
    MD = []

    # regex pattern for checking user input
    num_pattern = re.compile("^[1-9]$")

    # print a welcome prompt
    print("Please enter numeric values corresponding to the descend"
          "ing order of your array (must be 1 - 9). Enter 'q' when finished.")

    # loop until user has prompted they are done entering values
    while True:
        user_input = input("Please enter value: ").strip()
        if re.fullmatch(num_pattern, user_input) is not None:
            MD.append(int(user_input))
        elif user_input == 'q' or user_input == 'Q':
            break
        else:
            print("Invalid input! Try again.")

    # execute method to count up to max value
    addToMax(MD)


def addToMax(md):
    # calculates a max value for the given array
    static_max_val = 1
    count_up = []
    for i in md:
        static_max_val *= (i + 1)
        count_up.append(0)
    static_max_val -= 1

    # adds values up to max value
    for i in range(0, static_max_val + 1):
        counter = 1
        max_val = i
        max_converted = []
        while True:
            mod_val = max_val % (md[-counter] + 1)
            max_val = max_val // (md[-counter] + 1)
            max_converted.insert(0, mod_val)
            if max_val == 0 or max_val == -1:
                break
            counter += 1
            if counter > len(md):
                counter = 1

        # for values less then (1, ..., 0)
        # fills in the leading digits with 0
        while len(max_converted) != len(md):
            max_converted.insert(0, 0)
        print(max_converted)



if __name__ == "__main__":
    main()