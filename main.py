"""
This document contains the code need to run the program that finds the solution to Secondmind's code
exercise.

Author: Jacobo Fernandez Vargas
"""
from utils import calculate_largest_island, create_graph
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Wrong format. It should be: python {sys.argv[0]} path_to_file')
    file = sys.argv[1]
    connections, connectivityMatrix = create_graph(file)
    answer = calculate_largest_island(connections, connectivityMatrix)
    print(answer)
