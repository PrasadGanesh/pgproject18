class Regular():

    def __init__(self):
        x_max = 400
        y_max = 400

        cut_along_x = int(input("Enter block size along x"))
        cut_along_y = int(input("Enter block size along y"))

        scale_for_x_axis = [cell for cell in range(0, x_max, cut_along_x)]
        scale_for_y_axis = [cell for cell in range(0, y_max, cut_along_y)]

    def insert(self, id, x, y):
        pass

    def get_all_els(self, x, y):
        pass

    def get_all_els(self, block_number):
        pass


row_of_mapper = len(scale_for_x_axis)
col_of_mapper = len(scale_for_y_axis)



