import random

game_count = 0
user_wins = 0

while True:
    user_input = input('Enter rock, paper, or scissors: ')
    while user_input not in ['rock', 'paper', 'scissors']:
        user_input = input('Invalid choice. Please enter rock, paper, or scissors: ')
    print(f'You entered: {user_input}')
    
    choices = ['rock', 'paper', 'scissors']
    random_choice = random.choice(choices)
    print(f'Random choice: {random_choice}')
    
    game_count += 1
    
    if user_input == random_choice:
        print('It\'s a tie!')
    elif (user_input == 'rock' and random_choice == 'scissors') or \
         (user_input == 'scissors' and random_choice == 'paper') or \
         (user_input == 'paper' and random_choice == 'rock'):
        print('You win!')
        user_wins += 1
    else:
        print('You lose!')
    
    # ゲームを続けるかをユーザに聞く
    while True:
        continue_game = input('Do you want to play again? (yes/no): ').strip().lower()
        if continue_game in ['yes', 'no']:
            break
        print('Invalid choice. Please enter yes or no.')
    if continue_game == 'no':
        print(f'Thanks for playing! You played {game_count} games and won {user_wins} times.')
        break
