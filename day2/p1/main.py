from dataclasses import dataclass

@dataclass
class Password:
    lower: int
    higher: int
    letter: str
    passw: str

    def isValid(self) -> bool:
        return self.lower <= self.passw.count(self.letter) <= self.higher


class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = f.read().split('\n')

    def solve(self) -> int:
        sol = 0
        for x in self.input[:-1]:
            s_e, letter, string = x.split(' ')
            start, end = [int(a) for a in s_e.split('-')]
            letter = letter[:-1]
            if Password(start, end, letter, string).isValid():
                sol += 1
        return sol


if __name__=='__main__':
    print(Solution("day2/p1/input.txt").solve())