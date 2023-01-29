本地新建一个my文件夹，进去后新建一个myf文件夹，进去后新建index.php文件

```php
<?php
echo 'hello world';
?>
```

在项目的同目录下新建Dockerfile文件，内容：

```docker
FROM php:5.6-apache
#将所需文件放到容器中
#COPY setup.sh /mysql/setup.sh
#FROM mysql:5.7
#设置容器启动时执行的命令
#CMD ["sh", "/mysql/setup.sh"]
RUN docker-php-ext-install mysqli
ADD myapp /var/www/html
```

简单说明下我们基于的镜像是php:5.6-apache，然后配置mysql拓展，将项目copy到容器的var/www/html目录下,这里只会负责myf下面的内容

继续在项目同目录下创建镜像

    docker build -t myf ./

将镜像放到容器中

    docker run -d -p 8888:80 myf

简单理解就是启动docker，然后奖内网的80端口映射到外网的8888端口，接下来访问端口即可发现已经成功了

参数|说明
-|-
-i|以交互模式运行，通常配合-t
-t|为容器重新分配一个伪输入终端，通常配合-i
-d|后台运行容器
-p|端口映射，格式为主机端口:容器端口
-e|设置环境变量，这里设置的是root密码
--name|设置容器别名

作用|命令
-|-
查找mysql可用版本|docker search mysql
拉取mysql镜像别名latest|docker pull mysql:latest
新建并运行容器|docker run -itd -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 --name mysql-latest mysql
运行已有容器|docker start id
查看已安装镜像|docker images
查看docker|docker ps -a
进入容器|docker exec -it id /bin/bash
关闭docker|docker stop id
关闭所有正在运行的docker|docker stop $(docker ps -aq)
删除所有的docker|docker rm $(docker ps -aq)
删除容器|docker rm id
删除镜像|docker rmi -f id
删除所有镜像|docker system prune -a
更改中国源|{"registry-mirrors": ["https://registry.docker-cn.com"]}
将docker打包成image|docker commit id z91430/yyctf:tag然后docker push name


将项目上传至dockerhub

    docker login//登录
    docker tag z91430/yyctf:自定义名字
    docker push z91430/yyctf:自定义名字

将docker打包成image

拉取镜像

    docker pull z91430/yyctf:latest

运行镜像

    docker run -d -p 8080:80 z91430/yyctf:latest
    //或者
    docker run -d -p 8080:80 --name latest z91430/yyctf