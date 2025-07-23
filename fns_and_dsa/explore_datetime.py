from datetime import datetime, timedelta

def display_current_datetime():
	current_date = datetime.now()
	formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
	print(f"Current Date and Time: {formatted_date}")

def calculate_future_datetime():
	try:
		days = int(input("Enter the number of days to add: "))
		current_date = datetime.now()
		future_date = current_date + timedelta(days=days)
		print(f"Future Date after {days} days: {future_date.strftime('%Y-%m-%d')}")
	except ValueError:
		print("Invalid input. Please enter a valid integer for days.")


display_current_datetime()
calculate_future_datetime()