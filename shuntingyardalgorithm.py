def get_input():
  return input("Enter the expression to be evaluated : ")

def separate_tokens(string):
  return

def sya(list):
  return

def infix_operations(reverse_polish):
  return

def evaluate():
  user_input = get_input()
  token_list = separate_tokens(user_input)
  reverse_polish_stack = sya(token_list)
  answer = infix_operations(reverse_polish_stack)
  return answer

def main():
  answer = evaluate()
  print(answer)

if __name__ == "__main__":
    main()
