def tic_tac_toe(field):

    field = [line.split() for line in data.split('\n')]
    lines = field + [list(col) for col in zip(*field)] + [[field[i][i] for i in range(3)],
                                                          [field[i][2 - i] for i in range(3)]]

    if ['x'] * 3 in lines:
        return "x win"
    if ['0'] * 3 in lines:
        return "0 win"

    return "draw"


data = """x . 0
x x 0
. . 0"""

if __name__ == "__main__":
    print(tic_tac_toe(data))
