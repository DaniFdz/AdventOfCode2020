class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n')[:-1]]

    def solve(self):
        total = {0:1}
        for line in sorted(self.input):
            total[line] = 0
            if line - 1 in total:
                total[line]+=total[line-1]
            if line - 2 in total:
                total[line]+=total[line-2]
            if line - 3 in total:
                total[line]+=total[line-3]

        # print(total)

        return total[max(self.input)]

        


if __name__=='__main__':
	print(Solution("day10/p2/input.txt").solve())
