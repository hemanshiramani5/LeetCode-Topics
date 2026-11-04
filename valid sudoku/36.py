class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=[[False] *9 for _ in range(9)]
        cols=[[False] *9 for _in range(9)]
        boxes=[[False] * 9 for _in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=ord(board[i][j])-ord('1')
                    boxindex=(i//3)*3+(j//3)
                    if rows[i][num] or cols[j][num] or boxes[boxindex][num]:
                        return False
                    rows[i][num]=cols[j][num]=boxes[boxindex][num]=True
        return True                
