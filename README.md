# 获取application id和rest api key
注册[Bmob后端云](https://www.bmobapp.com)账号，通过认证之后，创建应用，获取application id 和rest api key

# 下载Bmob Python SDK文件
Bmob Python SDK文件下载地址：[bmob.py](./bmob.py) 
把SDK文件放到你创建的python工程里面。

# 引用Bmob Python SDK文件
```
from bmob import *
import json
```

# 初始化Bmob模块
```
bmob = Bmob("你的application id","你的rest api key")
```

# 往其中一个表中插入一条数据
```
try:
    bmob.insert("你的表名",{"username":"张三","value":"优秀"})
except Exception as e:
    print(e)
```

# 更多
更多用法，请参考demo中的例子。