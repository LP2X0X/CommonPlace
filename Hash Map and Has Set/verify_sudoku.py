from typing import List
import math

# Given a partially completed 9x9 Sudoku board, determine if the current state of the board adheres to the rules of the game:

# Each row and column must contain unique numbers between 1 and 9, or be empty (represented as 0).
# Each of the nine 3x3 subgrids that compose the grid must contain unique numbers between 1 and 9, or be empty.
# Note: You are asked to determine whether the current state of the board is valid given these rules, not whether the board is solvable.

# OBSERVATION
# KEY: The board is 9x9
# From intuition, we can see that we need to know if the currently selected number has existed in its ROW, COLUMN or SUBGRID before => This is a very good use of Hash Map for that O(1) access time
# For row and col, we can give each one a hash map of its own. But what about subgrid, how do we know which one belong to which subgrid?
# We know that there are 9 subgrids in total for a 9 x 9 board so base on the indexes position of the currently selected number, can we know its subgrid? => Yes, by dividing the indexes by 3. For example, if the r is 1 and the c is 1, int divide r or c with 3 return 0 => We know that this number is in subgrid 1 (index 0)
# TIME: O(n^2) for nested loop and O(1) constant look up time
# SPACE: O(n^2) for n hash set in each array which each hash set can contain max of n items

def verify_sudoku(board: List[List[int]]) -> bool:
    boardSize = len(board)
    
    # Create Hash Mapes
    rowHashMap = [set() for _ in range(boardSize)]
    colHashMap = [set() for _ in range(boardSize)]
    subgridHashMap = [[set() for _ in range(math.sqrt(boardSize))] for _ in range(math.sqrt(boardSize))]
    
    for row in range(boardSize):
        for column in range(boardSize):
            num = board[row][column]
            
            if num == 0: continue
            
            if num in rowHashMap[row]: 
                return False
            else:
                rowHashMap.add(num)
                
            if num in colHashMap[column]:
                return False
            else:
                colHashMap.add(num)
                
            if num in subgridHashMap[row // math.sqrt(boardSize)][column // math.sqrt(boardSize)]:
                return False
            else:
                subgridHashMap[row // math.sqrt(boardSize)][column // math.sqrt(boardSize)].add(num)
    return True
             