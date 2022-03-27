numbers = [2, -3, -7, 5, -4]
size = len(numbers)
count = 0
index = 0

while index < size:
    if numbers[index] > 0:
        count = count + 1
    index = index + 1

print(count)
