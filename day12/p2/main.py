from dataclasses import dataclass
import math

@dataclass
class Move:
    direction: str
    value: int

class Solution:
    def __init__(self, file:str="input.txt"):
        with open(file, 'r') as f:
            self.input = [Move(x[0], int(x[1:])) for x in f.read().split("\n")[:-1]]

    def solve(self):
        def rotate(direction, degrees):
            newDir = direction.copy()
            senTheta = math.sin(degrees)
            cosTheta = math.cos(degrees)
            newDir[0] = int(round(cosTheta*direction[0]-senTheta*direction[1]))
            newDir[1] = int(round(senTheta*direction[0]+cosTheta*direction[1]))
            return newDir

        pos = [0, 0]
        direction = [10, 1]
        for move in self.input:
            if move.direction ==  "F":
                pos[0] += direction[0] * move.value
                pos[1] += direction[1] * move.value
            elif move.direction ==  "L":
                direction = rotate(direction, math.radians(move.value))
            elif move.direction ==  "R":
                direction = rotate(direction, math.radians(-move.value))
            elif move.direction ==  "N":
                direction[1] += move.value
            elif move.direction ==  "E":
                direction[0] += move.value
            elif move.direction ==  "S":
                direction[1] -= move.value
            elif move.direction ==  "W":
                direction[0] -= move.value

        return abs(pos[0]) + abs(pos[1])

if __name__=='__main__':
	print(Solution("day12/p2/input.txt").solve())
