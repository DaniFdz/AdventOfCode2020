class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[int(x) if x[0] in '+-' else x for x in y.split(' ')] for y in f.read().split('\n')[:-1]]

    def solve(self):
        acc = i = 0
        visited = []
        while i < len(self.input) and i not in visited:
            visited.append(i)
            if self.input[i][0] == 'acc':
                acc+=self.input[i][1]
                i+=1
            elif self.input[i][0] == 'jmp':
                i+=self.input[i][1]
            else:
                i+=1

        return acc

if __name__=='__main__':
	print(Solution("day8/p1/input.txt").solve())