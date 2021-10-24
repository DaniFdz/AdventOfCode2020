class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = f.read().split('\n')

    def solve(self):
        groups = []
        inp=''
        for x in self.input:
            if len(x) > 0:
                for char in x:
                    if char not in inp:
                        inp+=char
            else:
                groups.append(len(inp))
                inp=''
        return sum(groups)
            

if __name__=='__main__':
	print(Solution("day6/p1/input.txt").solve())