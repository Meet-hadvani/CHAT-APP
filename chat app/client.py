import socket
import pickle

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
#normal data recieve
'''
while(1):
	full_msg = ''
	new_msg = True
	while(1):
		msg = s.recv(16)
		if new_msg:
			#print(f"new message length: {msg[:HEADERSIZE]}")
			msglen = int(msg[:HEADERSIZE])
			new_msg = False
			
		full_msg += msg.decode("utf-8")
		if len(full_msg)-HEADERSIZE == msglen:
			#print("full message recieved")
			print(full_msg[HEADERSIZE:])
			new_msg = True
			full_msg = ''
			
	print(full_msg)
'''
#data encodede transmission
'''
while(1):
	full_msg = b''
	new_msg = True
	while(1):
		msg = s.recv(16)
		if new_msg:
			msglen = int(msg[:HEADERSIZE])
			new_msg = False
			
		full_msg += msg
		if len(full_msg)-HEADERSIZE == msglen:
			print(full_msg[HEADERSIZE:])
			
			d = pickle.loads(full_msg[HEADERSIZE:])
			print(d)
			new_msg = True
			full_msg = b''
			
	print(full_msg)
'''

