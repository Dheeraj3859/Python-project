def showMenu():
	print('Menu: ')
	print("1. Add an item")
	print("2. mark as done")
	print("3 view items")
	print("4 exit")

user_input='random'
data = []
while user_input!='4':
	showMenu()
	user_input = input('Enter your choice ')
	if(user_input=='1'):
		item = input("What has to be done? ")
		data.append(item)
		print("Added item ", item)
	elif user_input=='2':
		item = input("What has to be marked as done ")
		if item in data:
			data.remove(item)
			print("removed item: ",item)
		else:
			print("item doesn't exist")
	elif user_input=='3':
		print("List of to do items are: ")
		for item in data:
			print(item)
	elif user_input=='4':
		print("bye")

