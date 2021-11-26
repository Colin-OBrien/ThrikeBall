
player_1 = input('Who is Player 1? ')
player_2 = input('Who is Player 2? ')
player_3 = input('Who is Player 3? ')


def keep_score(player1, player2, player3):

    score = [0, 0, 0]
    game_on = True

    while game_on:

        scored = input('Who scored the point? ')

        if scored.lower() == player1.lower():
            score[0] += 2
            score[1] -= 1
            score[2] -= 1
        elif scored.lower() == player2.lower():
            score[0] -= 1
            score[1] += 2
            score[2] -= 1
        elif scored.lower() == player3.lower():
            score[0] -= 1
            score[1] -= 1
            score[2] += 2

        print(f'The score is {player1}:{score[0]}, {player2}:{score[1]}, {player3}:{score[2]}.')

        for x in score:
            if x == 10 or x == -10:
                game_on = False


keep_score(player_1, player_2, player_3)


#added this one the web