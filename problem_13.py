read= open("/home/shane/Code/python/puzzle/project_euler/prob_13_input","r")
ls=read.readlines()
totes=0
for s in ls:
	totes+=int(s.strip())
read.close()
print str(totes)[:10]

