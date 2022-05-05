from pprint import pprint

global counter 
counter = 0

def solve_puzzle(puzzle):
    #empty cells represented by -1

    #helper function to find the next empty cell
    def find_next_empty(puzzle):
        for r in range(9):
            for c in range(9):
                if puzzle[r][c] == -1:
                    return r,c
        
        return None, None

    #helper function to see if guess is valid
    def is_valid(puzzle, guess, row, col):
        #check row
        row_vals = puzzle[row]
        if guess in row_vals:
            return False

        #check column
        col_vals = [puzzle[i][col] for i in range(9)]
        if guess in col_vals:
            return False


        #check 3x3 matrix
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range(row_start, row_start +3):   
            for c in range(col_start, col_start + 3):
                if puzzle[r][c] == guess:
                    return False

        #if passes all checks
        return True


    #solver function
    def solve_sodoku(puzzle):
        #initializes recursion counter
        
        #find next instance of empty cell
        row, col = find_next_empty(puzzle)

        #if all cells full
        if row is None:
            return True
        
        #recursively check each number 1-9 in each empty cell

        for guess in range(1, 10):
            global counter 
            counter += 1
            if counter < 250000:

                if is_valid(puzzle, guess, row, col):
                    puzzle[row][col] = guess
                    if solve_sodoku(puzzle):
                        return True
                puzzle[row][col] = -1

            else: 
                break

        #no solutions work
        return False

    solvable = solve_sodoku(puzzle)
    pretty = pprint(puzzle)

    return(solvable, pretty, counter)
        
   
