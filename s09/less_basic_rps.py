from random import choice

print('...rock...')
print('...paper...')
print('...scissors...')

player = input('(Enter your choice): ').lower()
computer_choice = choice(['rock', 'paper', 'scissors'])
print(f'The computer plays: {computer_choice}')

if player == computer_choice:
    print('Draw!')
elif player == 'rock':
    if computer_choice == 'scissors':
        print('Player wins!')
    else:
        print('Computer wins!')
elif player == 'paper':
    if computer_choice == 'rock':
        print('Player wins!')
    else:
        print('Computer wins!')
elif player == 'scissors':
    if computer_choice == 'rock':
        print('Computer wins!')
    else:
        print('Player wins!')
else:
    print('Please enter valid choice!')
