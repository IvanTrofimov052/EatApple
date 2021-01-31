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

        if size_memory == 0:
            return "0+"

        if(result_last == "w"):
            print('bvhjcbsj,vcjsvshbvhsbvsvgysvgsyvushvysuhyvsilkvjsiis')
            return self.steps[last_progress]

        return last_progress