numbers = [1, 8, 3, 2, 6]
size = len(numbers)
index = 0
max = numbers[0]
min = numbers[0]
maxindex = 0
minindex = 0

while index < size:
    if numbers[index] > max:
        max = numbers[index]
        maxindex = index
    if numbers[index] < min:
        min = numbers[index]
        minindex = index
    index = index + 1

print(max, maxindex, sep=',')
print(min, minindex, sep=',')

