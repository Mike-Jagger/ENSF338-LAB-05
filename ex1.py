import sys


class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack items

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack. If the stack is empty, raise an error.
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        # Return the top item of the stack without removing it. If the stack is empty, raise an error.
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")


def compute(expression):
    stack = Stack()  
    tokens = expression.split()  
    # Iterate over tokens in reverse order to process them using stack logic
    for token in reversed(tokens):
        if token in "+-*/":  
            operand1 = stack.pop()  # Pop the first operand from the stack
            operand2 = stack.pop()  # Pop the second operand from the stack
         
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 / operand2)
        else:
            stack.push(int(token))  # If the token is a number, convert it to int and push onto the stack
    return stack.pop()  # Return the result by popping the last item from the stack


def parse_expression(expression):

    expression = expression.replace('(', ' ').replace(')', ' ')
    return compute(expression)  # Compute and return the value of the simplified expression


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex1.py 'expression'")  
        sys.exit(1)

    expression = sys.argv[1] 
    result = parse_expression(expression) 
    print(result) 
