class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n') if len(x) > 0]

    def _solve(self, iNums, target):
        nums = {}
        for i, x in enumerate(iNums):
            nums[x] = i

        for i, x in enumerate(iNums):
            if target - x in nums and nums[target-x] != i:
                return (target-x) * x
        return -1

    def solve(self):
        for i, x in enumerate(self.input):
            target = 2020 - x
            s = self._solve(self.input[i+1:], target)
            if s != -1:
                return x * s
            
        return -1


if __name__=='__main__':
    print(Solution("day1/p1/input.txt").solve())