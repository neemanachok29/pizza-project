def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    

    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  