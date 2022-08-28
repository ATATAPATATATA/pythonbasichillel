a = int(input('Enter any number for A: '))
b = int(input('Enter any number for B: '))
if a < b:
    for i in range(a, b + 1, 1):
        print(i, end=' ')
    else:
        for i in range(a, b - 1, - 1):
            print(i, end=' ')
# в консолі чомусь не виводить в порядку зменшення

# done
