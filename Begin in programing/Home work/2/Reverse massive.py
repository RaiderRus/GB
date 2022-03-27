numbers = [1, 8, 3, 2, 6]
index = -1

print(len(numbers) // 2)

for i in range(len(numbers) // 2):
    numbers[index], numbers[i] = numbers[i], numbers[index]
    index = index - 1

print(numbers)
