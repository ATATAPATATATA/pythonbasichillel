numbers = input('Enter 5 numbers: ')
list_ten = []
for elem in numbers:
    list_ten.append(int(elem))
    list_ten.reverse()
print(list_ten)
