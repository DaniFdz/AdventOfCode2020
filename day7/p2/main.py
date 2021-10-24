class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            t = f.read().split('\n')
            self.input = dict()
            for row in t[:-1]:
                x = row.split(' bags contain ')
                if x[1] == 'no other bags.':
                    self.input[x[0]] = []
                else:
                    bags = [[int(y[0]), y[2:]] for y in x[1].replace('bags', 'bag')[:-5]. split(' bag, ')]
                    self.input[x[0]] = bags
          
    def solve(self, target:str = 'shiny gold') -> int:
        if len(self.input[target]) >= 1:
            n = 0
            for x in self.input[target]:
                n += x[0] + x[0]*self.solve(x[1])
            return n
        else:
            return 0
        

if __name__=='__main__':
	print(Solution("day7/p2/input.txt").solve())