# not know - "nk"
# was - "be"
# wall - "w"

from pprint import pprint as pp

from collections import *

class Maping:
    def __init__(self, n, size_of_memory, memory):

        # self.move = {
        #     "0+": (1, 0),
        #     "0-": (-1, 0),
        #     "+0": (0, -1),
        #     "-0": (0, +1),
        #     "00" : (0, 0)
        # }

        self.move = {
            "-0": (-1, 0),
            "+0": (+1, 0),
            "0+": (0, +1),
            "0-": (0, -1),
            "00": (0, 0)
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

        used = [[-1 for i in range(self.n * 2+ 1)] for i in range(self.n * 2+ 1)]

        path = [[[-1, -1] for i in range(self.n * 2+ 1)] for i in range(self.n * 2+ 1)]

        #dist = [-1 for i in range(self.n * self.n * 4 + 1)]

        hohol = []

        while(d):
            coord = d.pop()
            used[coord[0]][coord[1]] = 1

            if self.maping[coord[0]][coord[1]] == "nk":
                print(coord[0], coord[1])
                hohol.append(coord[0])
                hohol.append(coord[1])
                break

            brute_force = ["0+", "0-", "-0", "+0"]

            for i in range(4):
                x = coord[0] + self.move[brute_force[i]][0]
                y = coord[1] + self.move[brute_force[i]][1]

                if(self.maping[x][y] != "w" and used[x][y] == -1 and self.checking_coords(x,y)):
                    d.append([x, y])
                    path[x][y] = [coord[0], coord[1]]

        print(hohol[0], hohol[1], "we go")

        f = path[hohol[0]][hohol[1]]
        f_1 = []

        while(path[f[0]][f[1]][0] != -1):
            f_1 = f
            f = path[f[0]][f[1]]
            pp(f)

        print(self.robot_coords[0], self.robot_coords[1], "robot_coords")
        print(f_1[0], f_1[1])

        if(f_1[0] > self.robot_coords[0]):
            return "0-"
        elif(f_1[0] < self.robot_coords[0]):
            return "0+"
        elif(f_1[1] < self.robot_coords[1]):
            return "+0"
        else:
            return "-0"

        # for i in range(0, 4):
        #     if  self.maping[self.robot_coords[0] + self.move[brute_force[i]][0]][self.robot_coords[1] + self.move[brute_force[i]][1]] != "w":
        #         if (self.checking_coords(self.robot_coords[0] + self.move[brute_force[i]][0], self.robot_coords[1] + self.move[brute_force[i]][1])):
        #             return brute_force[i]

