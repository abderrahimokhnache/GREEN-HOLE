import sqlite3

class DBConnect:
	'''this class makes working with data base easy by taking all the heavy stuff'''

	def __init__(self,**kwargs):
		
		self.Data= kwargs
		
		self._db = sqlite3.connect(self.Data['FN'])
		
		self._db.row_factory = sqlite3.Row
		
		self._db.execute("CREATE TABLE IF NOT EXISTS {} {}".format(self.Data['TN'] , self.Data['TC']))
		
		self._db.commit()

	def Add(self,TN ,VL, Data):
	
		'''this method for inserting self.data into specific table'''
		
		self._db.execute('INSERT INTO {} VALUES {}'.format(TN,VL)
		 , (Data))
		
		self._db.commit()
		
		return "Saved"

	def Listrequest(self,**kwargs):

		'''this method returns the table as Dictionary '''
		
		cursor = self._db.execute('SELECT * FROM {} '.format(self.Data['TN']))
		
		return cursor

	def DeleteRecord(self,Table_Name,ID,item):
		
		'''this for deleting items '''
		
		self._db.execute('DELETE FROM {} WHERE {} = ? '.format(Table_Name,ID),(item,))
		
		self._db.commit()
		
		return'Deleted'

	def Listrequest2(self,Table_Name,ID,item):
		'''this method returns the specified item '''
		
		cursor2 = self._db.execute('SELECT * FROM {} WHERE {} = ? '.format(Table_Name,ID),(item,))
		
		return cursor2

	def Update(self,Table_Name , Column , VL1 , Column1 ,VL2):

		'''this method for updating items '''

		self._db.execute("UPDATE {} SET {} = ? WHERE {} = ? ".format(Table_Name , Column , Column1),(VL1 , VL2))

		self._db.commit()

