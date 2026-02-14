#I used Python for this project

import heapq as min_heap_esque_queue
import copy

# Predefined puzzles for testing
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]

veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]

oh_boy = [[8, 7, 1],
          [6, 0, 2],
          [5, 4, 3]]

eight_goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]



class Node:
    def __init__(self, parent, state, g, h):
        self.parent = parent
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

    def state_to_tuple(self):
        return tuple(tuple(row) for row in self.state)


# Utility functions_

def misplaced_tile(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != eight_goal_state[i][j]:
                count += 1
    return count


def manhattan_distance(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i = (value - 1) // 3
                goal_j = (value - 1) % 3
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def expand(node, heuristic_type): #function used to expand problem based on which heuristic we're using
    children = []
    i, j = find_blank(node.state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = copy.deepcopy(node.state)
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]

            if heuristic_type == 0:
                h = 0
            elif heuristic_type == 1:
                h = misplaced_tile(new_state)
            else:
                h = manhattan_distance(new_state)

            child = Node(node, new_state, node.g + 1, h)
            children.append(child)

    return children

# -----------------------------
# Queueing Function, which is used to edit the states on our current 8 puzzle board
# -----------------------------

def queueing_function(frontier, children):
    for child in children:
        heapq.heappush(frontier, child)
    return frontier

# General search algorithm
def general_search(initial_state, heuristic_type):
    # MAKE-NODE(problem.INITIAL-STATE)
    if heuristic_type == 0:
        h = 0
    elif heuristic_type == 1:
        h = misplaced_tile(initial_state)
    else:
        h = manhattan_distance(initial_state)

    start_node = Node(None, initial_state, 0, h)

    # MAKE-QUEUE
    nodes = []
    heapq.heappush(nodes, start_node)

    explored = set()
    nodes_expanded = 0
    max_queue_size = 0


