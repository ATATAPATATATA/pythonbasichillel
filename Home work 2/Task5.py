# 5. У математиці функцію `sign(x)` (знак числа) визначено так:
#  sign(x) = 1, якщо x > 0,
#  sign(x) = -1, якщо x < 0,
#  sign(x) = 0 якщо x = 0.
#  Для цього числа x виведіть значення sign(x).
#  Це завдання бажано вирішити за допомогою каскадних інструкцій if... elif... else.

print('Please, enter sign(x) ', end='')
x = int(input())
if x > 1:
    print('sign (x) = 1')
elif x < -1:
    print('sign (x) = -1')
else:
    x = 0
    print('sign (x) = 0')

