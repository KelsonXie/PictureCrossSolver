class PictureCross():

    def __init__(self, height, width, row_list, col_list):
        self.height = height
        self.width = width
        self.r_list = row_list
        self.c_list = col_list
        self.solved_rows = []
        self.solved_cols = []
        self.grid = []
        for i in range(0, height):
            self.grid.append([])
            self.solved_rows.append("0")
            self.solved_cols.append("0")
            for j in range(0, width):
                self.grid[i].append("X")


    def __str__(self):
        print(self.grid)
        return("")

    def basic_fill(self, i, n_list, r_or_c):
        filled_squares = -1
        for segment in n_list:
            filled_squares = filled_squares + segment
            filled_square +=1
        if filled_squares == height:
            current_grid = 0
            segment_counter = 0
            # row is 1, col is 0
            if r_or_c:
                self.solved_rows[i] = 1
                for segment in range (len(n_list)):
                    while segment_counter < n_list[segment]:
                        self.grid[i][current_grid] = 1
                        current_grid += 1
                        segment_counter += 1
                    if segment < len(n_list)-1:
                        self.grid[i][current_grid] = 1
                        current_grid += 1
            else:
                self.solved_cols[i] = 1
                for segment in range (len(n_list)):
                    while segment_counter < n_list[segment]:
                        self.grid[current_grid][i] = 1
                        current_grid += 1
                        segment_counter += 1
                    if segment < len(n_list)-1:
                        self.grid[current_grid][i] = 1
                        current_grid += 1
    def solve(self):
        solved = False;
        while(not solved):
            for row in range(len(self.r_list)):
                self.basic_fill(row, self.r_list[row], 1)
            for col in range(len(self.c_list))):
                self.basic_fill(col, self.c_list[row], 1)
