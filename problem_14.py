#Brute force should utalise memoization in chainLength


def chainLength(n):
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            length += 1
        else:
            n = (3 * n) + 1
            length += 1
    return length

maxChain = 0
maxChainNum = 0

for x in range(1, 1000000):
    l = chainLength(x)
    if l > maxChain:
        maxChain = l
        maxChainNum = x

print maxChain, maxChainNum
