# 切记，细心，耐心
通读全文代码，从功能函数代码开始阅读，例如include文件夹下的common_fun.php，或者有类似关键字的文件。

看配置文件，带有config关键字的文件，找到mysql.class.php文件的connect()函数，查看在数据库连接时是否出现漏洞。

继续跟读首页文件index.php，了解程序运作时调用了哪些函数和文件 以index.php文件作为标线，一层一层去扩展阅读所包含的文件，了解其功能，之后进入其功能文件夹的首页文件，进行扩展阅读。

# 一、输入输出验证


用户的一切输入都是有害的，大多数漏洞的形成原因主要都是未对输入数据进行安全验证或对输出数据未经过安全处理。

所以我们需要针对输入输出数据进行以下的安全检查：

1. 对数据进行精确匹配

2. 接受白名单的数据

3. 拒绝黑名单的数据

4. 对匹配黑名单的数据进行编码



在PHP中，能够由用户输入的变量有：

```
$_SERVER
$_GET
$_POST
$_COOKIE
$_REQUEST
$_FILES
$_ENV
$_HTTP_COOKIE_VARS
$_HTTP_ENV_VARS
$_HTTP_GET_VARS
$_HTTP_POST_FILES
$_HTTP_POST_VARS
$_HTTP_SERVER_VARS
```
我们需要针对这些函数进行必要的安全检查。



1. XSS

    反射型XSS出现在接受用户提交的变量后进行处理，直接输出显示给酷护短，存储型XSS出现在用户提交的变量进行处理后存储到数据库中，再从数据库中读取这条信息输出到客户端。

    对于反射型XSS，应当在当前的PHP页面检查变量被提交时是否经过了安全检查，是否在当前的PHP页面有立即显示。

    对于存储型XSS，首先对于输入的数据进行安全检查后再写入数据库，在输出显示时是否有安全检查。

防御策略：

对输入的数据进行严格的匹配，过滤所有的非法字符进行过滤。

对于输出的数据进行HTML编码，


    < → &lt;    
    > → &gt;
    ( → &#40;
    ) → &#41;
    # → &#35
    & → &amp;
    " → &quot;
    ’ → &apos;
    ` → %60
 

2. SQL注入

SQL注入关系到的是数据库安全，所以对于用户的恶意输入必须做严格的过滤。

在SQL注入攻击中，一般会用到 ’、select、insert、delete、from、=、in、update等关键字，需要针对这些字符进行过滤，要查看传递的变量参数是否用户可控制，以及它们是否做到安全检查。

防御策略：

使用参数化查询。

 

3. 文件上传

任意文件上传可能会造成网站getshell，也是一个非常危险的功能，对于文件上传也需要非常警惕。

PHP的文件上传通常会使用move_uploaded_file()函数，在文件上传的位置也需要进行上传文件的检测，做好安全检查。

防御策略：

使用白名单检测上传文件后缀。

上传后随机生成文件名称。

上传目录限制文件不可执行。

注意防范%00进行的截断。

 

4. 文件包含

文件包含漏洞可以读取敏感文件，配合文件上传功能可以得到webshell,远程文件包含可以直接远程包含shell。

PHP可能出现文件包含的函数：include、include_once、require、require_once、show_source、highlight_file、readfile、file_get_contents、fopen、file。

防御策略：

对输入数据进行精确匹配。

过滤参数中的/、..等字符。

 

5. 命令注入

php执行系统命令可以使用以下几个函数：system、exec、passthru、“、shell_exec、popen、proc_open、pcntl_exec。

我们通过在全部程序文件中搜索这些函数，确定函数的参数是否会因为外部提交而改变，检查这些参数是否有经过安全处理。

防御策略：

使用自定义函数或函数库来替代外部命令的功能。

使用escapeshellarg函数来处理命令参数。

使用safe_mode_exec_dir指定可执行文件的路径。

 

6. 代码注入

PHP可能出现代码注入的函数：eval、preg_replace+/e、assert、call_user_func、call_user_func_array、create_function。

查找程序中程序中使用这些函数的地方，检查提交变量是否用户可控，有无做输入验证

防御策略：

输入数据精确匹配。

使用白名单过滤可执行的函数。

 

7. 文件管理

PHP的用于文件管理的函数，如果输入变量可由用户提交，程序中也没有做数据验证，可能成为高危漏洞。我们应该在程序中搜索如下函数：copy、rmdir、unlink、delete、fwrite、chmod、fgetc、 fgetcsv、fgets、fgetss、file、file_get_contents、fread、readfile、ftruncate、 file_put_contents、fputcsv、fputs，但通常PHP中每一个文件操作函数都可能是危险的。

防御策略：

对提交数据进行严格匹配。

限定文件可操作的目录。

 

8. 变量覆盖

PHP的变量覆盖会出现在以下集中情况：

遍历初始化变量

函数覆盖变量parse_str、mb_parse_str、import_request_variables

3.Register_globals=ON时，GET方式提交变量会直接覆盖

防御策略：

设置Register_globals=OFF。

不使用覆盖变量的函数来获取变量。

二、会话安全

1. HTTPOnly设置

打开该指令可以有效预防通过XSS攻击劫持会话ID。

2. domain设置

检查session.cookie_domain是否只包含本域，如果是父域，则其他子域能够获取本域的cookies。

3. path设置

检查session.cookie_path，如果网站本身应用在/app，则path必须设置为/app/，才能保证安全。

4. cookies持续时间

检查session.cookie_lifetime，如果时间设置过程过长，即使用户关闭浏览器，攻击者也会危害到帐户安全。

5. secure设置

如果使用HTTPS，那么应该设置session.cookie_secure=ON，确保使用HTTPS来传输cookies。

6. session固定

如果当权限级别改变时（例如核实用户名和密码后，普通用户提升到管理员），我们就应该修改即将重新生成的会话ID，否则程序会面临会话固定攻击的风险。

7. CSRF

跨站请求伪造攻击，是攻击者伪造一个恶意请求链接，通过各种方式让正常用户访问后，会以用户的身份执行这些恶意的请求。我们应该对比较重要的程序模块，比如修改用户密码，添加用户的功能进行审查，检查有无使用一次性令牌防御csrf攻击。

三、加密

1. 明文存储密码

采用明文的形式存储密码会严重威胁到用户、应用程序、系统安全。

2. 密码弱加密

使用容易破解的加密算法，MD5加密已经部分可以利用md5破解网站来破解。

3. 密码存储在攻击者能访问到的文件

例如：保存密码在txt、ini、conf、inc、xml等文件中，或者直接写在HTML注释中。

四、认证和授权

1. 用户认证

检查代码进行用户认证的位置，是否能够绕过认证，例如：登录代码可能存在表单注入。

检查登录代码有无使用验证码等，防止暴力破解的手段。

2. 函数或文件的未认证调用

一些管理页面是禁止普通用户访问的，有时开发者会忘记对这些文件进行权限验证，导致漏洞发生

某些页面使用参数调用功能，没有经过权限验证，比如index.php?action=upload。

3. 密码硬编码

有的程序会把数据库链接账号和密码，直接写到数据库链接函数中。

五、PHP危险函数

1. 缓冲区溢出

（1）confirm_phpdoc_compiled

影响版本：

phpDocumentor phpDocumentor 1.3.1

phpDocumentor phpDocumentor 1.3 RC4

phpDocumentor phpDocumentor 1.3 RC3

phpDocumentor phpDocumentor 1.2.3

phpDocumentor phpDocumentor 1.2.2

phpDocumentor phpDocumentor 1.2.1

phpDocumentor phpDocumentor 1.2

（2）mssql_pconnect/mssql_connect

影响版本：PHP < = 4.4.6

（3）crack_opendict

影响版本：PHP = 4.4.6

（4）snmpget

影响版本：PHP <= 5.2.3

（5）ibase_connect

影响版本：PHP = 4.4.6

（6）unserialize

影响版本：PHP 5.0.2、PHP 5.0.1、PHP 5.0.0、PHP 4.3.9、PHP 4.3.8、PHP 4.3.7、PHP 4.3.6、PHP 4.3.3、PHP 4.3.2、PHP 4.3.1、PHP 4.3.0、PHP 4.2.3、PHP 4.2.2、PHP 4.2.1、PHP 4.2.0、PHP 4.2-dev、PHP 4.1.2、PHP 4.1.1、PHP 4.1.0、PHP 4.1、PHP 4.0.7、PHP 4.0.6、PHP 4.0.5、PHP 4.0.4、PHP 4.0.3pl1、PHP 4.0.3、PHP 4.0.2、PHP 4.0.1pl2、PHP 4.0.1pl1、PHP 4.0.1



2. session_destroy()删除文件漏洞

影响版本：不祥，需要具体测试。

测试代码如下：


<?php
session_save_path(‘./’);
session_start();
if($_GET[‘del’]) {
session_unset();
session_destroy();
}else{
$_SESSION[‘do’]=1;
echo(session_id());
print_r($_SESSION);
}
?>
当我们提交cookieHPSESSIONID=/../1.php，相当于删除了此文件。



3. unset()-zend_hash_del_key_or_index漏洞

zend_hash_del_key_or_index PHP4小于4.4.3和PHP5小于5.1.3，可能会导致zend_hash_del删除了错误的元素。当PHP的unset()函数被调用时，它会阻止变量被unset。

六、信息泄露

phpinfo()

如果攻击者可以浏览到程序中调用phpinfo显示的环境信息，会为进一步攻击提供便利。


七、PHP环境

1. open_basedir设置

open_basedir能限制应用程序能访问的目录，检查有没有对open_basedir进行设置，当然有的通过web服务器来设置，例如：apache的php_admin_value，nginx+fcgi通过conf来控制php设置。

2. allow_url_fopen设置

如果allow_url_fopen=ON，那么php可以读取远程文件进行操作，这个容易被攻击者利用。

3. allow_url_include设置

如果allow_url_include=ON，那么php可以包含远程文件，会导致严重漏洞。

4. safe_mode_exec_dir设置

这个选项能控制php可调用的外部命令的目录，如果PHP程序中有调用外部命令，那么指定外部命令的目录，能控制程序的风险。

5. magic_quote_gpc设置

这个选项能转义提交给参数中的特殊字符，建议设置magic_quote_gpc=ON。

6. register_globals设置

开启这个选项，将导致php对所有外部提交的变量注册为全局变量，后果相当严重。

7. safe_mode设置

safe_mode是PHP的重要安全特性，建议开启。

8. session_use_trans_sid设置

如果启用 session.use_trans_sid，会导致 PHP 通过 URL 传递会话 ID，这样一来，攻击者就更容易劫持当前会话，或者欺骗用户使用已被攻击者控制的现有会话。

9. display_errors设置

如果启用此选项，PHP将输出所有的错误或警告信息，攻击者能利用这些信息获取web根路径等敏感信息。

10. expose_php设置

如果启用 expose_php 选项，那么由 PHP 解释器生成的每个响应都会包含主机系统上所安装的 PHP 版本。了解到远程服务器上运行的 PHP 版本后，攻击者就能针对系统枚举已知的盗取手段，从而大大增加成功发动攻击的机会。