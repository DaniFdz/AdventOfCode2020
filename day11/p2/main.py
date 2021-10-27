class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[y for y in x] for x in f.read().split("\n")[:-1]]

    def __nextState(self) -> list:
        def countNeightbours(board, x, y) -> int:
            neightbours = 0
            for direction in [
                [-1, -1], [0, -1], [1, -1],
                [-1,  0],          [1,  0],
                [-1,  1], [0,  1], [1,  1]
            ]:
                i = 1
                while i < max(len(board[0]), len(board)):
                    x_ = x + direction[0]*i
                    y_ = y + direction[1]*i

                    if not(0 <= x_ < len(board[0]) and \
                        0 <= y_ < len(board)):
                        break
                    if board[y_][x_] in "#L":
                        neightbours += 1 if board[y_][x_] == "#" else 0
                        break
                    i+=1


            return neightbours


        board = [["" for _ in x] for x in self.input]

        for y in range(len(board)):
            for x in range(len(board[y])):
                cN = countNeightbours(self.input, x, y)

                if self.input[y][x] == "#" and cN >= 5:
                    board[y][x] = "L"

                elif self.input[y][x] == "L" and cN == 0:
                    board[y][x] = "#"

                else: board[y][x] = self.input[y][x]
                
        return board

    def solve(self) -> int:
        def pS(b):
            for row in b:
                for col in row:
                    print(col, end="")
                print()
            print()

        x = self.__nextState()
        while x != self.input:
            # pS(self.input)
            self.input = x
            x = self.__nextState()
        # pS(self.input)
            
        tot = 0
        for row in self.input:
            tot+=row.count("#")

        return tot

if __name__=='__main__':
	print(Solution("day11/p2/input.txt").solve())