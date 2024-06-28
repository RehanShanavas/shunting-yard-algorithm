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
  queue = []
  stack = []
  for token in list:
    if type(token) == type(9):
      queue.append(token)
    elif token in OPERATORS:
      token_rank = OPERATORS.index(token)
      while len(stack)>0 and (stack[-1] in OPERATORS) and OPERATORS.index(stack[-1]) > token_rank:
        queue.append(stack.pop())
      stack.append(token)
    elif token == '(':
      stack.append(token)
    elif token == ')':
      while len(stack)>0 and stack[-1]!='(':
        queue.append(stack.pop())
      stack.pop()
  while len(stack)>0:
    queue.append(stack.pop())

  return queue

def perform_operations(reverse_polish):
  return

def evaluate(expression):
  token_list = separate_tokens(expression)
  reverse_polish_stack = sya(token_list)
  answer = perform_operations(reverse_polish_stack)
  return answer

def main():
  user_input = get_input()
  answer = evaluate(user_input)
  print(answer)

if __name__ == "__main__":
    main()
