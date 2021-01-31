import sys

from myparser import *
from robot_a import *
from make_output import *

robot = Robot_a()
parser_1 = ParserInput()
making_output = Make_output()

path_output = sys.argv[2]

input_args = parser_1.parsing_input_file(sys.argv[1])
move = robot.make_move(input_args)
making_output.make_output(move, path_output, input_args)

print(input_args)