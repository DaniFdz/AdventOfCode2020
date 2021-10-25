class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n')[:-1]]

    def notValid(self, n:int = 25) -> int:
        for i in range(n, len(self.input)):
            _in = False
            for j in range(i-n, i):
                if self.input[i]-self.input[j] in self.input[j+1:i]:
                    _in = True
                    
            if not _in: return i
        return -1
    
    def getSequence(self, x:int) -> list:
        for i in range(x):
            for j in range(x, i, -1):
                if sum(self.input[i:j]) == self.input[x]:
                    return self.input[i:j]



    def solve(self, n:int = 25):
        i = self.notValid(n)

        s = self.getSequence(i)
        return max(s) + min(s)

if __name__=='__main__':
	print(Solution("day9/p2/input.txt").solve())