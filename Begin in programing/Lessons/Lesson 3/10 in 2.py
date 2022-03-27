dec = int(input())
bin = ''

while dec > 0:
    bin = str(dec % 2) + bin
    dec = dec // 2

print(int(bin))
