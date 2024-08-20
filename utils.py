"""
This file contains the functions needed to solve the problem set in Secondmind's coding test.

Author: Jacobo Fernandez Vargas
"""
import numpy as np
from numpy.typing import NDArray


def create_graph(file: str) -> tuple[list, NDArray]:
    """
    Function that creates the graph in the form of a connectivity matrix that specifies which players see each other.
    :param file: File name that contains the list of players, and who they see
    :return connections: List with all the connections defined in the file.
    :return connectivityMatrix: NxN connectivity matrix that define the observation graph. For any position i,j in the
    matrix, there is a 1 if player i sees player j.
    :raise ValueError: If any of the players names is longer than 20 or if a player sees another player that was not
    defined in the file.
    :raise FileNotFoundError: If the file was not found.
    """
    with open(file, 'r') as f:
        lines = f.readlines()
    names = [line.split(',')[0].strip() for line in lines]
    players = {name: i for i, name in enumerate(names)}
    for name in players.keys():
        if len(name) >= 20:
            raise ValueError(f'Player {name} has {len(name)} characters. Maximum length is 20 characters.')

    if len(names) != len(players):
        raise ValueError(f'There are at least 2 playes with the same name, they need to be unique names.\n'
                         f'This is the list of names {names}')

    nPlayers = len(players)
    connectivityMatrix = np.zeros((nPlayers, nPlayers)) + np.Inf
    connections = []
    for i, line in enumerate(lines):
        visible = line.split(',')
        sourcePlayer = visible.pop(0).strip()
        source = players[sourcePlayer]
        for target in visible:
            targetPlayer = target.strip()
            if targetPlayer in players:
                target = players[targetPlayer]
                if source != target:
                    connectivityMatrix[source, target] = 1
                    connections.append([source, target])
            else:
                raise ValueError(f'{targetPlayer} player is not defined in the list of players, but is seen by'
                                 f' {sourcePlayer}. Please add a line to the file to include {targetPlayer}')
    return connections, connectivityMatrix


def calculate_largest_island(connections: list, connectivityMatrix: NDArray) -> NDArray:
    """
    Efficiently computes the size of the islands defined in the graph. An island is defined as a group of nodes that are
    connected bi-directionally. Then returns the size of the largest island.
    :param connections: List with all the connections defined in the file.
    :param connectivityMatrix: NxN connectivity matrix that define the observation graph. For any position i,j in the
    matrix, there is a 1 if player i sees player j.
    :return: Size of the largest island in the graph.
    """
    nPlayers = connectivityMatrix.shape[0]
    islands = np.zeros(nPlayers, int) + nPlayers + 1
    sizes = np.zeros(nPlayers, int)
    for (source, target) in connections:
        if connectivityMatrix[target, source] == 1:
            group = np.min([source, target, islands[source], islands[target]])
            if islands[source] == nPlayers + 1:
                sizes[group] += 1
            elif islands[source] != group:
                sizes[islands[source]] -= 1
                sizes[group] += 1
            if islands[target] == nPlayers + 1:
                sizes[group] += 1
            elif islands[target] != group:
                sizes[islands[target]] -= 1
                sizes[group] += 1
            islands[source] = group
            islands[target] = group
    return np.max(sizes)
