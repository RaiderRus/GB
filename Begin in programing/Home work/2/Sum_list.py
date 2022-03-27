numbers = [1, 8, 3, 2, 6]
size = len(numbers)
index = 0
max = numbers[0]
min = numbers[0]

while index < size:
    if numbers[index] > max:
        max = numbers[index]
    index = index + 1

index = 0

while index < size:
    if numbers[index] < min:
        min = numbers[index]
    index = index + 1

result = 0

for i in numbers:
    result = result + i
result = result - (max + min)
print(result)
