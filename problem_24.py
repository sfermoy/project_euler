import itertools

lex = list(itertools.permutations('0123456789'))
print "".join(lex[999999])
