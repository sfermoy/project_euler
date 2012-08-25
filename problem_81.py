from numpy import *
mat= genfromtxt("prob_81_input.txt",delimiter=",")
#print mat
#print mat[0,1]
#print len(matrix)

def dikjstraish(matrix):
	nrows=len(matrix)
	mcols=len(matrix[0])

	for row in range(nrows):
		#first row just one node flowing in
		if row==0:
			for col in range(1,mcols):
				matrix[row,col]=matrix[row,col]+matrix[row,col-1]
		#all other rows
		elif row>0:
			for col in range(mcols):
				#first entry in each row only has one node flowing in from above
				if col==0:
					matrix[row,col]=matrix[row,col]+matrix[row-1,col]
				else:
					option1=matrix[row,col]+matrix[row,col-1]
					option2=matrix[row,col]+matrix[row-1,col]
					matrix[row,col]=min(option1,option2)

	return matrix

out=dikjstraish(mat)
print out


