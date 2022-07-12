# 2- Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Insert coordinates x, y, z:')

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

if not(x or y or z) == (not x) and (not y) and (not z):
    print(f'The truth of the statement ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} for all values, the predicate -', True)
else:
    print(f'The truth of the statement ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} for all values, the predicate -', False)

