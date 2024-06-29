# Declaring the operators in the order of precedence from high to low
# Reverses the order to make it from low to high (so we can compare the order using indices)
OPERATORS = [op for op in "^/*+-"][::-1]

def get_input():
  return input("Enter the expression to be evaluated : ")

def separate_tokens(expression):
  ''' Takes a mathematical expression of type string and returns a list with all
      the operations(as type string) and numbers(as type integer) as elements of
      the list.
      This function makes iterating over the tokens easier.
  '''
  token_list = []
  is_reading_number = False
  number_read = ""
  for char in expression:
    if char==' ':
      continue
    else:
      if char.isdigit():
        is_reading_number = True
        number_read += char
      else:
        if is_reading_number:
          token_list.append(int(number_read))
          is_reading_number = False
          number_read = ""
        token_list.append(char)
  if is_reading_number:
    token_list.append(int(number_read))

  return token_list

def sya(list):
  ''' Takes a list of tokens of the infix-notation format and returns a list of tokens
      in the postfix-notation format
  '''
  queue = []
  stack = []
  # Read a token
  for token in list:
    # If it's a number, add it to QUEUE
    if type(token) == type(9):
      queue.append(token)
    # If its an operator
    elif token in OPERATORS:
      token_rank = OPERATORS.index(token) # Get the precedence of the operator read
      # While there's an operator with higher precedence on the top of the STACK, pop that operator onto the QUEUE
      while len(stack)>0 and (stack[-1] in OPERATORS) and OPERATORS.index(stack[-1]) > token_rank:
        queue.append(stack.pop())
      stack.append(token) # Add operator read to STACK
    # If it's a left bracket, add it to the STACK
    elif token == '(':
      stack.append(token)
    # If its a right bracket
    elif token == ')':
      # While there's no left bracket on the top of the STACK, pop operators from the stack onto the QUEUE
      while len(stack)>0 and stack[-1]!='(':
        queue.append(stack.pop())
      stack.pop() # Discard the left bracket
    # Inavlid input, so return empty list
    else:
      return []
  # While there are operators on the stack, pop them onto the QUEUE
  while len(stack)>0:
    queue.append(stack.pop())

  return queue

def operate(a,b,operator):
  ''' Performs the operation a operator b and returns the result of the operation
  '''
  if operator == "^":
    return a**b
  elif operator == "/":
    return a/b
  elif operator == "*":
    return a*b
  elif operator == "+":
    return a+b
  elif operator == "-":
    return a-b

def perform_operations(reverse_polish):
  ''' Takes a list of tokens in postfix-notation and returns the evaluated expression
  '''
  stack = []
  for token in reverse_polish:
    if type(token) == type(9):
      stack.append(token)
    elif token in OPERATORS:
      n2 = stack.pop()
      n1 = stack.pop()
      result = operate(n1,n2,token)
      stack.append(result)
  return stack.pop()

def evaluate(expression):
  try:
    token_list = separate_tokens(expression)
    reverse_polish_stack = sya(token_list)
    answer = perform_operations(reverse_polish_stack)
    return answer
  except ZeroDivisionError:
    return "Invalid Expression ( Division by 0 )"
  except:
    return "Inavlid Expression"

def main():
  user_input = get_input()
  answer = evaluate(user_input)
  print(answer)

if __name__ == "__main__":
    main()
