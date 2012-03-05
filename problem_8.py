read= open("/home/shane/Code/python/puzzle/project_euler/prob_8_input","r")
ls=read.readlines()
read.close()
totes=""
for s in ls:
	totes+=s.strip()

def consecutive_sum_generator(numdigits,number):
	ls=map(int,list(str(number)))
	for i in range(0,len(ls)-numdigits-1):
		total=1
		for d in range(i,i+numdigits):
			total*=ls[d]
		yield total


print max(consecutive_sum_generator(5,totes))

