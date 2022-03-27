first_vector = [1, 8]
second_vector = [6, 3]
size = len(first_vector)
scalar_product = 0
index = 0

while index < size:
    scalar_product = scalar_product + first_vector[index] * second_vector[index]
    index = index + 1

print(scalar_product)
