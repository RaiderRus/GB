numbers = [2, 5, 13, 7, 6, 4]
size = 6
sum = 0
avg = 0
index = 0

while index < size:
    sum = sum + numbers[index]
    index = index + 1
    avg = sum / size

print(int(avg))  # int к avg добавил для округления
