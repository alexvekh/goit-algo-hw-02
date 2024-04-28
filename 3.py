''' Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, 
наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, 
коли розділювачі симетричні, несиметричні, 
наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.
'''

# class Stack:
#   def __init__(self):
#     self.stack = []
#   # Додавання елемента до стеку
#   def push(self, item):
#     self.stack.append(item)
#   # Видалення елемента зі стеку
#   def pop(self):
#     if len(self.stack) < 1:
#       return None
#     return self.stack.pop()
#   # Перевірка, чи стек порожній
#   def is_empty(self):
#     return len(self.stack) == 0
#   # Перегляд верхнього елемента стеку без його видалення
#   def peek(self):
#     if not self.is_empty():
#       return self.stack[-1]



def is_simetric(str):
  stack = []
  for c in str:
    if c == "(" or c == "[" or c == "{":
      stack.append(c)
    elif c == ")" or c == "]" or c == "}":
      s = stack.pop()     
      if (s == '(' and c != ')') or \
         (s == '{' and c != '}') or \
         (s == '[' and c != ']'):
            return False
  if stack == []:
    return True
  else:
     return False


        
print(is_simetric("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(is_simetric("( 23 ( 2 - 3);"))
print(is_simetric("( 11 }"))