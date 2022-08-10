x1 = int(input('1 number: '))
y1 = int(input('2 number: '))
x2 = int(input('3 number: '))
y2 = int(input('4 number: '))
if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print('YES')
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print('YES')
else:
    print('NO')
