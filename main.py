import sys

class bra:
    def __init__(self, btype, index):
        self.btype = btype
        self.index = index

text = ""

if len(sys.argv) > 1:
    text = sys.argv [1]
else:
    text = input("Input String to Check: ")

arr = []
prev = ""

for x in range(len(text)):
    c = text[x]

    if c == '[' or c == '{' or c =='(':
        arr.append(bra(c, x))
    elif c == ']' or c == '}' or c == ')':
        if len(arr) < 1:
            sys.exit("Missing opening bracket for " + c + " at index: " + str(x))
        else:
            prev = arr.pop(len(arr) -1)

            if c == ']' and prev.btype != '[':
                sys.exit("Bracket Mismatch at index: " + str(x) + " \'" + text[prev.index: x + 1] + "\'")
            elif c == '}' and prev.btype != '{':
                sys.exit("Bracket Mismatch at index: " + str(x) + " \'" + text[prev.index: x + 1] + "\'")
            elif c == ')' and prev.btype != '(':
                sys.exit("Bracket Mismatch at index: " + str(x) + " \'" + text[prev.index: x + 1] + "\'")

for bracket in arr:
    sys.exit(bracket.btype + " at index: " + str(bracket.index) + " Missing Closing Bracket")

print("No Mismatches found!")
sys.exit(0)
        
    