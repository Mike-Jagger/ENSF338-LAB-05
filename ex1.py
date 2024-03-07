import sys

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

def compute(expression):
    stack = Stack()
    tokens = expression.split()
    for token in reversed(tokens):
        if token in "+-*/":
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 / operand2)
        else:
            stack.push(int(token))
    return stack.pop()

def parse_expression(expression):
    expression = expression.replace('(', ' ').replace(')', ' ')
    return compute(expression)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex1.py 'expression'")
        sys.exit(1)

    expression = sys.argv[1]
    result = parse_expression(expression)
    print(result)