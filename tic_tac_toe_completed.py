board = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

def display_board(board):
    print("     |     |     ")
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ")
    print("     |     |     ")

def move(player, move):
    if move < 1 or move > 9:
        return False

    row = (move - 1) // 3
    col = (move - 1) % 3

    if board[row][col] != move:
        return False

    board[row][col] = player
    return True

def evaluate_board(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    for row in board:
        for cell in row:
            if isinstance(cell, int):
                return -1
    
    return 0

player_1 = "X"
player_2 = "O"

display_board(board)

while True:
    print(f"Igrač {player_1} je na potezu!")

    player_move = int(input(f"Odigraj potez igrača {player_1} od 1 do 9: "))
    
    while not move(player_1, player_move):
        print("Neispravan potez! Molimo pokušajte ponovno.")
        player_move = int(input(f"Odigraj potez igrača {player_1} od 1 do 9: "))

    display_board(board)

    board_state = evaluate_board(board)

    if board_state == "X":
        print(f"Igrač X je pobjednik!")
        break
    elif board_state == "O":
        print(f"Igrač O je pobjednik!")
        break
    elif board_state == -1:
        print("Igra je neriješena!")
        break

    print(f"Igrač {player_2} je na potezu!")

    player_move = int(input(f"Odigraj potez igrača {player_2} od 1 do 9: "))
    
    while not move(player_2, player_move):
        print("Neispravan potez! Molimo pokušajte ponovno.")
        player_move = int(input(f"Odigraj potez igrača {player_2} od 1 do 9: "))

    display_board(board)

print("Kraj igre!")
