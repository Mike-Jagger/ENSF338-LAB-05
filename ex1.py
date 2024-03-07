class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            stack.push(token)
        elif token == '(':
            continue
        elif token == ')':
            subexpression_result = evaluate_subexpression(stack)
            if subexpression_result is not None:
                stack.push(subexpression_result)
            else:
                return "Error: Invalid expression format"
    return stack.pop()

def evaluate_subexpression(stack):
    operator = stack.pop()
    if operator not in ['+', '-', '*', '/']:
        return None
    
    operands = []
    while isinstance(stack.peek(), int):
        operands.append(stack.pop())
    operands.reverse()

    if len(operands) < 2:
        return None
    
    if operator == '+':
        return sum(operands)
    elif operator == '-':
        return operands[0] - sum(operands[1:])
    elif operator == '*':
        result = 1
        for operand in operands:
            result *= operand
        return result
    elif operator == '/':
        result = operands[0]
        for operand in operands[1:]:
            if operand == 0:
                return "Error: Division by zero"
            result /= operand
        return result
    else:
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)

    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(result)
