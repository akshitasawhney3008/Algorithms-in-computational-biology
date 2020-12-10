# v = list of item values or profit
# w = list of item weight or cost
# W = max weight or max cost for the knapsack
def zeroOneKnapsack(v, w, W):
	# c is the cost matrix
	c = []
	n = len(v)
	c = zeros(n,W+1)
	for i in range(0,n):
		#for ever possible weight
		for j in range(0,W+1):
	                #can we add this item to this?
			if (w[i] > j):
				c[i][j] = c[i-1][j]
			else:
				c[i][j] = max(c[i-1][j],v[i] +c[i-1][j-w[i]])
	return [c[n-1][W], getUsedItems(w,c)]


def bestvalue(i, j):
    if i == 0: return 0
    value, weight = items[i - 1]
    if weight > j:
        return bestvalue(i - 1, j)
    else:
        return max(bestvalue(i - 1, j),
                   bestvalue(i - 1, j - weight) + value)


j = maxweight
result = []
for i in xrange(len(items), 0, -1):
    if bestvalue(i, j) != bestvalue(i - 1, j):
        result.append(items[i - 1])
        j -= items[i - 1][1]
result.reverse()
return bestvalue(len(items), maxweight), result