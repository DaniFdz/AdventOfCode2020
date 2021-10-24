class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[x[:7], x[7:]] for x in f.read().split("\n")]

    def solve(self):
        ids = []
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
            ids.append(sID)

        notInIds = [i for i in range(max(ids)) if i not in ids]
        for i in notInIds:
            if i+1 not in notInIds and i-1 not in notInIds:
                return i

        return -1


if __name__=='__main__':
	print(Solution("day5/p2/input.txt").solve())