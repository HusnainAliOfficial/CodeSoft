import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return -1
    if is_winner(board, "O"):
        return 1
    if is_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            score = minimax(board, depth + 1, False)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            score = minimax(board, depth + 1, True)
            board[row][col] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    best_move = None
    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        user_row = int(input("Enter the row (0, 1, 2): "))
        user_col = int(input("Enter the column (0, 1, 2): "))
        
        if board[user_row][user_col] != " ":
            print("Invalid move. Cell already occupied.")
            continue

        board[user_row][user_col] = "X"
        print_board(board)

        if is_winner(board, "X"):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI's move:")
        print_board(board)

        if is_winner(board, "O"):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
