import random

from bmob import *
import json
bmob = Bmob("你的appid","你的rest key")

#获取数据
def get_chatlist():
    try:
        result = bmob.find(
            "你的表名"
            ,where=BmobQuerier().addWhereEqualTo("username","小王")
            ,limit=100).stringData
        data = json.loads(result)
        return data["results"]
    except Exception as e:
        print(e)
        return None

#插入数据
def insert_chatlist(data):
    try:
        bmob.insert("你的表名",data)
        return True
    except Exception as e:
        print(e)
        return False

#删除数据
def del_chatlist(objectId):
    try:
        bmob.remove("你的表名",objectId)
        return True
    except Exception as e:
        print(e)
        return False

#更新数据
def update_chatlist(objectId,data):
    try:
        bmob.update("你的表名",objectId,data)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    insert_chatlist({"username":"张三","value":"优秀"})

    rand = random.randint(1,1000)

    data = get_chatlist()
    if data is not None:
        print(data)

    del_chatlist("要删除的某条数据的objectId")

    update_chatlist("更新的某条数据的objectId",{"value":str(rand)})

