# 系统安全配置类
用途|命令
-|-
查看开放端口|`netstat -anpt`
关闭所有进程、指定进程|`kill -9 -1` `kill -9 -1111(是pid不是端口号)`
将用户添加到组|`usermod userName -a -G groupName`
将用户从组删除|`gpasswd -d userName groupName`
查看可以ssh登录的用户|`cat /etc/passwd|grep sh$`
查看在adm组中的用户|`cat /etc/group|grep ^adm`


# 杂项技巧
用途|命令
-|-
统计文件行数、字数、字节数|`wc -l -w -c 1.txt`