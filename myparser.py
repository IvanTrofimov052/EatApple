class ParserInput:
    def parsing_input_file(self, location_file):
        response = {}

        with open(location_file, 'r') as file:
            n = int(file.readline().replace('\n', ""))
            print(n)
            progress = int(file.readline().replace('\n', ""))
            x, y = file.readline().split()
            last_progress = file.readline().replace('\n', "")
            result_last = file.readline().replace('\n', "")
            size_of_memory = int(file.readline())
            memory = file.readline().split()

            response['n'] = n
            response['progress'] = progress
            response['x'] = x
            response['y'] = y
            response['last_progress'] = last_progress
            response['result_last'] = result_last
            response['size_of_memory'] = size_of_memory
            response['memory'] = memory

        return response