def prime_factors(n):
	fact = []
	div = 2
	while div <= n:
		if n % div == 0:
			fact.append(div)
			n = n // div
		else:
			div += 1
	
	return fact
