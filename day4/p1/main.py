class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = f.read().split('\n')


    def solve(self):
        valid = 0
        passport = [False]*7
        fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid") 
        for row in self.input:
            if len(row)==0:
                if all(passport):
                    valid+=1
                passport = [False]*7
            else:
                for i, f in enumerate(fields):
                    if f in row:
                        passport[i] = True

        return valid
                    

if __name__=='__main__':
	print(Solution("day4/p1/input.txt").solve())