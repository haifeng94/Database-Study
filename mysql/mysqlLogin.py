#coding=utf-8
from Mysql_Python import Mysql_Python
from hashlib import sha1 #导入加密方法

#接受用户输入
name = input("请输入用户名：")
pwd = input("请输入密码：")

#对密码进行加密
s1 = sha1()
s1.update(pwd)
pwd2 = s1.hexdigest()

#根据用户名查询密码
sql = "select passwd from users where name=%s"
helper = Mysql_Python('localhost',3306,'python3','root','mysql')
result = helper.selectAll(sql,[name])

#验证
if len(result)==0:
	print('用户名错误')
elif result[0][0]==pwd2:
	print("登陆成功")
else:
	print('密码错误')	
#查询出来的结果(('123'),)