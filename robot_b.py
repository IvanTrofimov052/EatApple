class Robot_b:
    def __init__(self):
        self.reversed_move={
            "0+" : "0-",
            "0-": "0+",
            "+0": "-0",
            "-0": "+0",
        }

    def make_move(self, input_args):
        result_last = input_args["result_last"]
        last_progress = input_args["last_progress"]

        if int(input_args['size_of_memory']) == 0:
            input_args['size_of_memory'] += 3
            input_args['memory'].append("zero_zero_point")
            input_args['memory'].append("0+")
            input_args["memory"].append(0)
            return "0+"

        if(int(input_args["memory"][2]) < (int(input_args["n"]))):
            if result_last != "w" and last_progress == "+0":
                input_args["memory"][2] = int(input_args["memory"][2]) + 1

            if result_last == "w":
                input_args['memory'][1] = self.reversed_move[input_args['memory'][1]]
                return "+0"

            print(input_args["memory"][2])

            return input_args['memory'][1]

        if int(input_args['size_of_memory']) == 3:
            input_args['size_of_memory'] += 1
            input_args['memory'].append("zero_zero_point")
            return "-0"

        if result_last == "w":
            input_args['memory'][1] = self.reversed_move[input_args['memory'][1]]
            return "0-"


        return input_args['memory'][1]