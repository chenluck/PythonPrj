import requests
import re
import pandas as pd
keyword='sun'
urlop=requests.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&1m=-1&c1=2&nc=1&ie=utf-8&word='+keyword)
pattern='"objURL":"(.+?)"'
s2=re.findall(pattern,urlop.text)
s2p=pd.Series(s2)
num=0
for num in s2p.index:
      a=requests.get(s2p[num]).content
      with open('img/%s.jpg'&str(num+1),'wb') as f:
            f.write(a)
            print("Downloading:",s2p[num])
      num+=1
