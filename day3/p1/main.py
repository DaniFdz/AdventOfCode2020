class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[0 if x == '.' else 1 for x in row] for row in f.read().split('\n')[:-1]]

    def solve(self):
        x = 0
        nTrees = 0
        for y in range(len(self.input)):
            nTrees += self.input[y][x] 
            x = (x+3) % len(self.input[y])

        return nTrees
            

if __name__=='__main__':
	print(Solution("day3/p1/input.txt").solve())