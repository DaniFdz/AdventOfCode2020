from dataclasses import dataclass

@dataclass
class Passport:
    byr: str # (Birth Year)
    iyr: str # (Issue Year)
    eyr: str # (Expiration Year)
    hgt: str # (Height)
    hcl: str # (Hair Color)
    ecl: str # (Eye Color)
    pid: str # (Passport ID)

    def isValid(self) -> bool:
        valid = []

        valid.append(bool(1920 <= int(self.byr) <= 2020))
        valid.append(bool(2010 <= int(self.iyr) <= 2020))
        valid.append(bool(2020 <= int(self.eyr) <= 2030))

        if self.hgt[-2:] == 'cm':
            valid.append(bool(150 <= int(self.hgt[:-2]) <= 193))
        elif self.hgt[-2:] == 'in':
            valid.append(bool(59 <= int(self.hgt[:-2]) <= 76))
        else:
            valid.append(False)

        if self.hcl[0]=='#':
            for char in self.hcl[1:]:
                if not char in '0123456789abcdef':
                    valid.append(False)
                    break
            valid.append(True)
        else:
            valid.append(False)

        valid.append(self.ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))

        valid.append(len(self.pid) == 9 and self.pid.isnumeric())
        
        return all(valid)

class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = f.read().split('\n')

    def solve(self):
        valid = 0
        values = [None]*7
                    
        fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid") 

        for row in self.input:
            if len(row)==0:
                if None not in values:
                    if Passport(*values).isValid():
                        valid += 1
                values = [None]*7
            else:
                for field in row.split(' '):
                    if field[:3] in fields:
                        i = fields.index(field[:3])
                        values[i] = field[4:]
                    
        return valid

        

if __name__=='__main__':
	print(Solution("day4/p2/input.txt").solve())