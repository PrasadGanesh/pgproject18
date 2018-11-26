import math

xmax=200
ymax=200

xcut = 40
ycut = 40

x_scale = range(40,200,40)+[200]
y_scale = range(40,200,40)+[200]




# this function gives indices for a point, of the cell it is in

def give_indices_of_2dcell(x, y, x_scale, y_scale):
    i=0;j=0
    while j < len(x_scale):
        if x <= x_scale[j]:
            break
        j+=1

    while i < len(y_scale):
        if y <= y_scale[i]:
            break
        i+=1

    return (i,j)







def get_cell_no(index_i, index_j, x_scale):
    cell_no = (len(x_scale) * index_i) + index_j
    return cell_no



def get_x_y_for_euclidian_dist(query_i, query_j, cell_i, cell_j, x_scale, y_scale):

    if query_i == cell_i:

        if query_j < cell_j:
            if cell_i == 0:
                y_point = y_scale[cell_i]/2
            else:
                y_point=(y_scale[cell_i-1]+y_scale[cell_i])/2
                x_point=x_scale[cell_j-1];

        elif query_j > cell_j:
            if cell_i == 0:
                y_point = y_scale[cell_i]/2
            else:
                x_point=x_scale[cell_j]
                y_point=(y_scale[cell_i-1] + y_scale[cell_i])/2

    elif query_j == cell_j:

        if query_i > cell_i:
            if cell_j == 0:
                x_point = x_scale[cell_j]/2
            else:
                x_point=(x_scale[cell_j]+x_scale[cell_j-1])/2
            y_point=y_scale[cell_i]

        elif query_i < cell_i:
            if cell_j == 0:
                x_point = x_scale[cell_j]/2
            else:
                x_point=(x_scale[cell_j]+x_scale[cell_j-1])/2
            y_point=y_scale[cell_i-1]

    elif query_i < cell_i:

        if query_j < cell_j:
            x_point = x_scale[cell_j-1]
            y_point = y_scale[cell_i-1]

        elif query_j > cell_j:
            x_point = x_scale[cell_j]
            y_point = y_scale[cell_i-1]

    elif query_i > cell_i:

        if query_j < cell_j:
            x_point = x_scale[cell_j-1]
            y_point = y_scale[cell_i]

        elif query_j > cell_j:
            x_point = x_scale[cell_j]
            y_point = y_scale[cell_i]
    return (x_point, y_point)



def get_euclidian_dist(query_x, query_y, data_x, data_y):
    return math.sqrt(math.pow((data_x-query_x),2) + math.pow((data_y-query_y),2))

''' cycle returns a list of tuples [(cell_no, euclidean_dist),()...]
    takes input as x and y for query point and
    c for cycle no.

'''
def cycle(query_x, query_y, cycle_no, x_scale, y_scale):
    cycle = []

    index_i, index_j = give_indices_of_2dcell(query_x, query_y, x_scale, y_scale)
    cycle_cell_i, cycle_cell_j = index_i, index_j + cycle_no

    if cycle_cell_i in range(len(y_scale)) and cycle_cell_j in range(len(x_scale)):
        cycle_cell_x, cycle_cell_y = get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j, x_scale, y_scale)

        euclidian_dist = get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
        cell_no = get_cell_no(cycle_cell_i, cycle_cell_j, x_scale)

        cycle.append((cell_no, euclidian_dist))

    for i in range(1,cycle_no*8):
        if i<=cycle_no:
            cycle_cell_i -= 1

            if cycle_cell_i not in range(len(y_scale)) or cycle_cell_j not in range(len(x_scale)):
                continue

            cycle_cell_x, cycle_cell_y = get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j, x_scale, y_scale)
            euclidian_dist =  get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
            cell_no = get_cell_no(cycle_cell_i, cycle_cell_j, x_scale)

            cycle.append((cell_no, euclidian_dist))


        elif i>cycle_no and i <= (3*cycle_no):
            cycle_cell_j -= 1

            if cycle_cell_i not in range(len(y_scale)) or cycle_cell_j not in range(len(x_scale)):
                continue
            cycle_cell_x, cycle_cell_y = get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j, x_scale, y_scale)
            euclidian_dist =  get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
            cell_no = get_cell_no(cycle_cell_i, cycle_cell_j, x_scale)

            print(cycle_cell_x, cycle_cell_y)
            cycle.append((cell_no, euclidian_dist))

        elif i > (3*cycle_no) and i <=  (5*cycle_no):
            cycle_cell_i += 1

            if cycle_cell_i not in range(len(y_scale)) or cycle_cell_j not in range(len(x_scale)):
                continue

            cycle_cell_x, cycle_cell_y = get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j, x_scale, y_scale)
            euclidian_dist =  get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
            cell_no = get_cell_no(cycle_cell_i, cycle_cell_j, x_scale)

            cycle.append((cell_no, euclidian_dist))

        elif i > (5*cycle_no) and i <=  (7*cycle_no):
            cycle_cell_j += 1

            if cycle_cell_i not in range(len(y_scale)) or cycle_cell_j not in range(len(x_scale)):
                continue

            cycle_cell_x, cycle_cell_y = get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j, x_scale, y_scale)
            euclidian_dist =  get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
            cell_no = get_cell_no(cycle_cell_i, cycle_cell_j, x_scale)

            cycle.append((cell_no, euclidian_dist))

        elif i  > 7*cycle_no:
            cycle_cell_i -= 1

            if cycle_cell_i not in range(len(y_scale)) or cycle_cell_j not in range(len(x_scale)):
                continue

            cycle_cell_x, cycle_cell_y = get_x_y_for_euclidian_dist(index_i, index_j, cycle_cell_i, cycle_cell_j, x_scale, y_scale)
            euclidian_dist =  get_euclidian_dist(query_x, query_y, cycle_cell_x, cycle_cell_y)
            cell_no = get_cell_no(cycle_cell_i, cycle_cell_j, x_scale)

            cycle.append((cell_no, euclidian_dist))
    return cycle




c = cycle(50,100,1, x_scale, y_scale)
print c
