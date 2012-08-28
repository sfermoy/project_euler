from numpy import *

row_mat= genfromtxt("prob_11_input.txt")
column_mat=rot90(row_mat.copy(),1)

up_diagonal=row_mat.copy()
dn_diagonal=row_mat.copy()
for y in xrange(len(row_mat)):
	 up_diagonal[y]=roll(up_diagonal[y],y)
	 dn_diagonal[y]=roll(dn_diagonal[y],len(row_mat)-y)
up_diagonal=rot90(up_diagonal,1)
dn_diagonal=rot90(dn_diagonal,1)

result=[]
for i in xrange(len(row_mat)-4):
	result.append(max(map(prod,row_mat    [:,i:i+4])))
	result.append(max(map(prod,column_mat [:,i:i+4])))
	result.append(max(map(prod,up_diagonal[:,i:i+4])))
	result.append(max(map(prod,dn_diagonal[:,i:i+4])))
print max(result)

