class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n')[:-1]]

    def solve(self):
        mem = {0:1}
        for line in sorted(self.input):
            mem[line] = 0
            for i in range(1, 4):
                if line - i in mem:
                    mem[line]+=mem[line-i]

        # print(mem)

        return mem[max(self.input)]

        


if __name__=='__main__':
	print(Solution("day10/p2/input.txt").solve())
