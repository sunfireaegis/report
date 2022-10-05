

import ast 

text = ast.parse('''
def f(a) -> int:
    return a + 1

a = int(input())
print(f(a))
''')

with open('res.txt', 'w+') as file:
    file.writelines(ast.dump(text))
