class Make_String:
    def string_from_array(self, array):
        string = ""

        for i in array:
            string += str(i) + " "

        return string



class Make_output:
    def __init__(self):
        self.make_string = Make_String()

    def make_output(self, step,  path_output, input_args):
        memory_string = self.make_string.string_from_array(input_args['memory'])
        size_of_memory = input_args['size_of_memory']

        with open(path_output, 'w') as file:
            file.write(step + '\n ' + str(size_of_memory ) + ' \n' + memory_string + '\n')
