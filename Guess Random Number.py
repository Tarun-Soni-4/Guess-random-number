from random import randint
def computer_number(min_num,max_num):
    return randint(min_num,max_num)

def player_guess(min_num,max_num):
    user_input = int(input(f'\nGuess a number between {min_num} and {max_num}: '))
    return user_input

def play():
    count = 0
    low = int(input("Please enter lower range to guess a number : "))
    high = int(input("Please enter upper range to guess a number : "))
    computer_choice = computer_number(low,high)
    player_choice = player_guess(low,high)
    while player_choice != computer_choice:
        count += 1
        if player_choice>computer_choice:
            player_choice = int(input(f'Number is too high, guess a lower number than {player_choice}! Please try again: '))
        elif player_choice<computer_choice:
            player_choice = int(input(f'Number is too low, guess a higher number than {player_choice}! Please try again: '))
            
    print(f'\nCongratulations! You managed to guess the number {computer_choice} after {count} chances')
play()
