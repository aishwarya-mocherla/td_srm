from random import randint


number = input("please type 'roll' to roll the dies: ")

while number == "roll":
	no = randint(1,6)

	if no == 1:
	
		print("|   |")
		print("| o |")
		print("|   |")
		
	if no == 2:
	
		print("| o |")
		print("|   |")        
		print("| o |")
	
	if no == 3:
		
		print("|   |")
		print("|ooo|")
		print("|   |")
		
	if no == 4:
		
		print("|o o|")
		print("|   |")
		print("|o o|")
		
	if no == 5:
		
		print("|o o|")
		print("| o |")
		print("|o o|")

	if no == 6:
		
		print("|ooo|")
		print("|   |")
		print("|ooo|")

		
	number=input("press roll to roll again or any other key to end:")
	
