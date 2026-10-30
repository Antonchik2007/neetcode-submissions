class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check rows
        for row in range(9):
            seen = set()
            for cell in range(9):
                c = board[row][cell]
                if c == ".":
                    continue
                elif c in seen:
                    return False
                else:
                    seen.add(c)
        #check columns
        for cell in range(9):
            seen = set()
            for row in range(9):
                c = board[row][cell]
                if c == ".":
                    continue
                elif c in seen:
                    return False
                else:
                    seen.add(c)
        #check squares
        def check_square(row, column):
            seen = set()
            column_counter = column
            row_counter = row
            while row_counter < row+3:
                while column_counter < column+3:
                    cell = board[row_counter][column_counter]
                    if cell == ".":
                        column_counter += 1
                        continue
                    elif cell in seen:
                        return False
                    else:
                        seen.add(cell)
                    column_counter += 1
                
                column_counter = column
                row_counter += 1
        row = 0
        while row < 9:
            column = 0
            while column < 9:
                if check_square(row, column) == False:
                    return False
                column += 3
            row += 3
        return True
                


        

