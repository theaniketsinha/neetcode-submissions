class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        boxes = [set() for x in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                box_num = ((i//3)*3)+(j//3)

                if value != ".":
                    if value in rows[i] or value in cols[j] or value in boxes[box_num]:
                        return False
                    
                    else:
                        rows[i].add(value)
                        cols[j].add(value)
                        boxes[box_num].add(value)
                
        
        return True