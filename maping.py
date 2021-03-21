# not know - "nk"
# was - "be"
# wall - "w"

from pprint import pprint as pp

from collections import *

class Maping:
    def __init__(self, n, size_of_memory, memory):

        self.move = {
            "0+": (1, 0),
            "0-": (-1, 0),
            "+0": (0, -1),
            "-0": (0, +1),
            "00" : (0, 0)
        }

        self.maping = [[] for _ in range(2*n)]

        for i in range(2 * n):
            self.maping[i] = ["nk" for _ in range(2*n)]


        self.maping[n-1][n-1] = "be"

        self.robot_coords = (n-1, n-1)

        for i in range(0, size_of_memory, 2):
            if(memory[i+1] == "w"):
                self.maping[self.robot_coords[0] + self.move[memory[i]][0]][self.robot_coords[1] + self.move[memory[i]][1]] = "w"
            else:
                self.maping[self.robot_coords[0] + self.move[memory[i]][0]][self.robot_coords[1] + self.move[memory[i]][1]] = "be"

                self.robot_coords = (self.robot_coords[0] + self.move[memory[i]][0], self.robot_coords[1] + self.move[memory[i]][1])

        self.maping[self.robot_coords[0]][self.robot_coords[1]] = "I"

        pp(self.maping)

        self.n = n

    def checking_coords(self, x , y):
        return (x >= 0) and (x < 2*self.n) and  (y >= 0) and (y < 2*self.n)

    def moving(self):
        brute_force = ["+0", "-0", "0+", "0-"]

        for i in range(0, 4):
            print(brute_force[i], self.maping[self.robot_coords[0] + self.move[brute_force[i]][0]][self.robot_coords[1] + self.move[brute_force[i]][1]] == "nk")
            if  self.maping[self.robot_coords[0] + self.move[brute_force[i]][0]][self.robot_coords[1] + self.move[brute_force[i]][1]] == "nk":
                if(self.checking_coords(self.robot_coords[0] + self.move[brute_force[i]][0], self.robot_coords[1] + self.move[brute_force[i]][1])):
                    print("wtf")
                    return brute_force[i]


        d = deque()
        d.append(self.robot_coords)

        used = [0 for i in range(self.n * self.n * 4 + 1)]

        path = []

        #dist = [-1 for i in range(self.n * self.n * 4 + 1)]

        hohol = []

        while(d):

            coords = d.pop()

            print(coords[0], coords[1])

            used[coords[0] * 2 * self.n + coords[1]] = 1

            if(self.maping[coords[0]][coords[1]] == "nk"):
                hohol.append(coords[0])
                hohol.append(coords[1])
                break

            brute_force = ["+0", "-0", "0+", "0-"]

            for i in range(0, 4):
                x = coords[0] + self.move[brute_force[i]][0]
                y = coords[1] + self.move[brute_force[i]][1]

                if self.checking_coords(x, y):
                    if(self.maping[x][y] != "w"):
                        if used[x * 2 * self.n + y] == 0:
                            path[x * 2 * self.n + y] = coords
                            lol = (x, y)
                            d.append(lol)

        # this is stupid dont forgot about path
        # if(self.robot_coords[0] > hohol[0]):
        #     return "0+"
        # elif(self.robot_coords[0] < hohol[0]):
        #     return "0-"
        # elif(self.robot_coords[1] < hohol[1]):
        #     return "+0"
        # else:
        #     return "-0"


        # for i in range(0, 4):
        #     if  self.maping[self.robot_coords[0] + self.move[brute_force[i]][0]][self.robot_coords[1] + self.move[brute_force[i]][1]] != "w":
        #         if (self.checking_coords(self.robot_coords[0] + self.move[brute_force[i]][0], self.robot_coords[1] + self.move[brute_force[i]][1])):
        #             return brute_force[i]

