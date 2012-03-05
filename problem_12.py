from math import sqrt

tri_number=0
count=0

while True:
	num_divisors=0
	count+=1
	tri_number+=count

	for i in range(1,int(sqrt(tri_number))+1):
		if tri_number%i==0:
			num_divisors+=2
			
	if num_divisors>=500:
		print tri_number,num_divisors
		break