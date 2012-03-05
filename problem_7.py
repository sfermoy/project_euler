import math
def primeflags(limit):
	flags=[1]*limit
	flags[0]=flags[1]=0	
	for n in range(2,int(math.sqrt(limit))+10):
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

primels=primes(2000000)
print str(primels[10000])