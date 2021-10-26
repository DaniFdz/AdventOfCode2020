class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n')[:-1]]

    def solve(self):
        total = {0:1}
        for line in sorted(self.input):
            total[line] = 0
            for i in range(1, 4):
                if line - i in total:
                    total[line]+=total[line-i]

        # print(total)

        return total[max(self.input)]

        


if __name__=='__main__':
	print(Solution("day10/p2/input.txt").solve())
