pole = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def print_pole(list):
    for item in list:
        print(*item)


def find_win(list):
    win_list = [[list[0][0], list[0][1], list[0][2]],
                [list[1][0], list[1][1], list[1][2]], 
                [list[2][0], list[2][1], list[2][2]],
                [list[0][0], list[1][0], list[2][0]],
                [list[0][1], list[1][1], list[2][1]],
                [list[0][2], list[1][2], list[2][2]],
                [list[0][0], list[1][1], list[2][2]],
                [list[0][2], list[1][1], list[2][0]]]
    for i in range(len(win_list)):
        if win_list[i][0] == win_list[i][1] == win_list[i][2] != "-":
            return win_list[i][0]



print_pole(pole)
print(find_win(pole))
