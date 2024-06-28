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

  #print(token_list)
  return token_list

def sya(list):
  return

def infix_operations(reverse_polish):
  return

def evaluate(expression):
  token_list = separate_tokens(expression)
  reverse_polish_stack = sya(token_list)
  answer = infix_operations(reverse_polish_stack)
  return answer

def main():
  user_input = get_input()
  answer = evaluate(user_input)
  print(answer)

if __name__ == "__main__":
    main()
