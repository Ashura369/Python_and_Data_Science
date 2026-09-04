def isValid(s: str) -> bool:
    stack = []          # will hold only opening braces


    # Map closing brackets to their matching opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:                 # checks if char is a closing bracket
            # It's a closing bracket: pop top from stack
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            # It's an opening bracket: push to stack
            stack.append(char)

    # Valid only if stack is completely empty
    return len(stack) == 0


# Test Examples:
print(isValid("()"))        # Output: True
print(isValid("()[]{}"))    # Output: True
print(isValid("(]"))        # Output: False
print(isValid("([)]"))      # Output: False
print(isValid("{[]}"))      # Output: True