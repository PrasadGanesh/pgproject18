import math

class Grid():

    def __init__(self):
        self.x_max = 400
        self.y_max = 400

	self.bucket_size = int(input("Enter the bucket size: "))

        self.x_scale = [400]
        self.y_scale = [400]

	self.mapper = []

        self.bucket_count = 0

        self.bucket_access_record=[]
        self.file_access_record={}


        for i in range(len(self.x_scale)*len(self.y_scale)):
		filename = "{}-grid_bucket.txt".format(self.bucket_count)
        	with open(filename, "w+") as opened_file:
			pass
		self.mapper.insert(i,[filename, 0, 0])
                self.bucket_count +=1







    def divide_x_axis(self, division_point):
        j=0
	while j < len(self.x_scale):
            if division_point <= self.x_scale[j]:
                break
	    j+=1

        self.x_scale.insert(j, division_point)

        next_jump_in_mapper = len(self.x_scale)
        div_cell_no = j


        for unused in range(len(self.y_scale)):
            filename = self.mapper[div_cell_no][0]
            self.mapper.insert(div_cell_no, [filename, 0, 0])

            with open(filename) as myfile:
                elements = myfile.read().splitlines()

            self.mapper[div_cell_no][1] = 0

            self.mapper[div_cell_no][2] = len(elements)


            elements =  [map(int, point.split(" ")) for point in elements]
            for point in elements:
                i,j = self.get_indices_of_2dcell(point[1], point[2])
                mapper_index = self.get_cell_no(i, j)
                if mapper_index == div_cell_no:
                	self.mapper[mapper_index][1] +=1

            div_cell_no += next_jump_in_mapper


    def divide_y_axis(self, division_point):
        i=0
	while i < len(self.y_scale):
            if division_point <= self.y_scale[i]:
                break
	    i+=1

        self.y_scale.insert(i, division_point)

        div_cell_no = self.get_cell_no(i, 0)

        for unused in range(len(self.x_scale)):
            filename = self.mapper[div_cell_no][0]
            self.mapper.insert(div_cell_no + len(self.x_scale), [filename, 0, 0])

            with open(filename) as myfile:
                elements = myfile.read().splitlines()

            self.mapper[div_cell_no + len(self.x_scale)][1] = 0

            self.mapper[div_cell_no + len(self.x_scale)][2] = len(elements)

            elements =  [map(int, point.split(" ")) for point in elements]
            for point in elements:
                i,j = self.get_indices_of_2dcell(point[1], point[2])
                mapper_index = self.get_cell_no(i, j)
                if mapper_index == (div_cell_no + len(self.x_scale)):
                	self.mapper[mapper_index][1] +=1

            div_cell_no +=1







    def insert(self, id, x, y):
	bucket, num_of_els_in_cell, elements_in_bucket = 0, 1, 2

        i,j = self.get_indices_of_2dcell(x,y)
	mapper_index = self.get_cell_no(i, j)

	if self.mapper[mapper_index][num_of_els_in_cell] < self.bucket_size:

            if self.mapper[mapper_index][elements_in_bucket] < self.bucket_size:

                with open(self.mapper[mapper_index][bucket], "a+") as opened_file:
		    opened_file.write("{} {} {}{}".format(id, x, y, '\n'))

	        self.mapper[mapper_index][elements_in_bucket] += 1
                self.mapper[mapper_index][num_of_els_in_cell] += 1

            elif self.mapper[mapper_index][elements_in_bucket] == self.bucket_size:
                filename = self.mapper[mapper_index][bucket]

                with open(filename) as myfile:
                    elements = myfile.read().splitlines()

                elements =  [map(int, point.split(" ")) for point in elements] + [[id,x,y]]

                els_in_new_bucket = [point for point in elements if self.get_cell_no_using_xy(point[1], point[2]) == mapper_index]

                els_in_old_bucket = [point for point in elements if point not in els_in_new_bucket]

                for old_point in els_in_old_bucket:
                    index = self.get_cell_no_using_xy(old_point[1], old_point[2])
                    self.mapper[index][elements_in_bucket] = len(els_in_old_bucket)

                with open(filename, 'w') as opened_file:
                    for old_point in els_in_old_bucket:
                        opened_file.write("{} {} {}{}".format(old_point[0], old_point[1], old_point[2], '\n'))

                new_filename = "{}-grid_bucket.txt".format(self.bucket_count+1)
                self.bucket_count +=1


                with open(new_filename, 'w') as opened_file:
                    for new_point in els_in_new_bucket:
                        opened_file.write("{} {} {}{}".format(new_point[0], new_point[1], new_point[2], '\n'))

                self.mapper[mapper_index][bucket] = new_filename
                self.mapper[mapper_index][num_of_els_in_cell] = len(els_in_new_bucket)
                self.mapper[mapper_index][elements_in_bucket] = len(els_in_new_bucket)

        else:
            filename = self.mapper[mapper_index][bucket]

            with open(filename) as myfile:
                    elements = myfile.read().splitlines()

            elements =  [map(int, point.split(" ")) for point in elements] + [[id,x,y]]
            max_x = max(elements, key = lambda x: x[1])[1]
            max_y = max(elements, key = lambda x: x[2])[2]
            min_x = min(elements, key = lambda x: x[1])[1]
            min_y = min(elements, key = lambda x: x[2])[2]

            span_along_x = max_x-min_x
            span_along_y = max_y-min_y

            if span_along_x > span_along_y:
                div_point = (max_x+min_x)/2
                self.divide_x_axis(div_point)

                els_in_new_bucket = [point for point in elements if self.get_cell_no_using_xy(point[1], point[2]) == mapper_index]

                els_in_old_bucket = [point for point in elements if point not in els_in_new_bucket]

                new_filename = "{}-grid_bucket.txt".format(self.bucket_count+1)
                self.bucket_count +=1


                with open(new_filename, 'w') as opened_file:
                    for new_point in els_in_new_bucket:
                        opened_file.write("{} {} {}{}".format(new_point[0], new_point[1], new_point[2], '\n'))

                self.mapper[mapper_index][bucket] = new_filename
                self.mapper[mapper_index][num_of_els_in_cell] = len(els_in_new_bucket)
                self.mapper[mapper_index][elements_in_bucket] = len(els_in_new_bucket)

                with open(filename, 'w') as opened_file:
                    for old_point in els_in_old_bucket:
                        opened_file.write("{} {} {}{}".format(old_point[0], old_point[1], old_point[2], '\n'))

                self.mapper[mapper_index][num_of_els_in_cell] = len(els_in_old_bucket)
                self.mapper[mapper_index][elements_in_bucket] = len(els_in_old_bucket)

            else:
                div_point = (max_y+min_y)/2
                self.divide_y_axis(div_point)

                els_in_new_bucket = [point for point in elements if self.get_cell_no_using_xy(point[1], point[2]) == mapper_index]

                els_in_old_bucket = [point for point in elements if point not in els_in_new_bucket]

                new_filename = "{}-grid_bucket.txt".format(self.bucket_count+1)
                self.bucket_count +=1


                with open(new_filename, 'w') as opened_file:
                    for new_point in els_in_new_bucket:
                        opened_file.write("{} {} {}{}".format(new_point[0], new_point[1], new_point[2], '\n'))

                self.mapper[mapper_index + len(self.x_scale)][bucket] = new_filename
                self.mapper[mapper_index + len(self.x_scale)][num_of_els_in_cell] = len(els_in_new_bucket)
                self.mapper[mapper_index + len(self.x_scale)][elements_in_bucket] = len(els_in_new_bucket)

                with open(filename, 'w') as opened_file:
                    for old_point in els_in_old_bucket:
                        opened_file.write("{} {} {}{}".format(old_point[0], old_point[1], old_point[2], '\n'))

                self.mapper[mapper_index][num_of_els_in_cell] = len(els_in_old_bucket)
                self.mapper[mapper_index][elements_in_bucket] = len(els_in_old_bucket)









    def get_all_els_using_x_y(self, x, y):
        cell_no = self.get_cell_no(x,y)
        return self.get_all_els(cell_no)






    def get_all_els(self, cell_no):
        bucket, last_bucket, num_of_elem = 0,1,2

        filename = self.mapper[cell_no][bucket]
        print filename


        points=[]

        while(True):
            with open(filename) as myfile:
                elements = myfile.read().splitlines()

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

    def get_cell_no_using_xy(self, x, y):
        i,j = self.get_indices_of_2dcell(x, y)
        return self.get_cell_no(i, j)

    def get_cell_no(self, index_i, index_j):
		cell_no = (len(self.x_scale) * index_i) + index_j
		return cell_no












    def get_x_y_for_euclidian_dist(self, query_x, query_y, cell_i, cell_j):
                query_i, query_j = self.get_indices_of_2dcell(query_x, query_y)

		if query_i == cell_i:

		    if query_j < cell_j:
		        y_point=query_y
		        x_point=self.x_scale[cell_j-1];

		    elif query_j > cell_j:
		        x_point=self.x_scale[cell_j]
		        y_point=query_y

		elif query_j == cell_j:

		    if query_i > cell_i:
		        x_point=query_x
		        y_point=self.y_scale[cell_i]

		    elif query_i < cell_i:
		        x_point=query_x
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
    	query_i, query_j = self.get_indices_of_2dcell(query_x, query_y)

        cell_no = self.get_cell_no(query_i, query_j)
        filename = self.mapper[cell_no][0]

        self.file_access_record[filename]=1

        k_list = self.get_all_els(cell_no)

        temp_k_list = []
        '''
        for temp in k_list:
            if temp not in temp_k_list:
                temp_k_list.append(temp)

        k_list = temp_k_list
        '''
        bucket_access_count =0

        self.bucket_access_record[cell_no] =1

        bucket_access_count += math.ceil(self.mapper[cell_no][2]/float(self.bucket_size))

        cycle_no = 1

        while len(k_list) < k:
            cycle = self.cycle(query_x, query_y, cycle_no)

            if len(cycle) == 0:
                break

            for cell in cycle:
                if not self.file_access_record.has_key(self.mapper[cell[0]][0]):
                    k_list += self.get_all_els(cell[0])
                    self.bucket_access_record[cell[0]] =1

                    bucket_access_count += math.ceil(self.mapper[cell[0]][2]/float(self.bucket_size))
                    self.file_access_record[self.mapper[cell[0]][0]] =1

                if len(k_list) >= k:
                    break
            cycle_no += 1

        if len(k_list) < k:
            print "The grid does not contains k elements"
            k_list = self.get_euclidian_dist_for_list(query_x, query_y, k_list)
            return (k_list, bucket_access_count)

        k_list = self.get_euclidian_dist_for_list(query_x, query_y, k_list[0:k])

        return (k_list, bucket_access_count)





    def knn(self, k, x, y):
        self.bucket_access_record=[]

        for i in range(len(self.mapper)):
            self.bucket_access_record.append(0)

        k_list, bucket_access_count = self.find_first_k_elements(k, x, y)

        if len(k_list) < k:
            return (k_list, bucket_access_count)

    #-------------------------------------------------------------------


        cycle_no =1
        already_visited_cycle = False
        while(True):
            last_list = k_list
            cycle = self.cycle(x, y, cycle_no)
            if len(cycle) == 0:
                break

            for cell in cycle:
                if self.bucket_access_record[cell[0]] == 1:
                    already_visited_cycle = True
                    continue



                if cell[1] < k_list[k-1][3]:
                    self.bucket_access_record[cell[0]] =1

                    if not self.file_access_record.has_key(self.mapper[cell[0]][0]):
                        temp_list = self.get_all_els(cell[0])
                        temp_list = self.get_euclidian_dist_for_list(x, y, temp_list)
                        k_list += temp_list
                        k_list.sort(key = lambda x: x[3])
                        k_list = k_list[0:k]
                        bucket_access_count += math.ceil(self.mapper[cell[0]][2]/float(self.bucket_size))
                        self.file_access_record[self.mapper[cell[0]][0]] =1

            if last_list == k_list and already_visited_cycle is False:
                break

            already_visited_cycle = False

            cycle_no +=1

        return (k_list, bucket_access_count)









    ''' cycle returns a list of tuples [(cell_no, euclidean_dist),()...]
    takes input as x and y for query point and
    c for cycle no.

	'''

    def cycle(self, query_x, query_y, cycle_no):
	cycle = []

	index_i, index_j = self.get_indices_of_2dcell(query_x, query_y)
	cycle_cell_i, cycle_cell_j = index_i, index_j + cycle_no

        if cycle_cell_i in range(len(self.y_scale)) and cycle_cell_j in range(len(self.x_scale)):
    	    cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(query_x, query_y, cycle_cell_i, cycle_cell_j)

            euclidian_dist = self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
	    cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

	    cycle.append((cell_no, euclidian_dist))

	for i in range(1,cycle_no*8):
	    if i<=cycle_no:
	        cycle_cell_i -= 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
                    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(query_x, query_y, cycle_cell_i, cycle_cell_j)
		euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

	        cycle.append((cell_no, euclidian_dist))


	    elif i>cycle_no and i <= (3*cycle_no):
		cycle_cell_j -= 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue
		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(query_x, query_y, cycle_cell_i, cycle_cell_j)
		euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))

	    elif i > (3*cycle_no) and i <=  (5*cycle_no):
		cycle_cell_i += 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(query_x, query_y, cycle_cell_i, cycle_cell_j)
	        euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))

	    elif i > (5*cycle_no) and i <=  (7*cycle_no):
		cycle_cell_j += 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(query_x, query_y, cycle_cell_i, cycle_cell_j)
		euclidian_dist = self. get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))

	    elif i  > 7*cycle_no:
		cycle_cell_i -= 1

		if cycle_cell_i not in range(len(self.y_scale)) or cycle_cell_j not in range(len(self.x_scale)):
		    continue

		cycle_cell_x, cycle_cell_y = self.get_x_y_for_euclidian_dist(query_x, query_y, cycle_cell_i, cycle_cell_j)
		euclidian_dist =  self.get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
		cell_no = self.get_cell_no(cycle_cell_i, cycle_cell_j)

		cycle.append((cell_no, euclidian_dist))
	return cycle


class Mapper():
    def __init__(self):
        mapper=[]


grid = Grid()

def insert_into_array(grid, dataset_name):
	with open(dataset_name) as dataset_file:
		points = dataset_file.read().splitlines()
		points = [map(int, point.split(" ")) for point in points]

	for point in points:
		grid.insert(point[0], point[1], point[2])
                #print("inserting :",point[0])

        while True:
            choice = int(input("\n=> for knn press 1: \n=> for printing the data structure press 2: \n=> project related info press 3: \n=> exit 0: \n: "))

            if choice == 1:
                k = int(input("Enter k : "))
	        x = int(input("query x : "))
	        y = int(input("query y : "))
	        k_list, bucket_access = grid.knn(k, x, y)
                print k_list
	        print("Bucket access count: ", bucket_access)

            elif choice == 2:
                if len(grid.mapper) > 1000:
                    ch = int(input("data structure has more than 1000 value, print[1/0]: "))
                    if ch == 1:
                        print grid.mapper
                        
            elif choice == 3:
            	ac=0
				k=[5,20,50,100]
				for ki in k:
       				 for i in range(8):
              		 	x=randint(0,400)
                		y=randint(0,400)
                		klist,bac = grid.knn(ki,x,y)
                		ac+=bac
        			print ac/float(ki)


            else:
                return
dataset = input("Enter dataset name: ")
insert_into_array(grid, dataset)
