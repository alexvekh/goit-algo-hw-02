''' Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, 
наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, 
коли розділювачі симетричні, несиметричні, 
наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.
'''

# Додатково можна ще спростити №3 якщо використати словник, як приклад:

def is_simetric(expression):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != brackets_map[char]:
                return False          
    if stack:
        return False
    else:
        return True

print(is_simetric("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(is_simetric("( 23 ( 2 - 3);"))
print(is_simetric("( 11 }"))