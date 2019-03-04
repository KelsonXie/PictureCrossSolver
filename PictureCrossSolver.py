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

    def solve(self):
        for i in range(0, )
        solved = False;
        while(not solved):
            
