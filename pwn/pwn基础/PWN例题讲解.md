
## 基础部分

### ELF文件

ELF文件有三种类型，可以通过ELF Header中的 e_type 成员进行区分：

**可重定位文件（Relocatable File）**：ETL_REL。一般为.o文件，可以与其他目标文件链接来创建可执行文件或共享目标文件的代码和数据。静态链接库属于可重定位文件

**可执行文件（Executable File）**：ET_EXEC。可以执行的一个程序，此文件规定了exec()如何创建一个程序的进程映像。

**共享目标文件（Shared Object File）**：ET_DYN。一般为.so文件。

### 动态链接和静态链接

链接可以分为静态链接和动态链接俩种。gcc默认使用动态链接，添加“-static”即可指定为静态链接。这一阶段将目标文件及其依赖库进行链接，生成可执行文件，主要包括地址和空间分配，符号绑定和重定位等操作。

linux下动态链接文件 .so            静态链接文件 .a
ida打开动态链接文件function里粉色的函数只是一个符号，并没有函数具体实现,符号去解析动态链接库里的函数
ida打开的静态链接function的函数都有函数体实现,并且函数有父函数的实现

```sh
gcc -fno-pie test.o -o test -static  静态链接，并且关掉pie
gcc -fno-pie -o dytest test.c  动态链接,并且关掉pie
```

### 部分寄存器的功能

**32位架构下寄存器功能**
EIP
存放当前执行的指令的地址
ESP
存放当前栈帧的栈顶地址
EBP
存放当前栈帧的栈底地址
EAX
通用寄存器。存放函数返回值
EBX
"基地址"(base)寄存器, 在内存寻址时存放基地址。
ECX
计数器(counter), 是重复(REP)前缀指令和LOOP指令的内定计数器。
ESI/EDI
分别叫做"源/目标索引寄存器"(source/destination index),因为在很多字符串操作指令中, DS:ESI指向源串,而ES:EDI指向目标串.


### 常用的汇编指令

| 指令 | 等同于 |
| ---- | ------ |
|call func|	push pc，jmp func|
|leave|	mov esp ebp，pop ebp|
|ret|	pop pc (相当于在栈顶弹出一个数据赋值给EIP寄存器)|
|push xxx|	将xxx压栈，将esp减4|
|pop rdi|	弹栈，将此时esp所指内容存入rdi，同时esp加4|

### 栈的工作方式

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628430507602.png)

### linux的保护机制

RELRO: Full RELRO – 重定向，RELRO会有Partial RELRO和FULL RELRO，如果开启FULL RELRO，意味着我们无法修改got表
Stack: No canary found – 栈canary检查
NX: NX enabled – 栈不可执行
PIE: PIE enabled – 程序地址随机化
ASLR：Address space layout randomization - 内存地址随机化

## 工具使用

### gdb的使用

vmmap：查看虚拟内存空间
break：下断点
del：删除断点
run：运行整个程序
continue：继续运行
start：和b main，然后run差不多
n：单步步过
s：单步步入
ni：单步步过，汇编层面
si：单步步入，汇编层面
bt：栈回溯
x：查看内存
x/nfu <addr>

- n,f,u都是可选参数，指要显示的内存的格式
- n 代表个数，要显示多少单位的内存
- u 代表单位大小，b 表示单字节，h代表双字节，w表示四字节，g表示八字节
- x	代表显示格式，常用的格式有 x十六进制，s字符串，i机器指令，c字符型

info：查看一些信息
- info b查看断点信息
- info r查看寄存器信息
- info threads查看线程信息

disass：反汇编
- disass <func> 反汇编指定函数
- disass <addr> 反汇编指定地址
- disass <addr_begin> <addr_end> 反汇编指定地址范围

fin：结束此函数，返回上一层
p：打印一些值
- p $esp 打印寄存器的值
- p <addr> 打印地址里面的值
attach：附加进程


### pwntools的使用

导入pwnlib库
```py
from pwn import *
```

打开与本地程序的交互
```py
io = process("./test")
```

打开与远程指定程序的交互
```py
io = remote("xxxx",8888)
```

打开debug调试模式，显示交互中的输入与输出
```py
context.log_level = "debug"
```

设置操作系统
```py
context.os = "linux"
```

指定32位交互程序的体系架构
```py
context.arch = "i386"
```

指定64位交互程序的体系架构
```py
context.arch = "amd64"
```

接收所有字符流输出
```py
io.recv()
```

接收程序的一行字符流输出
```py
io.recvline()
```

接收程序的字符流直到str字符
```py
io.recvuntil("str")
```

发送payload
```py
io.send(payload)
```

发送payload并在结尾加上"\n"
```py
io.sendline(payload)
```

直到接收到str，然后发送payload
```py
io.sendafter("str",payload)
```

直到接收到str，然后发送payload,并在payload结尾加上"\n"
```py
io.sendlineafter("str",payload)
```

关闭io

```py
io.close()
```

用户交互
```py
io.interactive()
```

首先先创建一个ELF对象，方便我们对齐数据进行查找
```py
elf = ELF('test')
```

输出一个sh的shellcode 汇编代码 默认是32位的shellcode
```py
shellcraft.sh()
```

输出一段sh的shellcode的机器码
```py
asm(shellcraft.sh())
```

输出一个sh的shellcode 汇编代码 amd64位的shellcode  记得加上64位环境说明 context.arch
```py
shellcraft.amd64.sh()
```

ljust是左对齐，shellcode后面用A来填充垃圾数据，一共形成112个字节的字节流
```py
payload = asm(shellcraft.sh()).ljust(112,b'A')+p32(buf_addr)
```

搜索一个字符串并返回其所在地址 python3里字符串前面必须加上b''，不然找的就是str对象,而不是字节数据
```py
hex(next(elf.search(b'/bin/sh')))
```

查看puts函数在got表中表项的地址
```py
hex(elf.got["puts"])
```

变量名和函数名本质上都是符号，下面是查找gets函数的plt表地址，got表地址和buf2变量的地址
```py
elf.plt['gets']
elf.got['gets']
elf.symbols['buf2']
```

生成60个字节的垃圾数据
```py
cyclic(60)
```

如果想在pwntools中某一位置在pwndbg中调试，可以在pwntools中的这一位置`pause()`,然后执行到这里的程序就被挂起到了进程，gdb进入，attach pid 就可以在pwndbg中进行调试
```py
pause()
```

### checksec的使用

```shell
file test		查看二进制程序的架构
checksec test	检查二进制程序的保护
```

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628323248278.png)

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628323245329.png)

### ROPgadget的使用

```shell
ROPgadget --binary xxx --only "pop|ret"		//查找pop和ret的gadget片段
ROPgadget --binary xxx --string "/bin/sh"	//查找/bin/sh字符串
```

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628323240519.jpeg)

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628323237039.png)

### one_gadget的使用

```shell
one_gadget /lib32/libc-2.23.so
```

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628323230613.jpeg)

### ropper的使用

```shell
$ ropper
$ help
$ search pop rdi
```

### patchelf的使用

```shell
patchelf --set-interpreter ~/lib/2.23-0ubuntu3_i386/ld-2.23.so ./test
patchelf --replace-needed libc.so.6 ~/lib/2.23-0ubuntu3_i386/libc-2.23.so ./test
```

## 攻击方式部分

### ret2text

ida32 打开程序观察main函数，发现main函数中调用了vulnerable函数，vulnerable函数中又调用了gets函数，这个gets是读入数据，没有大小限制。由此可以知道这里是溢出点

![heap_2021-08-09_08-46-23](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557127798.png)

观察左侧的函数窗口，发现有一个叫backdoor的函数，发现是后门函数。后门程序直接调用了system("/bin/sh")，这个system("/bin/sh")相当于在终端中输入"/bin/sh"，所以能够获得shell。如果我们能将程序的执行流控制，并且让执行流执行这个backdoor函数，那我们就攻击成功了。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557124198.png)

gdb调试demo32程序，运行到gets函数，我们输入"AAAA"，然后观察栈上的分布。手动计算发现eax到ret_addr的距离是44字节

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557120926.png)

我们这一次输入44字节的垃圾数据，观察栈上的分布，发现我们输入的垃圾数据下一个字长就是ret_addr

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557117021.png)

我们再一次输入44字节的垃圾数据填充前面，然后再输入4字节的字符串"dead"作为标识，观察ret时返回的地址

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557113318.png)

我们发现ret时就是dead字符串的ascii形成的地址

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557108555.png)

接着执行发现程序崩溃了，这是肯定的，因为我们输入的"dead"形成ascii地址不是一个有效的地址，所以会崩溃。我们预想如果在ret_addr处覆写成为backdoor的地址，那么我们就可以拿到shell了。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557104199.png)

这一次我们输入44字节的垃圾数据，加上一个字长的backdoor函数的地址，观察栈上的分布

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557099760.png)

执行后发现ret返回的地址就是backdoor函数的起始位置，接着执行肯定能拿到shell。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557095896.png)

脚本攻击成功。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557092675.png)

这只是本地成功了，真正的CTF题目会给你的ip地址和port号，以便我们攻击远程。如果我们想在本地模拟攻击远程的话

```shell
socat tcp-l:8887,fork exec:./demo32
```

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557088237.png)

攻击成功

### ret2syscall



ida32 打开demo32程序，进入main函数查看还是调用了vulnerable函数，gets函数还是漏洞溢出点，观察左侧的函数窗口发现没有了backdoor函数

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557083899.png)

有一个sys函数，双击进入观察发现，system("ls")函数相当于只是在终端中执行了ls，列出目录文件，好像对我们的攻击起不到任何帮助

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557080515.png)

我们在string窗口发现了，sh字符串，结合刚刚的system("ls")，不难想到也许构造成功system("sh")也可以拿到shell

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557075901.png)

这里我们知道了栈空间的分布情况后，发现"ls"字符串地址现在是栈顶处。也就是说栈空间分布中，大多数函数的参数是分布在栈上的，只要我们能够修改这个参数，将其修改为我们找到的"sh"字符串的地址，我们就能够执行system("sh")，其效果和system("/bin/sh")是一样的。

set $pc=xxxx

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557072269.png)

执行完call指令之后我们发现，call指令的下一条指令的地址被压入了栈中。这个地址就是ret_addr，也就是说，system函数的参数是在ret_addr下一个字长处。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557066894.png)

重新运行程序，运行到gets函数处，输入“AAAA”，观察栈空间分布，算出了ret_addr与eax的地址距离是44字节

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557062352.png)

我们重新运行程序，到gets函数处输入44字节的垃圾数据，查看栈空间分布。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557058570.png)

这一次我们还是输入44字节的垃圾数据，并在垃圾数据后门输入"dead"标识字符串，执行到ret处查看返回的地址。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557054739.png)

观察到我们返回的地址确实是"dead"的ascii形成的地址。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557050859.png)

ret后发生错误，因为它不是一个有效地址。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557047068.png)

我们查找一下调用system函数处的地址，一会将这个地址填入44字节的垃圾数据后面，然后再在这个地址后面填写"sh"的地址，就形成了system("sh")函数。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557042664.png)

发送payload后，观察栈空间分布。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557037830.png)

执行到ret处发现，要返回的地址就是我们写入的call system的地址，继续执行

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557032931.png)

可以看到pwndbg自动为我们标识出了system函数的参数，就是我们找到的"sh"

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557028260.png)

脚本攻击成功。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557023272.png)



### ret2shellcode

ida32 打开demo32程序，发现调用了vul函数，进入查看

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557016872.png)

vul函数，声明了72字节的局部变量，然后打印出一个字符串，调用了gets函数让我们输入，然后调用strncpy函数将局部变量的字符串拷贝到了bss段的buf。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557009881.png)

这里我们需要学习一种新的攻击方式ret2shellcode，前面的第一个demo是ret2text攻击，代表溢出后返回到程序的后门函数。第二个demo是ret2syscall，代表返回程序的system函数并且我们可以构造它的参数，那么ret2shellcode攻击中，什么是shellcode?

shellcode是一段用于利用软件漏洞而执行的代码，shellcode为机器码，因为经常让攻击者获得shell而得名。shellcode常常使用机器语言编写。 可在暂存器eip溢出后，塞入一段可让CPU执行的shellcode机器码，让电脑可以执行攻击者的任意指令。

了解了这些我们发现shellcode就是一段机器码，执行它后会拿到shell，和上面的执行system("/bin/sh")效果一样。那么怎么写shellcode呢，不用怕，pwntools中自动集成了shellcode模块，利用它我们可以很轻松的生成shellcode。

打开程序，运行到gets函数处，输入"AAAA"，查看栈空间分布。算出ret_addr和eax的地址偏移是76字节。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628557005486.png)

在内存中查找"AAAA"字符串，发现在heap段和stack段以及bss段，vmmap命令查看整个程序的内存空间分布。发现有可读可写可运行的段，这些段有stack和libc中的bss段以及程序中的bss段。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556999022.png)

重新运行程序，创建76字节的垃圾数据，发送过去查看栈空间分布。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556995220.png)

所以我们的思路就是写入shellcode，并利用程序中的strncpy函数，将我们写入的shellcode复制到bss段的某个位置。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556991278.png)

利用pwntools生成shellcode，并将ret_addr覆盖为bss段被复制shellcode地址。那么当我们程序执行ret时，就会将PC置位为shellcode处，执行shellcode。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556988097.png)

查看bss段出的shellcode。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556985139.png)

脚本攻击成功。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556981470.png)



### ROP

在Linux中有"Partial RELRO" "Full RELRO"两种模式，默认开启Partical RELRO，开启Partical RELRO时，GOT是可写的，开启 FULL RELRO 时，GOT表是只读的。

查看程序的保护发现开启了NX保护，栈不可执行保护。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556978543.png)

ida32 打开程序，进入main函数查看，发现调用了vul函数，gets函数还是漏洞溢出点。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556975151.png)

函数窗口ctrl+F查找system函数，发现system函数也没有了

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556972232.png)

strings窗口查看，发现有"/bin/sh"字符串。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556968278.png)

打开test.c程序，我们需要学习一种新的模式，这种模式有点像利用所有程序函数中汇编代码片段来重组，形成一个新的函数，我们要形成的函数就是execve("/bin/sh",NULL,NULL)

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556964723.png)

可以看到这个程序运行后也能拿到shell

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556960574.png)

gdb调试该程序，发现call execve函数，我们跟进入

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556954992.png)

发现在最后执行时调用了SYS_execve，这个函数的参数第一个是"/bin/sh"字符串的地址。我们此时知道了，只要将寄存器中的各个参数设置号，再调用一个函数执行SYS_execve，就可以得到system("/bin/sh")的效果。那么我们怎么进入构造呢？这里就用到了ROPgadget

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556950489.png)

开始攻击，首先运行程序，运行到gets处，输入"AAAA"，算出eax和ret_addr之间的距离，是76字节。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556946368.png)

发送完payload，观察栈空间分布。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556942624.png)

ret返回到了我们的第一个gadget片段地址处，并继续执行。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556937525.png)

调用int 0x80，可以拿到shell了。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556932612.png)



### ret2libc

这一次拿到程序使用checksec查看保护后，用 ida32 程序，发现main函数调用了vul函数，进入vul函数查看

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556928163.png)

发现调用了pus函数输入了一个单词，然后调用gets函数要求输入。漏洞溢出点还是在这里。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556919248.png)

在string窗口，查找发现没有任何可用字符串，并且函数窗口也没有任何能用的。这次该利用什么攻击呢?ret2libc，可以发现这次程序给了我们一个libc.so文件，这个文件是动态链接库文件，任何linux中动态链接的程序，在运行过程中都要用到这个libc.so文件。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556915225.png)

知道了libc.so文件的作用，那么什么是ret2libc攻击呢?简单来说就是通过某一些函数泄露libc的函数，通过与libc.so文件中对应的函数进行对比，得到libc函数基地址。拿到基地址后，我们利用libc的基地址和libc.so文件中的偏移就可以直到所有函数的真正地址。当我们溢出覆盖ret_addr到任何我们知道的函数，就可以执行任何的函数了。那么怎么拿到shell呢，出了构造system("/bin/sh")，还有其他的办法吗?

我们可以利用one_gadget，这个one_gadget就是上面ROPgadget的延申，one_gadget分布在libc中，只要知道了libc的地址，再加上one_gadget的偏移，当程序执行过去就可以执行拿到shell。

现在开始攻击，攻击之前我们需要学习plt表和got表的知识。

观察下面还没有执行puts函数时plt表和got表内容。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556910310.png)

观察执行完puts函数后，plt表和got表内容。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556906150.png)

我们知道了plt表和got表的知识，我们就可以进行攻击了，当我们控制ret_addr时，我们是否可以利用ROP攻击，先构造puts@plt执行，执行完后返回到main函数再一次触发漏洞，进行第二次溢出攻击。第一次的溢出攻击，我们的目标就是泄露libc中puts函数的地址。利用我们得到的libc.so文件，我们可以知道puts函数在libc中的偏移，通过知道了puts函数的真实地址和puts函数在libc中的偏移，我们就可以知道libc的基地址，知道了libc的基地址和libc.so文件中的所有函数偏移，我们就可以控制程序执行任何我们想要执行的函数。

发送完第一次payload后，看到我们泄露程序真实地址的过程中，程序执行jump到了puts函数。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556901512.png)

puts函数libc中的实现是由_IO_file_xsputs完成的，他的参数是我们写入的puts的got表地址。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556897602.png)

此时puts函数的真实地址已经被泄露了出来。ret时会进行第二次溢出攻击，我们也就要发送第二次的payload。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556894200.png)

第二次的payload我们先ret_addr之前填充垃圾数据，然后ret_addr处我们写入libc基地址和one_gadget偏移后成的one_gadget真实地址。在执行one_gadget时，我们就直接拿到了shell。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556885301.png)

反汇编查看one_gadget地址，可以看到最后还是调用了execve函数。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556878499.png)

攻击成功，脚本顺利拿到shell。

![](https://gitee.com/t0rped0/image-bed/raw/master/md/1628556874535.png)

