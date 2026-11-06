class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            s = set()

            for j in range(9):
                n = board[i][j]
                if n == ".":
                    continue
                elif n in s:
                    return False
                s.add(n)
        
        for i in range(9):
            s = set()

            for j in range(9):
                n = board[j][i]
                if n == ".":
                    continue
                elif n in s:
                    return False
                s.add(n)

        for i in range(3):
       
            for j in range(3):
                s = set()
                for x in range(3):
                    for y in range(3):

                        n = board[i*3 + x][j*3 + y]
                        if n == ".":
                            continue
                        elif n in s:
                                return False
                        s.add(n)

        return True