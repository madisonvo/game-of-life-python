import random

def main():
    width = input("Enter board width: ")
    height = input("Enter board height: ")
    # TODO: invalid widths and heights
    # TODO: implement input board from file
    raw_board = random_board(int(width), int(height))
    print(raw_board)
    render(raw_board, width)
    next_board(raw_board)

def random_board(width, height):
    board = [[0] * width for _ in range(height)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = random.randint(0, 1)

    return board

def render(board, width):
    purple = rgb(106, 90, 205)
    reset = "\033[0m"

    print("-" * (int(width) + 2))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 0:
                print("|", end='')
            if j == int(width) - 1:
                print(f"{purple}#{reset}|" if board[i][j] == 1 else " |")
            else:
                print(f"{purple}#{reset}" if board[i][j] == 1 else " ", end='')
    print("-" * (int(width) + 2))

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def next_board(board):
    pass

def is_alive():
    pass

def is_dead():
    pass

main()
