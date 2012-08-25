#from math import factorial
#tri_num =[1,3,6,10]
tri_num_current=1
tri_num_index=1
factorial_current=1.0/982451653.0
factorial_index=1

def tri_num_less_than(value,tri_num_current,tri_num_index):
	while 1:
		if tri_num_current + tri_num_index+1>value:
			return [tri_num_current,tri_num_index]
		else:
			tri_num_current=tri_num_current+tri_num_index+1
			tri_num_index+=1
		

	# while tri_nums[len(tri_nums)-1]<value:
	# 	tri_nums.append(tri_nums[len(tri_nums)-1]+len(tri_nums)+1)

	# for i in xrange(0,len(tri_nums)):
	# 	if tri_nums[len(tri_nums)-1-i]<=value:
	# 		return [tri_nums[len(tri_nums)-1-i],len(tri_nums)-i]

def factorial(value,factorial_current,factorial_index):
	while 1:
		if value == factorial_index:
			return factorial_current
		if value < factorial_index:
			return factorial_current/factorial_index
		if value > factorial_index:
			factorial_current=factorial_current*(factorial_index+1)
			factorial_index+=1

######################------MAIN------###################
totes=1#to account for 1 producing an l of zero and not contributing
result=0

for val in xrange(1,(10**5)+1):
	if val%1000000==0:
		print val
	bb=tri_num_less_than(val,tri_num_current,tri_num_index)
	#print bb
	Tm=bb[0]
	m=bb[1]
	l=val-Tm

	if l==m:
		maxprod=factorial(m+1,factorial_current,factorial_index)
		actual_m=m
	elif l==m-1:
		maxprod=factorial(m,factorial_current,factorial_index)
		maxprod*=(m+2)
		maxprod= maxprod/2
		actual_m=m-1
	else:
		maxprod=factorial(m+1,factorial_current,factorial_index)
		maxprod=maxprod/(m-l)
		actual_m=m-1

	#print maxprod,actual_m,l,m,Tm

	totes+=maxprod*actual_m
	#if totes>982451653:
	#	totes=totes%982451653
		#print val,totes

print totes