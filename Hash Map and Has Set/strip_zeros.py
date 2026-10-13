from typing import List

# Given an m * n matrix, for each 0, set its row and col to 0 in place.

# OBSERVATION:
# KEY: In place

# Intuition: Traverse the matrix, if find 0, set all items with same row and col to 0 => Time: Find 0 takes O(m * n) max (worst case, all are 0), convert the row and col to 0 takes O(m + n) max so it will take max O(m * n * (m + n)) => Space: O(1) since we modify in space

# Better solution: Technically, we only need to know if the row and col of current number belong to any register will-be-zero col and row => Traverse the matrix, find all 0 position => add its col and row to a hash set contain col and row indexes respectively (using hash set will prevent duplication of 0 on the same row or col)
# TIME: O(m * n) since we traverse the matrix twice
# SPACE: O(m + n) since we use 2 hash set for col and row and each can grow to their max respective size which is m and n 
def strip_zero_hash_set (matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return 
    
    rowSet = set()
    colSet = set()
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rowSet.add(row)
                colSet.add(col)
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in rowSet or col in colSet:
                matrix[row][col] = 0
                continue
            
            
# Is there a way we can reduce even more the space used for this?
# Could we use the first col and row as a replacement for the rowSet and colSet hash set? Yes, since its basically the same => We traverse the matrix, find the 0 in it then based on the col and row it belong to, set the number at the corresponding first col and row to 0 => We then traverse the submatrix (subtract the first col and row) then based on the first col and row, set the current number to 0 or not
# But what happen if the first col and row already contain a 0? => We must traverse them first and use a flags to know if there is any existing 0 in them or not. Then when the process is done, we travers the first col and row again to make them all 0
# TIME: O(m * n) since we still traverse twice + 2 O(m) + 2 O(n) for the two traverse first row and col time => O(m + n)
# SPACE: O(1)

def strip_zero (matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return 
    
    rowCnt = len(matrix) 
    colCnt = len(matrix[0])
    
    isZeroInFirstRow = False
    isZeroInFirstCol = False
    
    for col in range(colCnt):
        if matrix[0][col] == 0:
            isZeroInFirstRow = True
            break
    for row in range(rowCnt):
        if matrix[row][0] == 0:
            isZeroInFirstCol = True
            break
        
    # Traverse submatrix, not the matrix itself, to find the 0 and set the first col and row corresponding position values
    for row in range(1, rowCnt):
        for col in range(1 ,colCnt):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0
    
    for row in range(1, rowCnt):
        for col in range(1 ,colCnt):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0
    
    if isZeroInFirstRow:
        for col in range(colCnt):
            matrix[0][col] = 0
    if isZeroInFirstCol:
        for row in range(rowCnt):
            matrix[row][0] = 0
        
        
            
            
    