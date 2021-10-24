class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[x[:7], x[7:]] for x in f.read().split("\n")]

    def solve(self):
        n = 0
        for row, column in self.input:
            f,b = 0, 127
            l,r = 0, 7
            for char in row:
                if char == 'F':
                    b -= (b-f+1)//2
                else:
                    f += (b-f+1)//2
            for char in column:
                if char == 'L':
                    r-= (r-l+1)//2
                else:
                    l+= (r-l+1)//2

            sID = f*8+l
            n = max(n, sID)

        return n

if __name__=='__main__':
	print(Solution("day5/p1/input.txt").solve())