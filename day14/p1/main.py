class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, "r") as f:
            self.input = {}
            mask = ""
            for line in f.read().split("\n")[:-1]:
                op, num = line.split(" = ")
                if op == "mask": 
                    mask = num
                else:
                    direction = int(op[4:-1])
                    self.input[direction] = {"mask":mask, "value": int(num)}

    def solve(self):
        def applyMask(mask:str, value:str) -> str:
            val = ""
            for i in range(36):
                if mask[i] == "X":
                    val+=value[i]
                else:
                    val+=mask[i]
            return val

        def intToBinary(n):
            val = str(bin(n))[2:] 
            while len(val) < 36:
                val = "0"+val
            return val
            
        sum = 0
        for val in self.input:
            sum += int(applyMask(self.input[val]["mask"], intToBinary(self.input[val]["value"])), 2)

        return sum

if __name__=='__main__':
	print(Solution("day14/p1/input.txt").solve())
