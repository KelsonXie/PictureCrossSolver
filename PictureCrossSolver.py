class PictureCross():

    def __init__(self, height, width, row_list, col_list):
        self.height = height
        self.width = width
        self.r_list = height_list
        self.c_list = width_list
        self.grid = []
        for i in range(0, height-1):
            self.grid.append([])
            for j in range(0, width-1):
                self.grid[i].append(0)

    def __str__(self):
        print(self.grid)

a = PictureCross(10, 10, [1], [1])
print(a)
