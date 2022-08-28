x = int(input('Enter ran km at first day: '))
y = int(input('Enter km from last day: '))
d = 1
while x <= y:
    x = x + (x * 0.1)
    d += 1
print(d)

#done