''' функція, яка приймає рядок, додає всі його символи до двосторонньої черги deque (collections), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою 
до регістру та пробілів.
'''
from collections import deque

def is_palindrom(str):
  dq = deque()
  dq.extend(str.lower().replace(' ', ''))

  while len(dq) > 1:
    right_char = dq.pop()
    left_char = dq.popleft()
    if right_char != left_char:
      return False
  return True
        
# print(is_palindrom("rokttkor"))

