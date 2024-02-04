import copy
from typing import Generator

def new_board() -> list[list[str]]:
    board = [[None for _ in range(3)] for _ in range(3)]
    return board

def render(board: list[list[str]]) -> None:
    print("  0 1 2")
    print("  ------")
    for i, row in enumerate(board):
        row = [e if e is not None else " " for e in row]    
        print(f"{i}|{' '.join(row)}|")
    print("  ------")
    
def get_opponent(player: str) -> str:
    return "X" if player == "O" else "O"
    
def make_move(board: list[list[str]], move: (int, int), player: str) -> list[list[str]]:
    x, y = move
    if board[x][y] is not None:
        raise Exception(f"Square {x},{y} not empty")
    new_state = copy.deepcopy(board)
    new_state[x][y] = player
    return new_state

def win_indexes() -> Generator[tuple[int, int], None, None]:
    # Filas
    for r in range(3):
        yield [(r, c) for c in range(3)]
    
    # Columnas
    for c in range(3):
        yield [(r, c) for r in range(3)]
    
    # Diagonal izq-arr a der-abaj
    yield [(i, i) for i in range(3)]
    
    # Otra diagonal
    yield [(i, 2 - i) for i in range(3)]

def is_win(board: list[list[str]], player: str) -> bool:
    for line in win_indexes():
        if all(board[x][y] == player for x, y in line):
            return True
    return False

def is_draw(board: list[list[str]]) -> bool:
    return len(get_legal_moves(board)) == 0

def get_legal_moves(board: list[list[str]]) -> list[tuple[int,int]]:
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                moves.append((row, col))
    return moves

