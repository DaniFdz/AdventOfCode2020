class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [int(x) for x in f.read().split('\n')[:-1]]

    def solve(self):
        l = [0]
        lookingFor = max(self.input)
        x = 0

        while x != lookingFor:
            for i in range(x+1, x+4):
                # print(x)
                if i in self.input:
                    l.append(i)
                    x = i
                    pass

        l.append(lookingFor+3)

        oneDiff = threeDiff = 0
        for i in range(len(l)-1):
            if l[i+1]-l[i] == 1:
                oneDiff+=1
            elif l[i+1]-l[i] == 3:
                threeDiff+=1
        # print(oneDiff, threeDiff)
        return oneDiff * threeDiff

if __name__=='__main__':
	print(Solution("day10/p1/input.txt").solve())