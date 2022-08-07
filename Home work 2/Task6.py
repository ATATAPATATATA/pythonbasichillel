# Програма отримує на вхід число х.
#  Даний список із 10 елементів [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].
#  Написати програму яка поверне:
#  Чи є x серед елементів.
#  Число на введення може бути як цілим числом, числом з точкою, що плаває, так і від'ємним,
#  тобто. x = -10.00 має повернути що x є у списку.
#  ** В ідеалі список повинен бути записаний як кортеж один раз.

listy = (list(range(10, 101, 10)))
print(listy)
print('Please, enter your number: ', end='')
x = float(input())
if x in listy:
    print(x, ' is available in list')
elif -x in listy:
    print(x, ' is available in list')
elif x not in listy:
    print('Is not available in list')

