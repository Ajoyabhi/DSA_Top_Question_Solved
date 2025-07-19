"""
Valid Sudoku
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:



Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
Example 2:

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from collections import defaultdict

def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            if val in rows[r]:
                return False
            rows[r].add(val)
            if val in cols[c]:
                return False
            cols[c].add(val)
            box_idx = (r // 3) * 3 + (c // 3)
            if val in boxes[box_idx]:
                return False
            boxes[box_idx].add(val)
    return True

"""
1. Initialization : It initializes three lists of sets:
   
   - rows : A list of 9 sets, where rows[r] will store the numbers encountered in row r .
   - cols : A list of 9 sets, where cols[c] will store the numbers encountered in column c .
   - boxes : A list of 9 sets, where boxes[b] will store the numbers encountered in the 3x3 sub-box b .
2. Iterating through the board : The code iterates through each cell of the 9x9 board using nested loops with row index r and column index c .
3. Skipping empty cells : If the current cell board[r][c] contains a . (which signifies an empty cell), it skips to the next cell because empty cells don't violate the Sudoku rules.
4. Checking for duplicates : For each non-empty cell val :
   
   - Row Check : It checks if val is already present in rows[r] . If it is, it means a duplicate exists in that row, and the function immediately returns False .
   - Column Check : It checks if val is already present in cols[c] . If it is, a duplicate exists in that column, and the function returns False .
   - Box Check : It calculates the box_idx for the current cell. A Sudoku board has 9 3x3 sub-boxes. The formula (r // 3) * 3 + (c // 3) correctly maps the (r, c) coordinates to their corresponding 3x3 box index (0-8). It then checks if val is already present in boxes[box_idx] . If it is, a duplicate exists in that 3x3 sub-box, and the function returns False .
5. Adding to sets : If val passes all three checks (no duplicates found in its row, column, or box), it is added to the respective sets ( rows[r] , cols[c] , and boxes[box_idx] ) to mark its presence.
6. Returning True : If the loops complete without finding any duplicates, it means the Sudoku board is valid, and the function returns True .
This approach uses sets for efficient (O(1)) average-time lookups and insertions, making the overall time complexity (O(N^2)) where N is the size of the board (9 in this case), as each cell is visited once.
"""


#  Hash Set (One Pass)
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

output = isValidSudoku(board)
print(output)

suduko_check = Solution()
print(suduko_check.isValidSudoku(board))