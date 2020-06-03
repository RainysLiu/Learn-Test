import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
mydict2 = {"姓名": "刘", "其他": {'座右铭': "1314", '爱好': {'运动': ['篮球','足球']}}, "主页": "https://www.liu.com"}

mycol.insert_one(mydict2)
print(mycol)
dblist = myclient.list_database_names()
if "runoobdb" in dblist:
  print("数据库已经存在")
else:
    print("数据库不存在")

collist = mydb. list_collection_names()
if "sites" in collist:   # 判断 sites 集合是否存在
  print("集合已存在！")
else:
    print("集合不存在")
