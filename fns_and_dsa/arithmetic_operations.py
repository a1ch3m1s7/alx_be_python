def perform_operation(num1, num2, operation):
	# define arithmetic operations.
	if operation == 'add':
	        return num1 + num2
	    elif operation == 'subtract':
	        return num1 - num2
	    elif operation == 'multiply':
	        return num1 * num2
	    elif operation == 'divide':
	        if num2 == 0:
	            return 'DIVISION_BY_ZERO'  # Recognizable flag for main.py
	        return num1 / num2
	    else:
	        return 'INVALID_OPERATION'  # Optional: handle unknown operations