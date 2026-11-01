
def evaluate_postfix(expression):
    stack = []

    for item in expression.split():
        if item.isdigit():
            stack.append(int(item))
        else:
            b = stack.pop()
            a = stack.pop()

            if item == "+":
                stack.append(a + b)
            elif item == "-":
                stack.append(a - b)
            elif item == "*":
                stack.append(a * b)
            elif item == "/":
                stack.append(a // b)

    return stack.pop()


expression = "5 3 + 2 *"
print(evaluate_postfix(expression))
