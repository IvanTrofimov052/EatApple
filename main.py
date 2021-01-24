import sys

from myparser import *



parser_1 = ParserInput()

input_args = parser_1.parsing_input_file(sys.argv[1])

print(input_args)