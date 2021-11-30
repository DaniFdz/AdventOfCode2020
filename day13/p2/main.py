class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            t = f.read().split("\n")
            self.input = {int(x): -i%int(x) for i,x in enumerate(t[1].split(",")) if x!='x'}

            self.input = dict(reversed(sorted(self.input.items())))
            print(self.input)

    def solve(self):
        n = list(self.input.values())[0]
        m = list(self.input.keys())[0]
        for i in list(self.input.keys())[1:]:
            while n % i != self.input[i]:
                n+=m
            m*=i
            
        return n

if __name__=='__main__':
	print(Solution("day13/p2/input.txt").solve())

