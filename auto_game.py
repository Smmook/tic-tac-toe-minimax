import engine as ttt
import players as ai
from progress import print_progress_bar
import sys
import time

def play(player1, player2):
    board = ttt.new_board()
    players = ('X', 'O')
    engines = (player1, player2)
    turn = 0
    while True:
        player = players[turn % 2]
        engine = engines[turn % 2]
        move = ai.get_move(board, player, engine)
        board = ttt.make_move(board, move, player)
        if ttt.is_draw(board):
            return 0
        if ttt.is_win(board, player):
            return 1 if player == 'X' else 2
        turn += 1

def print_stats(wins, player1, player2, games):
    for i in range(3):
        wins[i] = "{0:.1f}".format(wins[i] / games * 100)
    print(f"{player1}: {wins[1]}%")
    print(f"{player2}: {wins[2]}%")
    print(f"Draws: {wins[0]}%")

def auto_play(player1, player2, games):
    wins = [0, 0, 0]
    for i in range(games):
        print_progress_bar(i, games, 50)
        wins[play(player1, player2)] += 1
    print("")
    print_stats(wins, player1, player2, games)
    
if __name__ == "__main__":
    if sys.argv.__len__() < 4:
        raise Exception("Uso: python game.py engine1 engine2 games")
    start = time.time()
    auto_play(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    seconds = time.time() - start
    print("Tiempo total: {:.1f}s".format(seconds))
    # auto_play("win_move", "minimax", 1000)