- [数学公式](#数学公式)
  - [二级标题1](#二级标题1)
  - [二级标题2](#二级标题2)
    - [三级标题1](#三级标题1)
    - [三级标题2](#三级标题2)
          - [六级标题](#六级标题)
- [横线](#横线)
- [图片](#图片)
- [锚点与链接 Links](#锚点与链接-links)
- [表格](#表格)
- [缩进风格](#缩进风格)
- [代码块](#代码块)
- [待办事项](#待办事项)
- [特殊符号 HTML Entities Codes](#特殊符号-html-entities-codes)
    - [Emoji表情 :smiley:](#emoji表情-smiley)
- [绘图](#绘图)
  - [绘制流程图 Flowchart](#绘制流程图-flowchart)
  - [绘制序列图 Sequence Diagram](#绘制序列图-sequence-diagram)
# 数学公式
上划线$\overline{X}$
下划线$\underline{X}$
上标：X<sub>2</sub> 下标：O<sup>2</sup>

来个公式

$$s=123^2$$

## 二级标题1
## 二级标题2
### 三级标题1
### 三级标题2
> 一级
>> 二级
>>>>>> 六级

1. 1
2. 234
   1. dsada
   2. sadasdfas
      1. dfsdf
      2. asf

- 1
  - 11
  - 12
- 2
  - 21
  - 22
    - 221
    - 222


......
###### 六级标题

# 横线

---

# 图片
![image](https://user-images.githubusercontent.com/1908863/28227953-eb6eefa4-68a1-11e7-8769-96ea83facf3b.png)

`在线图片`

==也可以是本地图片==

***加粗斜体***
**加粗**
*斜体*

跳转md文档[跳转](./Markdown%E8%AF%AD%E6%B3%95%E5%AD%A6%E4%B9%A0.md)

# 锚点与链接 Links

[普通链接](http://localhost/)

[普通链接带标题](http://localhost/ "普通链接带标题123")

直接链接：<https://github.com>

[锚点链接][anchor-id]

[anchor-id]: http://www.this-anchor-link.com/
# 表格
列名|居中|左对齐(默认)|右对齐
-|:-:|:-|-:
1|2|3|4

# 缩进风格

&emsp;&emsp;首行缩进
```
&emsp;&emsp;
```
即缩进四个空格，也做为实现类似`<pre>`预格式化文本(Preformatted Text)的功能。

    <?php
        echo "Hello world!";
    ?>

预格式化文本：

    | First Header  | Second Header |
    | ------------- | ------------- |
    | Content Cell  | Content Cell  |
    | Content Cell  | Content Cell  |

# 代码块
```c
#c语言代码块
include<stdio.h>
int main(void){
    int i=6;
    printf("hello world%d",i);
}
```
# 待办事项
- [ ] 未完成
- [x] 已完成


# 特殊符号 HTML Entities Codes

&copy; &  &uml; &trade; &iexcl; &pound;
&amp; &lt; &gt; &yen; &euro; &reg; &plusmn; &para; &sect; &brvbar; &macr; &laquo; &middot;

X&sup2; Y&sup3; &frac34; &frac14;  &times;  &divide;   &raquo;

18&ordm;C  &quot;  &apos;

### Emoji表情 :smiley:

> Blockquotes :star:
>
# 绘图
## 绘制流程图 Flowchart

```flow
st=>start: 用户登陆
op=>operation: 登陆操作
cond=>condition: 登陆成功 Yes or No?
e=>end: 进入后台

st->op->cond
cond(yes)->e
cond(no)->op
```

## 绘制序列图 Sequence Diagram

```seq
Andrew->China: Says Hello
Note right of China: China thinks\nabout it
China-->Andrew: How are you?
Andrew->>China: I am good thanks!
```
