from random import choice

moves = ['rock', 'paper', 'scissors']
game_info = {
    'wins': 0,
    'draws': 0,
    'losses': 0,
    'total games': 0
}
player_moves = []

while True:
    # Pick computer_move
    if game_info['total games'] == 0:
        computer_move = 'paper'
    else:
        # computer_move = choice(moves) # pick random
        rock_count = player_moves.count('rock')
        paper_count = player_moves.count('paper')
        scissors_count = player_moves.count('scissors')
        print(f'rocks: {rock_count} papers: {paper_count} scissors: {scissors_count}')
        max_count = max(rock_count, paper_count, scissors_count)
        if scissors_count == max_count:
            computer_move == 'rock'
        elif paper_count == max_count:
            computer_move == 'scissors'
        else:
            computer_move == 'paper'
        
    # Get play move
    player_move = str(input('Enter move (rock, paper, or scissors): '))
    while player_move not in moves:
        print('Sorry. "' + player_move + '" is not a valid move.')
        player_move = str(input('Please enter a move (rock, paper, or scissors): '))
    assert player_move in moves, f'{player_move} is not in {moves}'
    player_moves.append(player_move)    
        
    print('Computer chose ' + computer_move)
    game_info['total games'] += 1
    if player_move == 'rock':
        if computer_move == 'rock':
            game_info['draws'] += 1
            print('Draw!')
        elif computer_move == 'paper':
            game_info['wins'] += 1
            print('Computer Wins!')
        elif computer_move == 'scissors':
            game_info['losses'] += 1
            print('You Win!')
    elif player_move == 'paper':
        if computer_move == 'rock':
            game_info['losses'] += 1
            print('You Win!')
        elif computer_move == 'paper':
            game_info['draws'] += 1
            print('Draw!')
        elif computer_move == 'scissors':
            game_info['wins'] += 1
            print('Computer Wins!')
    elif player_move == 'scissors':
        if computer_move == 'rock':
            game_info['wins'] += 1
            print('Computer Wins!')
        elif computer_move == 'paper':
            game_info['losses'] += 1
            print('You Win!')
        elif computer_move == 'scissors':
            game_info['draws'] += 1
            print('Draw!')
            
    print(game_info)
    print(f'Computer win rate {game_info["wins"]/game_info["total games"]:.1%}')
    print(f'Player moves: {player_moves}')
