from maping import *

class Robot_b:
    def __init__(self):
        self.reversed_move={
            "0+": "+0",
            "+0":  "0-",
            "0-": "-0",
            "-0": "0+"
        }

        self.re_move = {
            "0+": "0-",
            "0-": "0+",
            "+0": "-0",
            "-0": "+0",
        }

    def make_move(self, input_args):
        n = int(input_args['n'])
        last_progress = input_args['last_progress']
        memory = input_args['memory']
        size_of_memory = input_args["size_of_memory"]
        result_last = input_args["result_last"]

        input_args["size_of_memory"] += 2
        input_args['memory'].append(last_progress)
        input_args['memory'].append(result_last)

        map_maze = Maping(n, size_of_memory + 2, memory + [last_progress, result_last])

        return map_maze.moving()


        # result_last = input_args["result_last"]
        # last_progress = input_args["last_progress"]
        # size_of_memory = int(input_args["size_of_memory"])
        # memory = input_args['memory']
        #
        # if(size_of_memory != 0):
        #     print(result_last)
        #     print(last_progress)
        #
        #     if(result_last == "w" and input_args['memory'][1] == last_progress):
        #         print("jscjcj")
        #         input_args['memory'][1] = self.reversed_move[last_progress]
        #
        #         return self.reversed_move[last_progress]
        #
        #     if input_args['memory'][1] == last_progress:
        #         return  self.reversed_move[last_progress]
        #     else:
        #         return input_args['memory'][1]
        #
        #
        # input_args["size_of_memory"] += 2
        # input_args['memory'].append("fuck")
        # input_args['memory'].append("0+")
        #
        # return "0+"

        # result_last = input_args["result_last"]
        # last_progress = input_args["last_progress"]
        #
        # if int(input_args['size_of_memory']) == 0:
        #     input_args['size_of_memory'] += 3
        #     input_args['memory'].append("zero_zero_point")
        #     input_args['memory'].append("0+")
        #     input_args["memory"].append(1)
        #     return "0+"
        #
        # if(int(input_args["memory"][2]) < (int(input_args["n"]))):
        #     print(input_args["memory"][2], ' nkkankcnacnakcmamckamckamckamcamcacakcmamca')
        #
        #     if result_last != "w" and last_progress == "+0":
        #         input_args["memory"][2] = int(input_args["memory"][2]) + 1
        #
        #     if result_last == "w":
        #         input_args['memory'][1] = self.reversed_move[input_args['memory'][1]]
        #         return "+0"
        #
        #     return input_args['memory'][1]
        #
        # if int(input_args['size_of_memory']) == 3:
        #     input_args['size_of_memory'] += 1
        #     input_args['memory'].append("zero_zero_point")
        #     return "-0"
        #
        # if result_last == "w":
        #     input_args['memory'][1] = self.reversed_move[input_args['memory'][1]]
        #     return "0-"
        #
        #
        # return input_args['memory'][1]