# 0, 1, 2
# 3, 4, 5
# 6, 7, 8

x = "X"
o = "O"
n = "N"


class Cell:
    def __init__(self):
        self.value = "N"
    def changeValue(self, value):
        self.value = value
    def getValue(self):
        return value

grid = [
    n, n, n,
    n, n, n,
    n, n, n
]

def displayGrid():
    verLine = " | "
    horLine = "_________"
    print(grid[0] + verLine + grid[1] + verLine + grid[2] )
    print(horLine)
    print(grid[3] + verLine + grid[4] + verLine + grid[5] )
    print(horLine)
    print(grid[6] + verLine + grid[7] + verLine + grid[8] )


def game():
    displayGrid()
    for i in range(5):
        xPlayer = int(input("Enter where you want to place an X: "))
        grid[xPlayer] = x
        displayGrid()
        checkScore()
        oPlayer = int(input("Enter where you want to place an O: "))
        grid[oPlayer] = o
        displayGrid()
        checkScore()

def checkScore():
    if grid[0] == x and grid[1] == x and grid[2] == x:
        print("X Wins!")
    if grid[0] == o and grid[1] == o and grid[2] == o:
        print("O Wins!")
    if grid[0] == x and grid[3] == x and grid[6] == x:
        print("X Wins!")
    if grid[0] == o and grid[3] == o and grid[6] == o:
        print("O Wins!")
    if grid[3] == x and grid[4] == x and grid[5] == x:
        print("X Wins!")
    if grid[3] == o and grid[4] == o and grid[5] == o:
        print("O Wins!")
    if grid[6] == x and grid[7] == x and grid[8] == x:
        print("X Wins!")
    if grid[6] == o and grid[7] == o and grid[8] == o:
        print("O Wins!")
    if grid[1] == x and grid[4] == x and grid[7] == x:
        print("X Wins!")
    if grid[1] == o and grid[4] == o and grid[7] == o:
        print("O Wins!")
    if grid[2] == x and grid[5] == x and grid[8] == x:
        print("X Wins!")
    if grid[2] == o and grid[5] == o and grid[8] == o:
        print("O Wins!")
    if grid[0] == x and grid[4] == x and grid[8] == x:
        print("X Wins!")
    if grid[0] == o and grid[4] == o and grid[8] == o:
        print("O Wins!")
    if grid[6] == x and grid[4] == x and grid[2] == x:
        print("X Wins!")
    if grid[6] == o and grid[4] == o and grid[2] == o:
        print("O Wins!")
    else:
        print("Draw!")

game()