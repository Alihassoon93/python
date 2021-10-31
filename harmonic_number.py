def hnum(n):

	if n == 1:
		return 1
	else:
		return hnum(n-1) + 1/n

print(round(hnum(8),5))
