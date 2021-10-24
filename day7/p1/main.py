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
          
    def __getBags(self, target:str = 'shiny gold') -> list:
        total = set()
        for k, v in self.input.items():
            if target in [x[1] for x in v] and target not in total:
                total.add(k)
                sB = self.__getBags(k)
                for x in sB:
                    total.add(x)

                
        return total

    def solve(self):
        x = self.__getBags()
        return len(x)

                

       
        

if __name__=='__main__':
	print(Solution("day7/p1/input.txt").solve())