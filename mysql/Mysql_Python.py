#coding=utf-8

#python2为MySQLdb,python3为pymysql
from pymysql import * 

class Mysql_Python:
	def __init__(self,host,port,db,user,passwd,charset='utf8'):
		self.host = host
		self.port = port
		self.db = db
		self.user = user
		self.passwd = passwd
		self.charset = charset

	def open(self):
		self.conn = connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
		self.cursor = self.conn.cursor()

	def close(self):
		self.cursor.close()
		self.conn.close()

	#select
	def selectAll(self,sql,params=[]):
		try:
			self.open()

			self.cursor.execute(sql,params)
			result = self.cursor.fetchall()

			self.close()
			return result
		except Exception,e:
			print (e.message)

	#insert或update
	def insertOrUpdate(self,sql,params):
		try:
			self.open()

			self.cursor.execute(sql,params)
			self.conn.commit()

			self.close()
		except Exception,e:
			print(e.message)
			
	