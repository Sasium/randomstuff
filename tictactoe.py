# write your code here
print("---------")
print("|       |")
print("|       |")
print("|       |")
print("---------")
rows = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
turn = 0
while True:
    turn += 1
    while True:
        cells_choose = input("Enter the coordinates: ").split()
        cells_numeric = [x for x in cells_choose if x.isdigit()]
        cells_numeric_needed = [x for x in cells_numeric if 1 <= int(x) <= 3]
        column_choose = abs(int(cells_numeric[1]) - 3)
        row_choose = int(cells_numeric[0]) - 1
        if len(cells_numeric) < 2:
            print("You should enter numbers!")
        elif len(cells_numeric_needed) < 2:
            print("Coordinates should be from 1 to 3!")
        elif rows[column_choose][row_choose] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if turn % 2:
                rows[column_choose][row_choose] = "X"
            else:
                rows[column_choose][row_choose] = "O"
            print("---------")
            print("| " + rows[0][0] + " " + rows[0][1]
                  + " " + rows[0][2] + " |")
            print("| " + rows[1][0] + " " + rows[1][1]
                  + " " + rows[1][2] + " |")
            print("| " + rows[2][0] + " " + rows[2][1]
                  + " " + rows[2][2] + " |")
            print("---------")
            break
    columns = [[x[0] for x in rows],
               [x[1] for x in rows],
               [x[2] for x in rows]]
    diagonals = [[rows[0][0], rows[1][1], rows[2][2]],
                 [rows[0][2], rows[1][1], rows[2][0]]]
    x_wins = 0
    o_wins = 0
    for i in range(3):
        if rows[i] == ["X", "X", "X"]:
            x_wins = 1
        elif rows[i] == ["O", "O", "O"]:
            o_wins = 1
        if columns[i] == ["X", "X", "X"]:
            x_wins = 1
        elif columns[i] == ["O", "O", "O"]:
            o_wins = 1
    for i in range(2):
        if diagonals[i] == ["X", "X", "X"]:
            x_wins = 1
        if diagonals[i] == ["O", "O", "O"]:
            o_wins = 1
    if x_wins == 1:
        print("X wins")
        break
    elif o_wins == 1:
        print("O wins")
        break
    elif not any([' ' in x for x in rows]):
        print("Draw")
        break
