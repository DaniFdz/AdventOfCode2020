class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [[int(x) if x[0] in '+-' else x for x in y.split(' ')] for y in f.read().split('\n')[:-1]]
            for index, inst in enumerate(self.input):
                if inst[0] == 'jmp':
                    self.input[index][0] = 'nop'
                    if self.__check():
                        break
                    self.input[index][0] = 'jmp'
                elif inst[0] == 'nop':
                    self.input[index][0] = 'jmp'
                    if self.__check():
                        break
                    self.input[index][0] = 'nop'



    def __check(self) -> bool:
        i = 0
        visited = []
        while i < len(self.input):
            visited.append(i)
            if self.input[i][0] == 'jmp':
                i+=self.input[i][1]
                if i in visited: return False
            else:
                i+=1
                if i in visited: return False
        return True


    def solve(self) -> int:
        acc = i = 0
        while i < len(self.input):
            if self.input[i][0] == 'acc':
                acc+=self.input[i][1]
                i+=1
            elif self.input[i][0] == 'jmp':
                i+=self.input[i][1]
            else:
                i+=1

        return acc
        

if __name__=='__main__':
	print(Solution("day8/p2/input.txt").solve())