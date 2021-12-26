from hashlib import sha256

from subprocess import call as shell

import os , sys

from Fileop import File

from SQL import DBConnect

class LOG :

	def __init__(self, DFN):
			
		self.db = DBConnect(FN = '{}.db'.format(DFN), TN = 'USERS',TC = '(UN text, Password text , key text)')

		self.db.Add(TN = 'USERS', VL = '(?,?,?)',Data = ("Empty.","Empty.","Empty."))		
		
		# shell('attrib +h {}.db'.format(DFN))

	def Save(self , UN , getpw , key):	

		try :

			Password = sha256(getpw).hexdigest()

			self.db.Add(TN = 'USERS', VL = '(?,?,?)',Data = ( UN , Password ,key ))

			return '\n\xb1 NEW ACCOUNT HAS BEEN SAVED [\xfb]\n'

		except TypeError :

				print("\n\xb0 [-] SAVE INVALID INPUT ! \n")


	def Check(self, UN , getpw):
		
		try :
		
			Password = sha256(bytes(getpw , encoding ="UTF-8")).hexdigest()
		

			data = self.db.Listrequest(TN ='USERS')

			for row in data :

				if row['Password'] == "Empty." and row['UN'] == "Empty."  :

					return "Empty."

				if row['Password'] == Password and row['UN'] == UN :

					return True

				if not row['Password'] == Password :

					return False

				if  not row['UN'] == UN : 

					return False

		except TypeError as e :
			raise e 
			print(f"\n\xb0 [-] Password INVALID INPUT ! \n {e} ")
			
	
	def reset_key(self,UN , Old , New ):
		
		try:

			OLD_Password = sha256(Old.strip()).hexdigest()

			data = self.db.Listrequest(TN ='USERS')

			for row in data :
				
				if row['Password'] == OLD_Password :

					Code = sha256(New.strip()).hexdigest()

					self.db.Update('USERS', 'Password' , Code , 'UN' , UN )
					
					return "Done."

			
				elif not row['Password'] == OLD_Password :

					return False
		except TypeError :

				print("\n\xb0 [-] INVALID INPUT ! \n")


	def clear_key(self, PW):

		self.db.DeleteRecord('USERS' ,'Password' ,PW )
	
	def reset_account(self):

		data = self.db.Listrequest(TN ='USERS')

		for row in data :

			self.db.DeleteRecord('USERS' ,'Password' , row['Password'] )

			self.db.Add(TN = 'USERS', VL = '(?,?,?)',Data = ("Empty.","Empty.","Empty."))

	def inition():

		self.db.Add(TN = 'USERS', VL = '(?,?,?)',Data = ("Empty.","Empty.","Empty."))
