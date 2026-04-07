class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We are given 9x9 2d array, and effecively:
        # We must check for duplicates in each row, column and 3x3

        # row
        for row in board:
            # check duplicates, use hashmap
            rowset = set()
            for entry in row:
                if entry != ".":
                    if entry in rowset:
                        return False
                    else:
                        rowset.add(entry)
        
        # column
        for j in range(9):
            column = ["."] * 9
            for i in range(9):
                column[i] = board[i][j]
            columnset = set()
            for entry in column:
                if entry != ".":
                    if entry in columnset:
                        return False
                    else:
                        columnset.add(entry)
        
        #3x3 grids
        for a in range(3):
            for b in range(3):
                # contruct array from 3x3 grid
                smallie = ["."] * 9
                smallie[0:3] = board[a * 3][(b * 3):((b * 3) + 3)]
                smallie[3:6] = board[(a * 3) + 1][(b * 3):((b * 3) + 3)]
                smallie[6:9] = board[(a * 3) + 2][(b * 3):((b * 3) + 3)]
                
                #Check it
                smallieset = set()
                for entry in smallie:
                    if entry != ".":
                        if entry in smallieset:
                            return False
                        else:
                            smallieset.add(entry)

        return True

        