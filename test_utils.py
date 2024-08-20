"""
File that contains the code to test the functions defined in utils.py

Author: Jacobo Fernandez Vargas
"""
import pytest
from utils import calculate_largest_island, create_graph
import numpy as np


def test_create_graph():
    expectedConnections = [[0, 3], [0, 4], [1, 2], [2, 3], [3, 2], [3, 0], [4, 3]]
    inf = np.Inf
    expectedMatrix = np.array([[inf, inf, inf, 1., 1.],
                               [inf, inf, 1., inf, inf],
                               [inf, inf, inf, 1., inf],
                               [1., inf, 1., inf, inf],
                               [inf, inf, inf, 1., inf]])
    assertion = {}
    with pytest.raises(FileNotFoundError) as exc_info:
        create_graph('./test_files/asdfasdf.txt')
    assertion['Wrong File'] = exc_info.type is FileNotFoundError

    with pytest.raises(ValueError) as exc_info:
        create_graph('./test_files/long_name.txt')
    assertion['Long Name'] = exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        create_graph('./test_files/not_defined_player.txt')
    assertion['Not defined Player'] = exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        create_graph('./test_files/repeated_name.txt')
    assertion['Repeated Name'] = exc_info.type is ValueError

    connections, connectivityMatrix = create_graph('./test_files/example_file.txt')
    assertion['Correct connections'] = connections == expectedConnections
    assertion['Correct matrix'] = np.all(expectedMatrix == connectivityMatrix)
    passed = all(assertion.values())
    if not passed:
        items = ['Test. ' + str(k) + ' Passed:' + str(v) for k, v in assertion.items()]
        print('\n'.join(items))
        print(f'Expected connections: {expectedConnections} obtained connections {connections}')
        print(f'Expected matrix: {expectedMatrix} obtained matrix {connectivityMatrix}')
    assert passed


def test_calculate_largest_island():
    assertion = {}
    connections, connectivityMatrix = create_graph('./test_files/example_file.txt')
    answer = calculate_largest_island(connections, connectivityMatrix)
    assertion['Example File'] = answer == 3
    connections, connectivityMatrix = create_graph('./test_files/loop_file.txt')
    answer = calculate_largest_island(connections, connectivityMatrix)
    assertion['Example File'] = answer == 5
    connections, connectivityMatrix = create_graph('./test_files/empty_player.txt')
    answer = calculate_largest_island(connections, connectivityMatrix)
    assertion['Alone'] = answer == 0
    passed = all(assertion.values())
    if not passed:
        items = ['Test. ' + str(k) + ' Passed:' + str(v) for k, v in assertion.items()]
        print('\n'.join(items))
    assert passed
