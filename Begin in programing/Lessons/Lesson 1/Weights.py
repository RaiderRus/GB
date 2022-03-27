a = 10
b = 18
c = 50
d = 18
e = 16

maximum = a

if b > a:
    b = maximum
if c > maximum:
    maximum = c
if d > maximum:
    maximum = d
if e > maximum:
    maximum = e

print('Самая тяжелая гиря весит', maximum, 'кг.')
