import sys

class Stack:
    def __init__(self):
        self.items = []  

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack. If the stack is empty, raise an error.
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        # Return the top item of the stack without removing it. If the stack is empty, raise an error.
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

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
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ex1.py 'expression'")
        sys.exit(1)

    expression = sys.argv[1]
    result = parse_expression(expression)
    print(result)