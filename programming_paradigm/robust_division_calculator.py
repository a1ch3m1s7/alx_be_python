def safe_divide(numerator, denominator):
	try:
		# Attempt division
		result = float(numerator) / float(denominator)
		return f"Result: {result}"

	except ZeroDivisionError:
		return "Error: Division by zero is not allowed."

	except ValueError:
		return "Error: Please enter numeric values only."