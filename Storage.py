from SQL import DBConnect
from Fileop import File , more
import os.path , sys , time , sqlite3 , os
from subprocess import call as shell
from input_ex import input_ex
from hashs import Hash_it
from datetime import datetime

hash_it = Hash_it()
current_time = datetime.today()
message = '{:%A-%B-%d-%Y}'
current_time = message.format(current_time)

class Storage : 

	def __init__(self):

		self.db = DBConnect(FN = 'static/Account0.db', TN = 'FILES',TC = '(File_Name text,Content varchr,Dir text,DN text ,time text)')

		self.db2 = DBConnect(FN = 'static/Account0.db', TN = 'Passwords',TC = '(Memo text,Password varchar)')
		
		# shell('attrib +h  static/Account0.db')
		# shell('static/Account0.db')
	def Passwords(self,Memo ,Password) :
	
		self.db2.Add(TN = 'Passwords', VL = '(?,?)',Data = ( Memo,Password ))


		os.system("cls||clear")

		time.sleep(0.5)

		print( "\n\xb0 NEW PASSWORD HAS SAVED [\xfb] \n ")

	def Passwords_Safe(self):

		self.db2 = sqlite3.connect("static/Account0.db")

		self.db2.row_factory = sqlite3.Row

		data = self.db2.execute('SELECT * FROM Passwords')

		count = 1

		os.system("cls||clear")

		time.sleep(0.5)

		for row in data:

				show = "\n\xb0 [{}]  MEMO : {} | PASSWORD : {} \n"

				print (show.format( str(count).zfill(2) , row["Memo"]  , row["Password"] ))

				count += 1 

		if count == 1 :

			print ('\n [-] THE DATABASE IS EMPTY.')
		

	def Store(self):

		os.system("cls||clear")

		time.sleep(0.5)

		try:

			choice = input_ex("\n\xb0 [?] FOLDER \xb1 FILE : ")

			if choice.lower() == "file" :
			
				Path = input_ex('\n [?] Path : ')

				Data = hash_it.en_f(Path = Path)

				S_F_Path = os.path.split(Path)

				self.db.Add(TN = 'FILES', VL = '(?,?,?,?,?)',Data = (S_F_Path[1],Data, False , False , current_time))

				print ("\n\xb0 %s | HAS BEEN SAVED [\xfb] \n" % (S_F_Path[1]))
			
			if choice.lower() == "folder" :

				Dir = input_ex('\n [?] Path : ')

				for n , file in enumerate(os.listdir(Dir)) :

					if os.path.isdir(file) == False :

						Data = File(Path = Dir +'/'+ file ,Mode = "rb")

						Data_input = hash_it.encrypt(Data)

						S_F_Path = os.path.split(file) 

						dir_name = os.path.dirname(Dir +"\\"+ file).split('\\')

						self.db.Add(TN = 'FILES',VL = '(?,?,?,?,?)', Data = (S_F_Path[1],Data_input,True,dir_name[-1] , current_time ))
						
						show =  ("\n \xb2 [{}] \xb1  File Name : {} | Folder : {} | has been Saved [\xfb] \n")
						
						print (show.format( str(n).zfill(2) , S_F_Path[1] ,dir_name[-1] ))
				
		except WindowsError :

			os.system("cls||clear")

			time.sleep(0.5)

			print ("\n\xb0 [!] WindowsError, TRY TO MOVE THE FILES TO A DIFFERENT LOCATION.")
		
		except IOError :

			os.system("cls||clear")

			time.sleep(0.5)

			print( "\n\xb0 [!] THE FILE IS NOT READABLE.")


	def Extract(self):

		choice = input_ex("\n\xb0 [?] ALL \xb1 ONE \xb1 FOLDER : ")

		count = 1
			
		if choice.lower() == "one" :

			FN =input_ex( '\n\xb0 [?] FILE NAME  : ')
	
			data = self.db.Listrequest2('FILES' ,'File_Name' , FN )

			for row in data:
				
				Data_output = hash_it.decrypt(bytes(row['Content']))

				File(Path = FN ,Mode = "wb" , Content = Data_output)
				
				os.system("cls||clear")

				time.sleep(0.5)

				show = "\n\xb0 [{}] {} | Folder : {} | has been Extracted [\xfb] "

				print (show.format(str(count).zfill(2), row['File_Name'] , row['DN'] ))

				count += 1

			if count == 1 :	

				print( '\n\xb0 [-] NameError. or The DataBase is Empty.')


		elif choice == "*" or choice.lower() == 'all' : 
			
			os.system("cls||clear")

			time.sleep(0.5)

			data = self.db.Listrequest(TN ='FILES')
		
			for row in data:
				
				if int(row["Dir"]) == True :

					if os.path.exists(row['DN']) == False :

						os.mkdir(row["DN"])

					Data_output = hash_it.decrypt(bytes(row['Content']))

					File(Path = row['DN'] +'\\' + row['File_Name'] ,Mode = "wb" , Content = Data_output)

					show = ('\n [{}] {}  | FOLDER : {} | HAS BEEN EXTRACTED [\xfb] ')

					print( show.format(str(count).zfill(2) ,row['File_Name'],row['DN']))

					count +=1


				if int(row['Dir']) == False :

					Data_output = hash_it.decrypt(bytes(row['Content']))

					File(Path = row['File_Name'] ,Mode = "wb" , Content = Data_output)

					show = ('\n [{}] {} | FOLDER : {} | HAS BEEN EXTRACTED [\xfb] ')

					print( show.format(str(count).zfill(2),row['File_Name'],row['DN']))

					count += 1

			if count == 1 :	

				print ('\n\xb0 [-] THE DATABASE IS EMPTY.')


	def Safe(self):

		os.system("cls||clear")

		time.sleep(0.5)

		data = self.db.Listrequest(TN ='FILES')

		count = 1

		Files = []

		for  row in data:

				show =  ("\n \xb2 [{}] \xb1  FILE NAME : {} | FOLDER : {} | STORING DATE : {} ")
				
				finel = show.format(str(count).zfill(2),row["File_Name"] , row['DN'] , row['time'])

				Files.append(finel)

				count += 1
	
		for line in Files :

			with open('handler.sys' , "a") as file :
				
				file.write(line)

		more(Path = 'handler.sys' )
	
	
		if count == 1 :	

			os.system('cls||clear')

			print( '\n\xb0 [-] THE DATABASE IS EMPTY.')
		

	def Delete(self ,choice):

		os.system("cls||clear")

		time.sleep(0.5)

		count = 1

		if choice.lower() == 'one' :

			FN = input_ex( '\n\xb0 [?] File Name : ')
			
			self.db.DeleteRecord('FILES' ,'File_Name' , FN )
			
			print ('\n\xb0  %s | HAS BEEN DELETED [\xfb]' % (FN))
			
			count +=1


			
		if choice.lower() == 'all' or choice == "*" :

			data = self.db.Listrequest(TN ='FILES')
			
			for row in data :

				self.db.DeleteRecord('FILES' ,'File_Name' ,row['File_Name'] )

				show = '\n\xb0 [{}] {} | HAS BEEN DELETED [\xfb]' 

				print (show.format( str(count).zfill(2) , row['File_Name']) )

				count +=1 

		if count == 1 :	
				
				os.system("cls||clear")

				time.sleep(0.5)

				print ('\n\xb0 [-] THE DATABASE IS EMPTY.')


		# elif choice.lower() == 'folder' : 
			
		# 	os.system("cls||clear")

		# 	time.sleep(0.5)

		# 	data = self.db.Listrequest(TN ='FILES')
		
		# 	for row in data:
			
		# 		FN =input_ex( '\n\xb0 [?] FILE NAME  : ')	

		# 		if row['Dir'] == FN :

		# 			if os.path.exists(row['DN']) == False :

		# 				os.mkdir(row["DN"])

		# 			Data_output = hash_it.decrypt(bytes(row['Content']))

		# 			File(Path = row['DN'] +'\\' + row['File_Name'] ,Mode = "wb" , Content = Data_output)

		# 			show = ('\n [{}] {}  | FOLDER : {} | HAS BEEN EXTRACTED [\xfb] ')

		# 			print show.format(str(count).zfill(2) ,row['File_Name'],row['DN'])

		# 			count +=1