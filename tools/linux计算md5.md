# 计算文件的md5值
- md5sum 文件名

例如我要计算flag.txt的md5值，那就md5sum flag.txt
# 计算字符串的md5值
- echo -n 'flag'|md5sum

-n是因为echo默认结尾加换行，加了-n就去掉了，这样就可以获取标准的字符串md5值