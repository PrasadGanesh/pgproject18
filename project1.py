import math

print("Start of the program")

###___Taking boundries of rectangele__###
x_bound_min, x_bound_max=0,100
y_bound_min, y_bound_max=0,100

##___take the width and height for bucket area from user___##
x_width=int(input("Enter width(x)"))
y_height=int(input("Enter height(y)"))

#create a mapper list to store all bucket name information.
max_bucket_x = int( x_bound_max/x_width )
max_bucket_y = int ( y_bound_max/y_height)
mapper=[[]]
first_bucket_index_=[[]]
mapper_id=-1
last_id=0
for i in range (0,x_bound_max,x_width):
    for j in range(0,y_bound_max,y_height):
        mapper_id=mapper_id+1
        #Create the number of bucket and store that bucket coordinate into mapper list
        mapper.insert(mapper_id,[i,i+x_width,j,j+y_height,last_id])
        first_bucket_index_.insert(mapper_id,[i,i+x_width,j,j+y_height,last_id])
        f=open(str(i)+str(i+x_width)+str(j)+str(j+y_height)+str(last_id)+".txt","w+")
        f.close()

print(mapper[23])
print(first_bucket_index_[12])
# read the point from file and enter into buckets.
def insert_into_bucket(id,x_crd,y_crd,max_bucket_x,max_bucket_y,x_width,y_height):
        x_temp = int ( x_crd / max_bucket_x )
        y_temp = int ( y_crd / max_bucket_y)
        #mapper_address = x_temp * max_bucket_y + y_temp
        #mapper_address = ((math.floor (x_crd/x_width)+1) * (math.floor (y_crd/y_height)+1))-1
        mapper_address =int( (((math.floor(x_crd/x_width)))* (100/x_width)) + math.floor(y_crd/y_height))
        print("mp",mapper_address,(math.ceil (x_crd/x_width)+1))
        print("Stored data into these files ",mapper[mapper_address])

        last_bit_of_add = str(mapper[mapper_address][4])
        #open mapper_address file and store that point into that fileself.
        thefilepath=str(mapper[mapper_address][0])+str(mapper[mapper_address][1])+str(mapper[mapper_address][2])+str(mapper[mapper_address][3])+str(last_bit_of_add)+".txt"

        with open(str(mapper[mapper_address][0])+str(mapper[mapper_address][1])+str(mapper[mapper_address][2])+str(mapper[mapper_address][3])+str(last_bit_of_add)+".txt","a") as created_bucket:
            count = 0
            for line in open(thefilepath).readlines(  ): count += 1
            print("Number of enteries in a bucket",count)

            if (bucket_size == count):
                mapper[mapper_address][4]=mapper[mapper_address][4]+1
                print("value in mapper last bit ",mapper[mapper_address][4])
                f=open(str(mapper[mapper_address][0])+str(mapper[mapper_address][1])+str(mapper[mapper_address][2])+str(mapper[mapper_address][3])+str(mapper[mapper_address][4])+".txt","w+")
                created_bucket.write(str(mapper[mapper_address][0])+str(mapper[mapper_address][1])+str(mapper[mapper_address][2])+str(mapper[mapper_address][3])+str(mapper[mapper_address][4]))
                created_bucket.close()
                f.close()
                insert_into_bucket(id,x_crd,y_crd,max_bucket_x,max_bucket_y,x_width,y_height)
                print("Hello Mom")

            #with open(thefilepath+"")
            elif (bucket_size>count):
                insert_value=str(id)+" "+str(x_crd)+" "+str(y_crd)
                created_bucket.write(insert_value+"\n")
                created_bucket.close()






###___HOME___###
with open("test_dataset.txt","r") as test_data:
    bucket_size=int (input("Enter the size of bucket"))
    for i in test_data:
        row = i.split(" ")
        id = row[0]
        x_crd=int(row[1])
        y_crd=int(row[2])
        insert_into_bucket(id,x_crd,y_crd,max_bucket_x,max_bucket_y,x_width,y_height)
#take input point from user.
id = input("Enter id")
x_crd = int(input("x coordinate"))
y_crd = int(input("y coordinate"))
insert_into_bucket(id,x_crd,y_crd,max_bucket_x,max_bucket_y,x_width,y_height)
print("Last Line")
