import socket
import time
import pickle

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while(1):
	clientsocket, address = s.accept()
	print(f"connection from {address} has been established")
	msg = ""
	
	while(1):
		#time.sleep(3)
		#msg = f"server - {time.time()} :"
		msg = "hello"
		msg = f'{len(msg):<{HEADERSIZE}}' + msg
		clientsocket.send(bytes(msg, "utf-8"))
	'''
	#for pickel encoded data transmission
	d = {1: "hey", 2:"THERE"}
	msg = pickle.dumps(d)
	
	msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
	clientsocket.send(msg)
	'''