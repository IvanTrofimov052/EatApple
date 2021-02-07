class Robot_a:
    def __init__(self):
        self.steps = {
            '0+':'0-',
            '0-':'0+'
        }

    def make_move(self, input_args):
        result_last = input_args['result_last']
        last_progress = input_args['last_progress']
        size_memory = input_args['size_of_memory']
        x = input_args['x']
        y = input_args['y']
        if int(input_args['size_of_memory']) == 0:
            if int(x) != 1:
                return '-0'

            if int(y) != 1:
                return '0-'

        if int(input_args['size_of_memory']) == 0:
            input_args['size_of_memory'] += 2
            input_args['memory'].append("zero_zero_point")
            input_args['memory'].append("+0")

        if(int(x) == 1 and input_args['memory'][1] == '-0'):
            input_args['memory'][1] = "+0"
            return "0+"

        elif(int(x) == (int(input_args['n'])) and input_args['memory'][1] == '+0'):
            input_args['memory'][1] = "-0"
            return "0+"


        return input_args['memory'][1]