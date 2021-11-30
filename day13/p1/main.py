class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            t = f.read().split("\n")[:-1]
            self.estimate = int(t[0])
            self.input = {}
            for i, x in enumerate(t[1].split(",")):
                if x != 'x':
                    self.input[i] = int(x)


    def solve(self):
        n = self.estimate
        while 0 not in [n%x for x in self.input.values()]:
            n += 1

        return (n - self.estimate) * [x for x in self.input.values() if n%x == 0][0]

if __name__=='__main__':
	print(Solution("day13/p1/input.txt").solve())
