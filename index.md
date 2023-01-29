[工具与靶场](#工具与靶场)

1. [工具](#工具)
2. [靶场](#靶场)
3. [工具使用方法](#工具使用方法)
   1. [github](#github)
   2. [hashcat](#hashcat)
   3. [sqlmap](#sqlmap)
   4. [xray](#xray)
   5. [nmap](#nmap)

1. [java安全](#java安全)
2. [ctf](#ctf)
   1. [web](#web)
   2. [misc](#misc)
   3. [crypto](#crypto)
   4. [re](#re)
   5. [pwn](#pwn)
3. [靶场](#靶场-1)
   1. [dvwa](#dvwa)
   2. [pikaqiu](#pikaqiu)
   3. [uploadlabs](#uploadlabs)
   4. [sqllabs](#sqllabs)
   5. [vulhub](#vulhub)
4. [wp](#wp)

`千里之行,始于足下`

# 工具与靶场

## 工具

常用工具与靶场与下载链接

`工欲其善必先利器`

| 工具                 | 链接                                                                                              | 教程  | 描述  |
| ------------------ | ----------------------------------------------------------------------------------------------- | --- | --- |
| github             | https://github.com                                                                              |     |     |
| dirsearch(目录扫描)    | https://github.com/maurosoria/dirsearch                                                         |     |     |
| xray(漏洞扫描)         | https://download.xray.cool/xray                                                                 |     |     |
| vulmap(漏洞扫描)       | https://github.com/zhzyker/vulmap                                                               |     |     |
| sqlmap(SQL注入)      | https://github.com/sqlmapproject/sqlmap                                                         |     |     |
| tplmap(SSTI注入)     | https://github.com/epinna/tplmap                                                                |     |     |
| CaptfEncoder(进制转换) | https://github.com/guyoung/CaptfEncoder/releases                                                |     |     |
| BerylEnigma(进制转换)  | https://github.com/ffffffff0x/BerylEnigma/releases                                              |     |     |
| 大佬的笔记              | https://github.com/ffffffff0x/1earn                                                             |     |     |
| f8x(linux环境搭建)     | wget -O f8x https://f8x.io/ && mv --force f8x /usr/local/bin/f8x && chmod +x /usr/local/bin/f8x |     |     |
| 小皮面板               | wget -O install.sh https://download.xp.cn/install.sh && sudo bash install.sh                    |     |     |
| 宝塔                 | wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh  |     |     |
| 宝塔卸载               | wget http://download.bt.cn/install/bt-uninstall.sh                                              |     |     |
| awd                | https://github.com/fyfztms/awd_ctf_platform                                                     |     |     |
| 蚁剑加载器              | https://github.com/AntSwordProject/AntSword-Loader                                              |     |     |
| 蚁剑                 | https://github.com/AntSwordProject/antSword                                                     |     |     |
|                    |                                                                                                 |     |     |
|                    |                                                                                                 |     |     |
|                    |                                                                                                 |     |     |
|                    |                                                                                                 |     |     |

## 靶场

| 工具                    | 链接                                               | wp                                             |
| --------------------- | ------------------------------------------------ | ---------------------------------------------- |
| dvwa(php7)            | https://github.com/digininja/DVWA                | [dvwa_wp](./靶场/dvwa通关.md)                      |
| pikachu               | https://github.com/zhuifengshaonianhanlu/pikachu | [pikachu_wp](./靶场/pikachu.md)                  |
| uploadlabs(php5.2.17) | https://github.com/clriseaa/docker-uploadlabs    | [uploadlabs_wp](./靶场/uploadlabs/uploadlabs.md) |
| sqlilabs(php5)        | https://github.com/himadriganguly/sqlilabs       | [sqlilabs_wp](./靶场/sqlilabs/sqlilabs.md)       |
| vulhub(中间件漏洞)         | https://github.com/vulhub/vulhub                 |                                                |
| xsslabs               | https://xssaq.com/yx/index.php                   | [xsslabs_wp](./靶场/xss闯关.md)                    |
| xvwa                  | https://github.com/s4n7h0/xvwa                   | [xvwa_wp](./靶场/xvwa/xvwa.md)                   |

## 工具使用方法


### hashcat

### sqlmap

### xray

- 使用基础爬虫爬取并对爬虫爬取的链接进行漏洞扫描：

`./xray.exe webscan --basic-crawler http://example.com --html-output xxx.html`

- 代理模式

`./xray.exe webscan --listen 127.0.0.1:7777 --html-output xray-testphp.html --poc pocs/* --plugin phantasm,baseline,brute-force,cmd-injection,crlf-injection,dirscan,fastjson,jsonp,path-traversal,redirect,shiro,sqldet,ssrf,struts,thinkphp,upload,xss,xxe`

### nmap

# java安全(待更新)

# ctf

## web

## misc

## crypto

## re

## pwn

# wp
