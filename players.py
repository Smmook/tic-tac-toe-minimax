import engine as ttt
import random

def human_player(board: list[list[str]], player: str) -> tuple[int,int]:
    row = input("Fila: ")
    col = input("Columna: ")
    return (int(row), int(col))

def random_ai(board: list[list[str]], player: str) -> tuple[int,int]:
    moves = ttt.get_legal_moves(board)
    return random.choice(moves)

def winning_move_ai(board: list[list[str]], player: str) -> tuple[int,int]:
    moves = ttt.get_legal_moves(board)
    for move in moves:
        state = ttt.make_move(board, move, player)
        if ttt.is_win(state, player):
            return move
    return random.choice(moves)

def get_move(board: list[list[str]], player: str, engine: str) -> tuple[int,int]:
    players = {
        "human": human_player,
        "random": random_ai,
        "win_move": winning_move_ai,
        "minimax": minimax_ai
    }
    return players[engine](board, player)

def minimax_ai(board: list[list[str]], player: str) -> tuple[int,int]:
    max_eval = -9999
    best_move = None
    for move in ttt.get_legal_moves(board):
        state = ttt.make_move(board, move, player)
        eval = minimax(state, ttt.get_opponent(player), False, alpha=-9999, beta=9999)
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

def minimax(board: list[list[str]], player: str, maximizing: bool, alpha: int, beta: int) -> int:
    
    if ttt.is_draw(board):
        return 0
    if ttt.is_win(board, player):
        return 10 if maximizing else -10
    
    max_eval = -9999
    min_eval = 9999
    for move in ttt.get_legal_moves(board):
        state = ttt.make_move(board, move, player)
        eval = minimax(state, ttt.get_opponent(player), not maximizing, alpha, beta)
        if eval > max_eval:
            max_eval = eval
        if eval < min_eval:
            min_eval = eval
            
        if maximizing:
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
        else:
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        
    result = max_eval if maximizing else min_eval
    return result
    