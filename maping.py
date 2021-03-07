# not know - "nk"
# was - "be"
# wall - "w"

from pprint import pprint as pp

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

    def moving(self):
        brute_force = ["+0", "-0", "0+", "0-"]

        for i in range(0, 4):
            print(brute_force[i], self.maping[self.robot_coords[0] + self.move[brute_force[i]][0]][self.robot_coords[1] + self.move[brute_force[i]][1]] == "nk")
            if  self.maping[self.robot_coords[0] + self.move[brute_force[i]][0]][self.robot_coords[1] + self.move[brute_force[i]][1]] == "nk":
                return brute_force[i]

        for i in range(0, 4):
            if  self.maping[self.robot_coords[0] + self.move[brute_force[i]][0]][self.robot_coords[1] + self.move[brute_force[i]][1]] != "w":
                return brute_force[i]

