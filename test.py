import randint from random

ac=0
k=[5,20,50,100]
for ki in k:
	for i in range(8):
		x=randint(0,400)
		y=randint(0,400)
		klist,bac = grid.knn(ki,x,y)
		ac+=bac
	print ac/float(ki)
