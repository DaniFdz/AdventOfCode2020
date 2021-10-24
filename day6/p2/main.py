class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = f.read().split('\n')

    def solve(self):
        groups = list()
        inp= set('abcdefghijklmnopqrstuvwxyz')
        for x in self.input:
            if len(x) > 0:
                inp = inp.intersection(set(x))
            else:
                groups.append(len(inp))
                inp= set('abcdefghijklmnopqrstuvwxyz')
            
        groups.append(len(inp))
        return sum(groups)
            

if __name__=='__main__':
	print(Solution("day6/p2/input.txt").solve())