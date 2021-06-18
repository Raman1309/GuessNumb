from random import randint

def computer_number(min_num,max_num):
    return randint(min_num,max_num)

def player_guess(min_num,max_num):
    user_input = int(input(f'Guess a number between {min_num} and {max_num}: '))
    return user_input

def play():
    low = 0
    high = 10

    computer_choice = computer_number(low,high)
    player_choice = player_guess(low,high)

    while player_choice != computer_choice:
        if player_choice>computer_choice:
            player_choice = int(input('Number is too high, try again: '))
        elif player_choice<computer_choice:
            player_choice = int(input('Number is too low, try again: '))

    print (f'Congratulation! You managed to guess the number {computer_choice}')

play()
