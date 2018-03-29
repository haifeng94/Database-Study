#coding=utf-8
from Mysql_Python import Mysql_Python

name = input("请输入学生姓名：")
id2 = input("请输入学生编号：")

#修改
sql = 'update students set name=%s where id=%s'
params = [name,id2]
mysqlPython = Mysql_Python('localhost',3306,'python3','root','nicai')
mysqlPython.insertOrUpdate(sql,params)

#查询
sql = 'select id name from students where id<3'
mysqlPython = Mysql_Python('localhost',3306,'python3','root','nicai')
result = mysqlPython.selectAll(sql)
print (result)