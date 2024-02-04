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

cache = {}
def minimax_ai(board: list[list[str]], player: str) -> tuple[int,int]:
    best_move = None
    max_score = -9999
    
    for move in ttt.get_legal_moves(board):
        state = ttt.make_move(board, move, player)
        score = minimax_score(state, ttt.get_opponent(player), False)
        if score > max_score:
            best_move = move
            max_score = score
    return best_move

def minimax_score(board: list[list[str]], player: str, maximizing: bool) -> int:
    cache_key = str(board)
    if cache_key in cache:
        return cache[cache_key]
    
    if ttt.is_win(board, player):
        eval = 10 if maximizing else -10
        cache[cache_key] = eval
        return eval
    if ttt.is_draw(board):
        cache[cache_key] = 0
        return 0
    
    if maximizing:
        max_eval = -9999
        for move in ttt.get_legal_moves(board):
            state = ttt.make_move(board, move, player)
            eval = minimax_score(state, ttt.get_opponent(player), False)
            max_eval = max(max_eval, eval)
        cache[cache_key] = max_eval
        return max_eval
    else:
        min_eval = 9999
        for move in ttt.get_legal_moves(board):
            state = ttt.make_move(board, move, player)
            eval = minimax_score(state, ttt.get_opponent(player), True)
            min_eval = min(min_eval, eval)
        cache[cache_key] = min_eval
        return min_eval