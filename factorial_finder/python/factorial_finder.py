def factorial_finder(number):
	if number == 1:
		return number
	else:
		return number * factorial_finder(number - 1)

print(factorial_finder(10))