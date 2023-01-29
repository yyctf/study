# 修改python安装目录 Python27\Lib\目录下的mimetypes.py文件。

- 在import下添加如下几行：
```
if sys.getdefaultencoding() != 'gbk': 
    reload(sys) 
    sys.setdefaultencoding('gbk')
 ```

# linux中python2安装pip
```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
python2 get-pip.py
```

# python2与python3共存

先安装python3添加到系统环境变量，然后安装python2，添加到环境变量，然后将python2的python.exe,pythonw.exe改名为python2.exe,pythonw2.exe,然后进行重新安装pip

```cmd
python2 -m pip install --upgrade pip --force-reinstall
python -m pip install --upgrade pip --force-reinstall
``

即可完成