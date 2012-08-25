def file_to_list(file1):
	read= open(file1,"r")
	ls=read.readlines()
	read.close()
	input_string=""
	for s in ls:
		input_string+=s
	input_string=input_string.replace("\"","")
	return input_string.split(",")

def main():
  name_ls=file_to_list("prob_22_input.txt")
  name_ls.sort()
  i=1
  for name in name_ls:
    #print name
    ans=0
    chars=list(name)
    for char in chars:
      ans+=ord(char)-64
    name_ls[i-1]=ans*i
    i+=1
  print sum(name_ls)

if __name__ == '__main__':
  main()
