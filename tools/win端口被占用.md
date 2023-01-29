```shell
netstat -aon|findstr "443"  #查看443端口占用情况
tasklist|findstr "4452"  #查看pid为4452的软件名称
taskkill /f /t /im vmware-hostd.exe #关闭软件名为vmware-hostd.exe的进程
```