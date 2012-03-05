#
def triangle_to_list(triangl_file):
	read= open(triangl_file,"r")
	ls=read.readlines()
	read.close()
	input_string=""
	for s in ls:
		input_string+=s
	return input_string.split()

def first_child_index(index):
	return index+depth(index)+1
	
def depth(index):
	totes=1
	i=0
	while totes<=index:
		i+=1
		totes+=i+1
	return i

def longest_path(graph):
	# For each node n in the graph in position [n][0] we have the value of each node.
	# In positinons [n][1] we wish to place the sum of the nodes traversed Which maxamize 
	# this value. To do this we set the children of n's second arguement equal to the sum 
	# of the nodes to n + the value of the child node if it is grater than the value 
	# currently contained in the second arguement. This is so that a child with more 
	# than one parent will only be overwritten by the parent with the longer sum. The 
	# result is the  second arguement of thelast row of the triangle contains the maximun
	# sum of the nodes traversed to.All nodes second arguments are inatilised to 0 with
	# the exception of the first which is inatilised to the nodes value, this is required 
	# since the first node has no parent an as such is not updated by the algorithm. The 
	# algorithm exits once a nodes child is reported as being outside the bounds of the
	# graph i.e. the first node of the last row of the triangle.
	graph[0][1]=graph[0][0]
	for i in range(0,len(graph)):
		child=first_child_index(i)
		if child>len(graph)-1:
			return graph 
		for c in range(child,child+2):#i.e range(0,3) =[0,1,2]
			if graph[c][1]<graph[i][1]+graph[c][0]:
				graph[c][1]=graph[c][0]+graph[i][1]
the_file="/home/shane/Code/python/puzzle/project_euler/prob_67_input"
my_graph=[[int(x),0] for x in triangle_to_list(the_file)]
longest_path(my_graph)
print max([my_graph[i][1] for i in range(0,len(my_graph))])