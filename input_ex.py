import sys , os ,time

def input_ex(inputs):

	try:
	
		uir = input("{}".format(inputs))

		return uir	

	except KeyboardInterrupt:

		os.system("cls||clear")

		sys.exit()

	except SyntaxError :

		print("\n\xb0 [-] PLEASE PUT THE INPUT IN COTTION ! \n")
		
		time.sleep(3)

		os.system("cls||clear")

		input_ex(inputs)

	except NameError :

		print("\n\xb0 [-] PLEASE PUT THE INPUT IN COTTION ! \n")
				
		time.sleep(3)

		os.system("cls||clear")
	
		input_ex(inputs)

	except TypeError :

		print("\n\xb0 [-] INVALID INPUT ! \n")
			
		time.sleep(3)

		os.system("cls||clear")

		input_ex(inputs)

	except Exception :	
	
		print("\n\xb0 [-] INVALID INPUT ! \n")
			
		time.sleep(3)

		os.system("cls||clear")

		input_ex(inputs)
