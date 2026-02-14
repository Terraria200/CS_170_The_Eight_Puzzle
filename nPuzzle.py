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



class TreeNode:
    def __init__(self, parent, board, g, h):
        self.parent = parent
        self.board = board
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

    def board_to_tuple(self):
        return tuple(tuple(row) for row in self.board)

    def solved(self):
        return self.board == eight_goal_state


# Utility functions_

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()


def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

