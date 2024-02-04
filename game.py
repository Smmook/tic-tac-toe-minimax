import players
import engine as ttt
import sys

def game(player1: str, player2: str) -> None:
    board = ttt.new_board()
    fichas = ('X', 'O')
    engines = (player1, player2)
    turn = 0
    winner = None
    while True:
        ttt.render(board)
        player = fichas[turn % 2]
        engine = engines[turn % 2]
        move = players.get_move(board, player, engine)
        board = ttt.make_move(board, move, player)
        if ttt.is_win(board, player):
            winner = player
            break
        if ttt.is_draw(board):
            print("Tablas!")
            ttt.render(board)
            return
        turn += 1
    ttt.render(board)
    print(f"Player {winner} as {engine} wins!")
    
if __name__ == "__main__":
    if sys.argv.__len__() < 3:
        raise Exception("Uso: python game.py engine1 engine2")
    game(sys.argv[1], sys.argv[2])