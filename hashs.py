from cryptography.fernet import Fernet

import os ,zlib ,Fileop as File , sqlite3

class Hash_it :

	def __init__(self) :

		try:
	
			cursor = sqlite3.connect('static/0.db')

			cursor.row_factory = sqlite3.Row


			Data_row = cursor.execute('SELECT * FROM USERS ')

			for row in Data_row : 

					self.f = Fernet(bytes(row['key'])) 

		except sqlite3.OperationalError :

			pass

		except TypeError :

			pass

	def encrypt(self , Code):

		compressed = zlib.compress(Code,9)
		
		Data = self.f.encrypt(compressed) 

		return Data

	def decrypt(self , Code):
		
		decrypted = self.f.decrypt(Code)
		
		Data = zlib.decompress(decrypted)

		return Data

	def en_f(self , Path):

		Code = File.File(Path = Path , Mode = "rb" )

		compressed = zlib.compress(Code,9)
		
		Data = self.f.encrypt(compressed) 

		return Data

	def de_f(self , Path):

		Code = File.File(Path = Path , Mode = "rb" )
		
		decrypted = self.f.decrypt(Code)

		Data =  zlib.decompress(decrypted)
		
		return Data

	def get_key(self , ):

		"""this function gets the key Encrtyption and Decryption"""
		
		return Fernet.generate_key()
