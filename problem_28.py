current=1
ans=1
space=0
while current<1001**2:
	space+=2
	for i in xrange(1,5):
		current+=space
		ans+=current
print ans