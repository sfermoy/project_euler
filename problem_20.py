
def factorial(n):
	totes=1
	for i in range(1,n+1):
		totes*=i
	return totes
		
#num -> string -> list_of_strings -> list_of_ints then sum
print sum(map(int,list(str(factorial(100)))))