numbers = [1, 8, 3, 2, 6]
size = len(numbers)
current_index = 0
max_number_index = 0
max = numbers[0]

while current_index < size:
    if numbers[current_index] > max:
        max = numbers[current_index]
        max_number_index = current_index
    current_index = current_index + 1

current_index = 0
second_max = numbers[0]

if max_number_index == 0:
    second_max = numbers[1]
while current_index < size:
    if current_index != max_number_index:
        if numbers[current_index] > second_max:
            second_max = numbers[current_index]
    current_index = current_index + 1

print(second_max)
