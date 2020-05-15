import working_data
import sys

filename = sys.argv[1:]
for file in filename:
	working_data.visualize(file)
	working_data.detect_problems(file)

