fibs=[0,1,1]
def fib(n):
	#pdb.set_trace()
	if n <= (len(fibs)-1):
		return fibs[n]
	else:
		ans=fib(n-1)+fib(n-2)
		fibs.append(ans)
		return ans

x=12
while len(str(fib(x)))<1000:
	x+=1

print x