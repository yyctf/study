# md5弱比较
1. 两个字符不等但是md5相等
```php
<?php
$a=$_GET[a];$b=$_GET[b];
if($a!=$b&&md5($a)==md5($b)){
    echo $flag;
}
?>
```
?a=QNKCDZO&b=240610708
2. md5前和md5后相等

0e215962017
+ [666](../常用工具.md)