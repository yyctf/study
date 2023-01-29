语法|作用
-|-
ping  127.0.0.1|执行命令
echo|输出语句
echo on|表示在此语句后所有运行的命令都显示命令行本身 
echo off|表示在此语句后所有运行的命令都不显示命令行本身
echo=|输出空白行
@|与echo off相像，但它是加在每个命令行的最前面，表示运行时不显示这一行的命令行（只能影响当前行）。
start ping 127.0.0.1|重新打开一个窗口进行执行命令
pause|按任意键继续
PAUSE>NUL|暂停且不提示“按下任意键继续”
rem|表示此命令后的字符为注释，不执行。
title|BAT的标题
cls|清除屏幕

@echo off
reg add HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{902CCC39-02E3-4814-AF71-C25E6C685CB2} /v DisplayName  /d "永中Office 2019"
pause

@echo off
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Contro l\Power\PowerSettings\{54533251-82be-4824-96c1-}\{be337238-0d82-4146-a960-4f3749d470c7} /v Attribute /t REG_BINARY /d 00000001
pause

reg add HKLM\Software\MyCo /v Data /t REG_BINARY /d fe340ead
//添加或修改一个值(名称: Data，类型: REG_BINARY，数据: fe340ead)