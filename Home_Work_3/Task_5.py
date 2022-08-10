from random import randint

x = randint(1, 10)
attempt = 0
print('I guessed a number from 1 to 10')
for i in range(1, 4):
    user_num = int(input('Enter digit from 1 to 10: '))
    if user_num > x:
        print('My number is less than you entered. Try again (:')
    elif user_num < x:
        print('My number is more than you entered. Try again (:')
    else:
        user_num = x
        print(f'You got it from {i}')
        break
    attempt += 1
    print(f'You have {3 - attempt} try')
if attempt >= 3:
    print('You lose!\nYou have exhausted all attempts')
