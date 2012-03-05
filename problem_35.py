import time as t
import math
t1=t.time()

def primeflags(limit):
	flags=[1]*limit
	flags[0]=flags[1]=0	
	for n in range(2,int(math.sqrt(limit))+10):
		#should be sqrt
		if n*n>limit:
			return flags
		elif flags[n]==1:
			i=2
			while n*i<(limit-1):
				flags[n*i]=0
				i=i+1

def primes(limit):
	flags=primeflags(limit)
	primes=[]
	for n in range(0,len(flags)-1):
		if flags[n]==1:
			primes.append(n)
	return primes

def circular_primes(limit):
	lprimes=primes(limit)
	 # use a list comprehension to make dict
	dic=dict([(str(x),x)for x in lprimes])
	cprimes=["2"]
	#digits=["1","3","5","7","9"]
	for p in lprimes:
		s=str(p)
		ls=list(s)
		if check_digits(ls):
			continue	
		elif check_circles(ls,dic):
			continue
		else:
			cprimes.append(s)
	return cprimes

def check_digits(ls):
	for s in ls:
		if int(s)%2==0:
			return True
	return False

def check_circles(ls,dic):
	for k in range(0,len(ls)):
		key=""
		swap=ls.pop(0)
		ls.append(swap)
		for s in ls:
			key+=s
		if key not in dic:
			return True
	return False

def to_file(file_location,ls):
	f=open(file_location,"w")
	for s in ls:
		f.write(s+",")
	f.close()

circle=circular_primes(1000000)
t2=t.time()

print str(t2-t1),len(circle)
#to_file("/home/shane/Code/python/puzzle/project_euler/prob_35",circle)