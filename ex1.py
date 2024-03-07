import sys

def tokenize(expr):
    # Replace '(' and ')' with ' ( ' and ' ) ' respectively and split
    expr = expr.replace('(', ' ( ').replace(')', ' ) ')
    return expr.split()

def evaluate(tokens):
    stack = []
    
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    
    for token in tokens:
        if token in operators:
            # It's an operator
            y, x = stack.pop(), stack.pop()  # Pay attention to the order
            stack.append(operators[token](x, y))
        elif token == '(':
            # No action needed for opening bracket in this approach
            continue
        elif token == ')':
            # End of a sub-expression; nothing to do in this simplified logic
            continue
        else:
            # It's a numeric value
            stack.append(int(token))
    
    return stack.pop()

def evaluate_expression(expr):
    tokens = tokenize(expr)
    # Reverse the tokens for right-to-left evaluation
    return evaluate(reversed(tokens))

if __name__ == "__main__":
    expr = sys.argv[1]  # Assuming the expression is passed as a command-line argument
    result = evaluate_expression(expr)
    print(result)
