import random

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        elif user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        elif user_guess > 2:
            break
        else:
            print(f'Your guess of {user_guess} is too high!')

guessing_game()

