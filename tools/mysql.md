Ubuntu上安装MySQL非常简单只需要几条命令就可以完成。

1. sudo apt-get install mysql-server

2. apt-get installmysql-client （可选）

3.  sudo apt-get install libmysqlclient-dev（可选）
安装完成之后可以使用如下命令来检查是否安装成功：

sudo netstat -tap | grep mysql
如果看到有mysql 的socket处于 listen 状态则表示安装成功。

登陆mysql数据库可以通过如下命令：

mysql -u root -p

-u 表示选择登陆的用户名， -p 表示登陆的用户密码，上面命令输入之后会提示输入密码，此时输入密码就可以登录到mysql。