# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]     


def find_mismatch(text):
    opening_brackets_stack = []                      # [paren: id]
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([next, i])

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1                                  
            elif "([{".index(opening_brackets_stack.pop()[0]) != ")]}".index(next):    # wrong closing
                return i + 1
            else:
                pass 
    if len(opening_brackets_stack) == 0:
        return "Success" 
    else:
        return opening_brackets_stack.pop()[1] + 1
            


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main() 
