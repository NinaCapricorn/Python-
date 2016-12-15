# Python学习日志

## 1. **201612W2---抽奖概率统计**
```
 抽奖概率设计思想：
 * 场景1：根据奖品数量和设定的抽奖概率，执行相应次数的抽奖，对抽奖结果进行统计
 * 场景2：执行超出奖品数量的抽奖次数，对结果进行统计
 * 多次执行上述2中场景，计算其平均概率
```

### 知识点：
* cookies信息保存
```python
 import cookielib
 import urllib2
 cookie = cookielib.CookieJar()
 opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
 urllib2.install_opener(opener) 
```

* 模拟post请求
```
 1). 模拟post请求的时候，若data为空，也不能省略；以data={}的形式模拟post请求；
 2). urllib2.urlopen(req),其中req可以为基本url，也可是包含data数据的Request格式
```
 
```python
 import urllib2
 import urllib
 import json
 url = 'xxx'
 data = {} # dict
 post_data = urllib.urlencode(data)
 req = urllib2.Request(url, post_data)
 result = urllib2.urlopen(req)
 content = json.loads(result.read()) # json
```

* 概率统计：**for循环语句**

