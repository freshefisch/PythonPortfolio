#This is a very simple calculator made by @gurkenjaeger13 -> gurkenjaeger13.github.io
z = 1
x = float(input("Enter your number to start: "))
repeat = True
while repeat:
	if z > 1:
		print("\nThe result is:", x)
	z = z + 1
	print("\nWhat do you want to do (enter letter):")
	print("   1) Add")
	print("   2) Sub")
	print("   3) Mult")
	print("   4) Div")
	print("   0) End")
	action = int(input("   "))

	if action == 0:
	    repeat = False
	    print("\nThe endresult is:", x)

	elif action == 1:
	    y = float(input("Number to add: "))
	    x = x + y

	elif action == 2:
		y = float(input("Number to subsctract: "))
		x = x - y

	elif action == 3:
		y = float(input("Number to multiply by: "))
		x = x * y

	elif action == 4:
		y = float(input("Number to divide by: "))
		x = x / y
