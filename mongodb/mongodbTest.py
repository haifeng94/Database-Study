#coding=utf-8
from pymongo import *

#获得客户端，建立连接
client = MongoClient('mongodb://python3:123@localhost:27017/python3')

#切换数据库
db = client.python3

#获取集合
stu = db.student

#增加
s1 = stu.insert_one({'name':'小明'})

#修改
stu.update_one({"name":'小明'},{'$set':{'name':'234'}})

#删除
stu.delete_one({'name':"234"})

#查询
s2 = stu.find({'age':{'$gt':20}}).sort({'_id',-1}).skip(1).limit(1)
for s in s2:
	print(s['name'])