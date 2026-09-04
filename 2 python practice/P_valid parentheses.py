# valid parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.

# string consists of aprenthese only

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def isValid(s):
    braces = {
        '(':')',
        '{':'}',
        '[':']'
    }

    temp = []
    for i in s:
        # checks for opening braces
        if i in braces:
            temp.append(i)
        else:
            # checks for closing braces
            if not temp or braces[temp.pop()] != i:
                return False  
            
    return len(temp) == 0


def isValid2(s):
    braces = {')': '(', 
              '}': '{', 
              ']': '['
              }

    temp = []
    for i in s:
        if i in braces:
            if temp:
                temp2 = temp.pop()
            else:
                temp2 = '#'

            if braces[i] != temp2:
                return False
        else:
            temp.append(i)

    return len(temp) == 0



print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False
print(isValid("([)]"))    # False






