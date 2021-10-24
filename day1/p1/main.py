class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n') if len(x) > 0]

    def solve(self):
        target = 2020
        self.nums = {}
        for i, x in enumerate(self.input):
            self.nums[x] = i

        for i, x in enumerate(self.input):
            if target - x in self.nums and self.nums[target-x] != i:
                return (target-x) * x
        return -1

if __name__=='__main__':
    print(Solution("day1/p1/input.txt").solve())