def prime_factors(n):
	fact = []

	while n % 2 == 0:
		fact.append(2)
		n = n // 2
	
	div = 3
	while div <= n:
		if n % div == 0:
			fact.append(div)
			n = n // div
		else:
			div += 2
	return fact

print(prime_factors(630))
print(prime_factors(13))