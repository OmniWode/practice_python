#08_rock_paper_scissors.py

game_over = False

print('Welcome to Rock-Paper-Scissors!')
print('For brevity, r=rock, p=paper, s=scissors')

def check_winner(p1, p2):
    winner = 0

    if p1 == 'r':
        if p2 == 's':
            winner = 1
        elif p2 == 'p':
            winner  = 2
        elif p2 == 'r':
            print('Draw!')
        else:
            print('Oops! Try one of (r, p, s)')
    elif p1 == 's':
        if p2 == 'p':
            winner = 1
        elif p2 == 'r':
            winner = 2
        elif p2 == 's':
            print('Draw!')
        else:
            print('Oops! Try one of (r, p, s)')
    elif p1 == 'p':
        if p2 == 'r':
            winner = 1
        elif p2 == 's':
            winner = 2
        elif p2 == 'p':
            print('Draw!')
        else:
            print('Oops! Try one of (r, p, s)')
    else:
        print('Oops! Try one of (r, p, s)')

    return winner


while (game_over != True):
    p1 = input('Player 1 move (r, p, s): ')
    p2 = input('Player 2 move (r, p, s): ')

    winner = check_winner(p1, p2)

    if winner == 0:
        print('Try again!')
    else:
        print('Winner: Player ',winner)
        replay = input('Would you like to play another round? (y/n) ')

        if replay == 'y':
            print('A challender approaches! Prepapre for another round')
        else:
            game_over = True


