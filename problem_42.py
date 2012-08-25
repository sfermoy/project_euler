def file_to_list(file1):
	read= open(file1,"r")
	ls=read.readlines()
	read.close()
	input_string=""
	for s in ls:
		input_string+=s
	input_string=input_string.replace("\"","")
	return input_string.split(",")

def mk_triangle_num_dict(up_to):
  ls=[]
  for i in xrange(0,up_to+1):
    ls.append((.5*i*(i+1),True))
  return dict(ls)

def main():
  word_ls=file_to_list("prob_42_input.txt")
  word_ls.sort()
  i=0
  for word in word_ls:
    ans=0
    chars=list(word)
    for char in chars:
      ans+=ord(char)-64
    word_ls[i]=ans
    i+=1
  tri_num_dict=mk_triangle_num_dict(650)
  print [tri_num_dict.has_key(x) for x in word_ls].count(True)
  print sum([tri_num_dict.has_key(x) for x in word_ls])

if __name__ == '__main__':
  main()
