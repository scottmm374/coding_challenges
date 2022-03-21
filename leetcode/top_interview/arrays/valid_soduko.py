

def soduko(board):

#* Holds intersect square of each mini square as a starting point to check all mini sqyares for accuracy.
    find_mid_of_each_mini_square = {(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)}
   

    for row in range(len(board)):
        check_rows = set()
        check_cols = set()
        
        
        for col in range(len(board)):
            
            #* Variables to check specific values of each square, row_value traveling along the rows while col_value travels cols
            row_value = board[row][col]
            col_value = board[col][row]

           
            # * Below checks through each mini square, using the middle(intersect) at the start and checking the eight squares around it.
       
            if (row, col) in find_mid_of_each_mini_square:
                check_sq = set()
                
                if board[row][col] not in check_sq:
                    if board[row][col] != ".":
                        check_sq.add(board[row][col])
                else:
                    return False

                if board[row][col - 1] not in check_sq:
                    if board[row][col - 1] != ".":
                        check_sq.add(board[row][col - 1])
                else:
                    return False

                if board[row][col + 1] not in check_sq:
                    if board[row][col + 1] != ".":
                        check_sq.add(board[row][col + 1])
                else:
                    return False

                if board[row - 1][col]not in check_sq:
                    if board[row - 1][col] != ".":
                        check_sq.add(board[row - 1][col])
                else:
                    return False

                if board[row + 1][col] not in check_sq:
                    if board[row + 1][col] != ".":
                        check_sq.add(board[row + 1][col])
                else:
                    return False

                if board[row - 1][col - 1] not in check_sq:
                    if board[row - 1][col - 1] != ".":
                        check_sq.add(board[row - 1][col - 1])
                else:
                    return False

                if board[row + 1][col - 1] not in check_sq:
                    if board[row + 1][col - 1] != ".":
                        check_sq.add(board[row + 1][col - 1])
                else:
                    return False

                if board[row - 1][col + 1] not in check_sq:
                    if board[row - 1][col + 1] != ".":
                        check_sq.add(board[row - 1][col + 1])
                else:
                    return False

                if board[row + 1][col + 1] not in check_sq:
                    if board[row + 1][col + 1] != ".":
                        check_sq.add(board[row + 1][col + 1])
                else:
                    return False

    

                # * Checks for the value in check_col set() and check_row set() for duplicates, if not there adds to set.

            if col_value != ".":
                if col_value in check_cols:
                    return False
                else:
                    check_cols.add(col_value)
            
            
            if row_value != ".":
                if row_value in check_rows:
                    return False
                else:
                    check_rows.add(row_value)
            else:
                continue
            
    return True
            
# Runtime: 145 ms  43.56%
# Memory Usage: 13.9 MB   48.77%      
   









