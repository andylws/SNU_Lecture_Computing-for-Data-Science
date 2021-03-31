"""
**Instruction**
<Rock, scissors, paper>
Input of P1 function is a list of games of Rock/Scissors/Paper of 3 players
Each element of the input list is a list 
for which 1st element is player 1's choice, 2nd element is player 2's choice and 3rd element is player 3's choice.
Each player's choice is one of 'R','S' and 'P'(R stands for rock, S for scissors, P for paper)
Example of input list is as following:
[['R','S','S'], ['R','R','P'], ['S','P','R']]

Complete P1 function that returns the number of of player 1's wins 
- Assume 'R' wins 'S', 'S' wins 'P', 'P' wins 'R'.
- If there are more than 1 winners and player 1 is one of the winners, it is counted as win. For example, ['P','R','P'] is win
- If the choice of players are all different, it is "Draw". For example, ['S','P','R'] is "Draw"
- If the choice of players are all same, it is also "Draw"

>>> P1([['R','S','S'], ['R','R','P'], ['S','P','R']]) # It is win-lose-draw
1

>>> P1([['R', 'S', 'P'],['R', 'R', 'S'],['S', 'P', 'P']]) # It is draw-win-win
2

>>> P1([['S', 'P', 'R'],['P', 'P', 'P'],['P', 'R', 'R'],['R', 'R', 'S'],['R', 'S', 'R']]) # It is draw-draw-win-win-win
3

"""


def P1(game: list) -> int:
    ##### Write your Code Here #####

    wins1 = 0

    for current_game in game:
        if current_game[0] == 'R':
            if current_game == ['R', 'R', 'R'] or 'P' in current_game:
                continue
            else:
                wins1 = wins1 + 1
        elif current_game[0] == 'S':
            if current_game == ['S', 'S', 'S'] or 'R' in current_game:
                continue
            else:
                wins1 = wins1 + 1
        elif current_game[0] == 'P':
            if current_game == ['P', 'P', 'P'] or 'S' in current_game:
                continue
            else:
                wins1 = wins1 + 1
        else:
            return "ERROR"

    return wins1
    ##### End of your code #####
