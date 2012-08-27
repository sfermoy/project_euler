from numpy import *
mat= genfromtxt("prob_82_input.txt",delimiter=",")
#mat= genfromtxt("prob_82_test.txt")

def smallest_unvisited(values,visited):
	min_index=unravel_index(values.argmin(), values.shape)
	if visited[min_index[0],min_index[1]]>0:
		values[min_index[0],min_index[1]]=20**12
		return smallest_unvisited(values,visited)
	else:
		return [values,min_index]

def dikjstra(matrix,source):
	nrows=len(matrix)
	mcols=len(matrix[0])
	index=source
	tentitive=array([[10**12 for x in xrange(mcols)] for x in xrange(nrows)])
	result=array([[0 for x in xrange(mcols)] for x in xrange(nrows)])
	tentitive[index[0],index[1]]=matrix[index[0],index[1]]
	#itterate over the total number of elements in our vertix weight matrix
	for z in xrange((nrows*mcols)):
		#use source first then the smallest tentive node for every subsequent loop
		if z>0:
			tentitive,index=smallest_unvisited(tentitive,result)

		i=index[0]
		j=index[1]
		# rules for which nodes are connected
		if i==0:
			#down
			option=matrix[i+1,j]+tentitive[i,j]
			if option<tentitive[i+1,j]:
				tentitive[i+1,j]=option

		elif i==(nrows-1):
			#up
			option=matrix[i-1,j]+tentitive[i,j]
			if option<tentitive[i-1,j]:
				tentitive[i-1,j]=option

		else:
			#up
			option=matrix[i-1,j]+tentitive[i,j]
			if option<tentitive[i-1,j]:
				tentitive[i-1,j]=option
			
			#down
			option=matrix[i+1,j]+tentitive[i,j]
			if option<tentitive[i+1,j]:
				tentitive[i+1,j]=option

		if j<(mcols-1):
			#right
			option=matrix[i,j+1]+tentitive[i,j]
			if option<tentitive[i,j+1]:
				tentitive[i,j+1]=option

		matrix[i,j]=tentitive[i,j]
		result[i,j]=tentitive[i,j]
	
	return result

######main#############
minlist=[]
for x in xrange(len(mat)):
	b=array(mat)
	result=dikjstra(b,(x,0))
	last_column=result[:,len(mat)-1]
	minlist.append(min(last_column))

print min(minlist)



