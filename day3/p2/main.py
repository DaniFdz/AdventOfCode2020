class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[0 if x == '.' else 1 for x in row] for row in f.read().split('\n')[:-1]]

    def __solve(self, xMove, yMove) -> int:
        x = y = 0
        nTrees = 0
        while y < len(self.input):
            nTrees += self.input[y][x] 
            x = (x+xMove) % len(self.input[y])
            y += yMove

        return nTrees

    def solve(self) -> int:
        trees = 1
        for moves in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
            trees *= self.__solve(*moves)
        return trees


if __name__=='__main__':
	print(Solution("day3/p2/input.txt").solve())