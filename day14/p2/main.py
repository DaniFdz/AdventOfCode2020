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
        def getNums(value: str) -> set:
            total = set()
            if "X" in value:
                i = value.index("X")
                for x in getNums(value[:i]+"0"+value[i+1:]): total.add(x)
                for x in getNums(value[:i]+"1"+value[i+1:]): total.add(x)
            else:
                total.add(value)
            return total

        def applyMask(mask:str, value:str) -> str:
            val = ""
            for i in range(36):
                if mask[i] == "1":
                    val+="1"
                elif mask[i] == "0":
                    val+=value[i]
                else:
                    val+="X"
            return getNums(val)

        def intToBinary(n):
            val = str(bin(n))[2:] 
            while len(val) < 36:
                val = "0"+val
            return val

        s = {}
        for val in self.input:
            for x in applyMask(self.input[val]["mask"], intToBinary(val)):
                s[int(x,2)]=self.input[val]["value"]
                
        return sum(s.values())



if __name__=='__main__':
	print(Solution("day14/p2/input.txt").solve())
