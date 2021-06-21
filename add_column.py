# Get the sum of all the columns in mat

mat = np.arange(1,26).reshape(5,5)
mat
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
       
mat.sum(axis=0)

# output
# array([55, 60, 65, 70, 75])
	   
	   
 