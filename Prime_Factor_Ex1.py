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

print(prime_factors(630))  # [2, 3, 3, 5, 7]
print(prime_factors(13))   # [13]