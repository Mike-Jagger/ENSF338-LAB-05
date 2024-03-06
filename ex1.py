# Function to check if a character is a digit
def is_digit(char):
  return char.isdigit()

# Function to check if a character is an operand
def is_operand(char):
  return char in "+-*/"

# Main parsing function
def parse_expression(expression):
  stack = []
  for char in expression:
    if is_digit(char):
      # Add number to the stack
      number = int(char)
      stack.append(number)
    elif is_operand(char):
      # Pop two elements from the stack, perform operation, and push result back
      operand2 = stack.pop()
      operand1 = stack.pop()
      result = perform_operation(char, operand1, operand2)
      stack.append(result)
    # Handle errors: invalid characters, unbalanced parentheses, etc.
  # Check if the stack contains only one element (final result)
  if len(stack) == 1:
    return stack.pop()
  else:
    # Handle errors: unprocessed elements in the stack
    raise ValueError("Invalid expression")

# Function to perform the operation based on the operand
def perform_operation(operand, operand1, operand2):
  if operand == "+":
    return operand1 + operand2
  # Implement similar logic for other operands
  # ...
  else:
    raise ValueError("Unsupported operand")

# Get expression string from command line arguments (replace with actual method)
expression_string = "10 + 20 * 3"

# Parse the expression
result = parse_expression(expression_string)

# Print the result
print(result)