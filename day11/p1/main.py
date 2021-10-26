class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[y for y in x] for x in f.read().split("\n")[:-1]]

    

    def __nextState(self) -> list:
        def countNeightbours(board, x, y) -> int:
            neightbours = 0
            for x_, y_ in [
                [x-1, y-1], [x, y-1], [x+1, y-1],
                [x-1,   y],           [x+1,   y],
                [x-1, y+1], [x, y+1], [x+1, y+1]
            ]:
                try:
                    neightbours+= 1 if board[y_][x_] == "#" else 0
                except IndexError:
                    pass

            return neightbours

        board = [["" for _ in x] for x in self.input]

        for y in range(len(board)):
            for x in range(len(board[y])):
                cN = countNeightbours(self.input, x, y)

                if self.input[y][x] == "#" and cN >= 4:
                    board[y][x] = "L"

                elif self.input[y][x] == "L" and cN == 0:
                    board[y][x] = "#"

                else: board[y][x] = self.input[y][x]
                
    
        return board

    def solve(self) -> int:
        x = self.__nextState()
        while x != self.input:
            # print(*self.input, sep = '\n', end='\n\n')
            self.input = x
            x = self.__nextState()
        print(*self.input, sep = '\n', end='\n\n')
            
        tot = 0
        for row in self.input:
            tot+=row.count("#")

        return tot

        

            
        

if __name__=='__main__':
	print(Solution("day11/p1/input.txt").solve())