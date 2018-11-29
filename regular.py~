import math

class Regular():

    def __init__(self):
        self.x_max = 400
        self.y_max = 400

        self.cut_along_x = int(input("Enter block size along x: "))
        self.cut_along_y = int(input("Enter block size along y: "))

	self.bucket_size = int(input("Enter the bucket size: "))

        self.x_scale = range(self.cut_along_x, self.x_max, self.cut_along_x) + [self.x_max]
        self.y_scale = range(self.cut_along_y, self.y_max, self.cut_along_y) + [self.y_max]

	self.mapper = []

        for i in range(len(self.x_scale)*len(self.y_scale)):
		filename = "{}-bucket.txt".format(i)
        	with open(filename, "w+") as opened_file:
			pass
		self.mapper.insert(i,(filename, filename, 0))







    def insert(self, id, x, y):
	bucket, last_bucket, elements_in_bucket = 0, 1, 2

        i,j = self.get_indices_of_2dcell(x,y)
	mapper_index = self.get_cell_no(i, j)

	if self.mapper[mapper_index][elements_in_bucket] < self.bucket_size:

	    with open(self.mapper[mapper_index][bucket], "a+") as opened_file:
		opened_file.write("{} {} {}{}".format(id, x, y, '\n'))

	elif self.mapper[mapper_index][elements_in_bucket] % self.bucket_size == 0:

    	    new_filename = "{}".format(mapper_index)+self.mapper[mapper_index][last_bucket]
    	    with open(new_filename , "a+") as opened_file:
    		opened_file.write("{} {} {}{}".format(id, x, y, '\n'))

            with open(self.mapper[mapper_index][last_bucket], "a+") as opened_file:
                opened_file.write(new_filename)

            self.mapper[mapper_index][last_bucket] = new_filename
	else:

            with open(self.mapper[mapper_index][last_bucket], "a+") as opened_file:
	        opened_file.write("{} {} {}{}".format(id, x, y, '\n'))

	self.mapper[mapper_index][elements_in_bucket] += 1








    def get_all_els_using_x_y(self, x, y):
        cell_no = self.get_cell_no(x,y)
        return self.get_all_els(cell_no)






    def get_all_els(self, cell_no):
        filename = self.mapper[cell_no][0]
        points=[]

        while(True):
            with open(filename) as myfile:
                elements = myfile.read().splilines()

            if len(elements) == self.bucket_size +1:
                filename = elements[-1]
                points += elements[0:-1]
                continue

            else:
                points += elements
                break

        return [map(int, point.split(" ")) for point in points]






    # this function gives indices for a point, of the cell it is in
    def get_indices_of_2dcell(self, x, y):
		i=0;j=0
		while j < len(self.x_scale):
		    if x <= self.x_scale[j]:
		        break
		    j+=1

		while i < len(self.y_scale):
		    if y <= self.y_scale[i]:
		        break
		    i+=1

		return (i,j)

    def get_cell_no(self, index_i, index_j):
		cell_no = (len(self.x_scale) * index_i) + index_j
		return cell_no












    def get_x_y_for_euclidian_dist(self, query_i, query_j, cell_i, cell_j):

		if query_i == cell_i:

		    if query_j < cell_j:
		        if cell_i == 0:
		            y_point = self.y_scale[cell_i]/2
		        else:
		            y_point=(self.y_scale[cell_i-1]+self.y_scale[cell_i])/2
		            x_point=self.x_scale[cell_j-1];

		    elif query_j > cell_j:
		        if cell_i == 0:
		            y_point = self.y_scale[cell_i]/2
		        else:
		            x_point=self.x_scale[cell_j]
		            y_point=(self.y_scale[cell_i-1] + self.y_scale[cell_i])/2

		elif query_j == cell_j:

		    if query_i > cell_i:
		        if cell_j == 0:
		            x_point = self.x_scale[cell_j]/2
		        else:
		            x_point=(self.x_scale[cell_j] + self.x_scale[cell_j-1])/2
		            y_point=self.y_scale[cell_i]

		    elif query_i < cell_i:
		        if cell_j == 0:
		            x_point = self.x_scale[cell_j]/2
		        else:
		            x_point=(self.x_scale[cell_j] + self.x_scale[cell_j-1])/2
		            y_point=self.y_scale[cell_i-1]

		elif query_i < cell_i:

		    if query_j < cell_j:
		        x_point = self.x_scale[cell_j-1]
		        y_point = self.y_scale[cell_i-1]

		    elif query_j > cell_j:
		        x_point = self.x_scale[cell_j]
		        y_point = self.y_scale[cell_i-1]

		elif query_i > cell_i:

		    if query_j < cell_j:
		        x_point = self.x_scale[cell_j-1]
		        y_point = self.y_scale[cell_i]

		    elif query_j > cell_j:
		        x_point = self.x_scale[cell_j]
		        y_point = self.y_scale[cell_i]
		return (x_point, y_point)






    def get_euclidian_dist_for_list(self, query_x, query_y, k_elem_list):
        k_elem_list = [[id, x, y, self.get_euclidian_dist(query_x, query_y, x, y)] for id,x,y in k_elem_list]
        k_elem_list.sort(key = lambda x: x[3])
        return k_elem_list





    def get_euclidian_dist(self, query_x, query_y, data_x, data_y):
    	return math.sqrt(math.pow((data_x-query_x),2) + math.pow((data_y-query_y),2))




    def find_first_k_elements(self, k, query_x, query_y):
        cell_no = self.cell_no(query_x, query_y)
        k_list = self.get_all_els(cell_no)

        cycle_no = 1

        while len(k_list) < k:
            cycle = self.cycle(query_x, query_y, cycle_no)

            if len(cycle) == 0:
                break

            for cell in cycle:
                k_list += get_all_els(cell[0])
                if len(k_list) >= k:
                    break
            cycle_no += 1

        if len(k_list) < k:
            print "The grid does not contains k elements"
            k_list = self.get_euclidian_dist_for_list(query_x, query_y, k_list)
            return k_list

        k_list = k_list[0:k]
        return k_list





    def knn(k, x, y):
        pass




    ''' cycle returns a list of tuples [(cell_no, euclidean_dist),()...]
    takes input as x and y for query point and
    c for cycle no.

	'''

    def cycle(self, query_x, query_y, cycle_no):
	cycle = []

	index_i, index_j = self.get_indices_of_2dcell(query_x, query_y)
	cycle_cell_i, cycle_cell_j = index_i, index_j + cycle_no

        if cycle_cell_i in range(len(self.y_scale)) and cycle_cell_j in range(len(self.x_scale)):
    	    cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j)

            euclidian_dist = self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
	    cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

	    cycle.append((cell_no, euclidian_dist))

	for i in range(1,cycle_no*8):
	    if i<=cycle_no:
	        cycle_cell_i -= 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
                    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j)
		euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

	        cycle.append((cell_no, euclidian_dist))


	    elif i>cycle_no and i <= (3*cycle_no):
		cycle_cell_j -= 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue
		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j)
		euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))

	    elif i > (3*cycle_no) and i <=  (5*cycle_no):
		cycle_cell_i += 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j)
	        euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))

	    elif i > (5*cycle_no) and i <=  (7*cycle_no):
		cycle_cell_j += 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j)
		euclidian_dist = self. get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))

	    elif i  > 7*cycle_no:
		cycle_cell_i -= 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j)
		euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))
	return cycle


class Mapper():
    def __init__(self):
        mapper=[]


reg = Regular()
