numbers = [1, 8, 3, 2, 6]
size = len(numbers)
index = 0
max = numbers[0]

while index < size:
    if numbers[index] > max:
        max = numbers[index]
    index = index +1

print(max)
