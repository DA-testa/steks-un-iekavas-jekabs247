
# Jēkabs Kindzulis, 221RDC047, 18.gr

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1
            else:
                temp = opening_brackets_stack.pop()
                if not are_matching(temp[0], next):
                    return i+1

    if opening_brackets_stack:
        return opening_brackets_stack[0][1]+1

    return "Success"

def main():

 
    text = input()

    #n = len(text)
    #if n < 1 or n > 105:
     #   print("Invalid input length. Length must be between 1 and 105.")
     #   return

    mismatch = find_mismatch(text)

    # Printing answer, write your code here

    print(mismatch)

if __name__ == "__main__":
    main()
