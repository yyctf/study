# apache不解析

`sudo apt-get install libapache2-mod-php`

kali安装apache

`apt-get install httpd`

选择apache的版本

`apt-get install apache2`

安装apache2

`vim /etc/apache2/ports.conf`

编辑这个文件，把端口号改成8080

关闭SElinux：`setenforce=0`

`/etc/init.d/apache2 start` 启动apache

`localhost:8080`  启动成功

- 安装
> sudo apt install apache2
- 卸载
> sudo apt remove apache2
- 更新已安装的包
> sudo apt-get update
- 创建html
> touch index.html
- 删除html
> sudo rm index.html
- 查看apache版本号
> apache2 -v
- 查看当前所在目录
> pwd
- 