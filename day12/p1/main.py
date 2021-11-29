from dataclasses import dataclass
import numpy as np

@dataclass
class Move:
    direction: str
    value: int

class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [Move(x[0], int(x[1:])) for x in f.read().split("\n")[:-1]]

    def solve(self):
        x = y = 0
        direction = 90
        for move in self.input:
            if move.direction ==  "F":
                x += int(move.value * np.sin(direction*np.pi/180))
                y += int(move.value * np.cos(direction*np.pi/180))
            elif move.direction ==  "L":
                direction -= move.value
                direction %= 360
            elif move.direction ==  "R":
                direction += move.value
                direction %= 360
            elif move.direction ==  "N":
                y += move.value
            elif move.direction ==  "E":
                x += move.value
            elif move.direction ==  "S":
                y -= move.value
            elif move.direction ==  "W":
                x -= move.value

        return abs(x) + abs(y)

if __name__=='__main__':
	print(Solution("day12/p1/input.txt").solve())
