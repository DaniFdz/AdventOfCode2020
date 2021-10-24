class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n')[:-1]]

    def solve(self, n:int = 25):
        for i in range(n, len(self.input)):
            _in = False
            for j, y in enumerate(self.input[i-n:i]):
                if self.input[i]-y in self.input[j+1:i]:
                    _in = True
                    
            if not _in: return self.input[i]
        return -1

if __name__=='__main__':
	print(Solution("day9/p1/input.txt").solve(5))