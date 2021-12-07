from SQL import DBConnect

from Fileop import File

import os , sys ,time ,sqlite3 


from subprocess import call as shell

from Storage import Storage

from input_ex import input_ex

from login_db import LOG

from hashs import Hash_it

storage = Storage()

hash_it = Hash_it()

log = LOG('0')


def Help():

	time.sleep(1)

	print( '''
\
\xb0 -s -F_Store  : STORE FILES         \xb0 -d -Delete   : DELETE FILES 

\xb1 -f -F_Record : STORED FILES        \xb1 -e -Extract  : EXTRACT FILES
	
\xb1 -e -P_Store  : STORE PASSWORDS     \xb1 -Reset      : RESET PASSWORD

\xb2 -o -P_Record : STORED PASSWORDS    \xb2 -h -help     : HELP MESSAGE

	''')
					
def reset():

	os.system("cls||clear")

	UN = input_ex("\n\xb0 [?] USERNAME : ")	
	
	Old = input_ex("\n\xb0 [?] OLD PASSWORD : ")
	
	New = input_ex("\n\xb0 [?] NEW PASSWORD : ")

	chk_key = log.reset_key(UN , Old , New)

	if chk_key == False :

		reset()
	
	if chk_key == 'Done.':

		print ("\n\xb0 NEW PASSWORD HAS BEEN SAVED [\xfb]")

def menu():
	
	os.system("cls||clear")
	
	choice = input_ex( '''
\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2
\xb2    	                                               	 	 \xb2
\xb2 [\xfe] S : STORE FILES    [\xfe] O : PASSWORDS RECORD 	 	 \xb2
\xb2   	                                                         \xb2
\xb2 [\xfe] E : EXTRACT FILES  [\xfe] P : STORE PASSWORDS 	 	 \xb2
\xb2   	                                                         \xb2
\xb2 [\xfe] F : FILES RECORD   [\xfe] R : RESET PASSWORD 	 	 \xb2
\xb2   	                                                         \xb2
\xb2 [\xfe] D : DELETE         [\xfe] C : RESET ACCOUNT			 \xb2
\xb2   	                                                         \xb2
\xb2 [\xfe] Q : QUIT   	                                         \xb2            
\xb2   	                                                         \xb2
\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2\xb2

\xb0''')

	if choice.upper() == "S"  : storage.Store()
	
	elif choice.upper() == "E"  : storage.Extract()
	
	elif choice.upper() == "F"  : storage.Safe()

	elif choice.upper() == "P"  : 

		Memo = input_ex("\n\xb0 [?] MEMO : ")

		Password = input_ex("\n\xb0 [?] PASSWORD : ")

		print (storage.Passwords(Memo , Password))

	elif choice.upper() == "O"  : storage.Passwords_Safe()
	
	elif choice.upper() == "D"  : 
		
		user = input_ex("\n\xb0 [?] ALL \xb0 ONE : ")
		
		storage.Delete(user)

	elif choice.upper() == "R"  : reset()

	elif choice.upper() == "C"  : 
		
		log.reset_account()

		storage.Delete('*') 

		print ('\n\xb1 YOUR ACCOUNT HAS BEEN DELETED [\xfb]\n')

	elif choice.upper() == "Q"  : 

		os.system("cls||clear")

		sys.exit() 

	else :

		print('\n\xb2 INVALID INPUT [\xfe]')
		
		time.sleep(2)
		
		menu()


count = 1

def on_start(choice):
	
	global count

	os.system("cls||clear")

	UN = input_ex("\n\xb0 [?] USERNAME : ")	
	
	Password = input_ex("\n\xb0 [?] PASSWORD : ")
		
	chk = log.Check(UN = UN , getpw = Password )
	
	if count == 3 :

		os.system("cls||clear")

		print ("\n TRY LATER [!] ")

		time.sleep(3)

		sys.exit()

	if chk == "Empty." : 

		log.clear_key("Empty.")  
		
		print (log.Save( UN = UN ,getpw = Password  ,key = hash_it.get_key()))

		time.sleep(3)
		
		menu()

	if chk == True :
	
		if choice == 'safe' : storage.Safe()
		
		if choice == "Delete" : 
			
			user = input_ex("\n\xb0 [?] ALL \xb0 ONE : ")	
			
			storage.Delete(user)
		
		if choice == "Store" : storage.Store()
		
		if choice == "Ext" : storage.Extract()
		
		if choice == 'menu' : menu()
		
		if choice == 'Store_pw' : storage.Passwords()
		
		if choice == 'view_pw' : storage.Passwords_Safe()

	if chk == False :
	
		count += 1
	
		on_start(choice)
	

if __name__ == '__main__':

	if (len(sys.argv) > 1) :

		if sys.argv[1].lower() == "-f" or sys.argv[1].lower() == "-f_record" : on_start('safe') 
		
		elif sys.argv[1].lower() == "-d" or sys.argv[1].lower() == "-delete" : on_start('Delete') 	
	
		elif sys.argv[1].lower() == "-s" or sys.argv[1].lower() == "-f_store" : on_start('Store') 
		
		elif sys.argv[1].lower() == "-e" or sys.argv[1].lower() == "-extract" : on_start('Ext') 	
	
		elif sys.argv[1].lower() == "-e" or sys.argv[1].lower() == "-p_store" : on_start('Store_pw') 
		
		elif sys.argv[1].lower() == "-o" or sys.argv[1].lower() == "-p_record" : on_start('view_pw') 	
			
		elif sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "-help"  : Help() 	
	
		elif sys.argv[1].lower() == "-Reset" : reset()

		else : 
			
			print('\n\xb2 INVALID INPUT [\xfe]')
			
			Help()				

	else :

		on_start('menu')

