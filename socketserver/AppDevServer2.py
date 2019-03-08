import socket
# socket server program

HOST = 'appdev.lyle.smu.edu'        # localhost means your machine acts as server for local clients
PORT = 5742	                        # CHANGE TO YOUR port

# --------------------
# Modify this function to return msg + name,id,& coding name
def processMsg(msg):
	name = 'JC'
	id = '46992742'
	codingName = 'hennrock05'
	
	return "ADDPEV says: " + msg + ' ' + name + ' ' + id + ' ' + codingName

# -----------------------------------

#create socket object for Internet V4 and use streams to get/send data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set up the socket on our PORT
s.bind((HOST, PORT))

#display a message to show we are alive
print ("Server waiting for a client on port " + str(PORT) )

keepListening = True

while (keepListening ):
	# listen( ) is synchronous - waits until client shows up
	# the parameter (backlog) sets the number of incoming that will be queued if busy
	s.listen(2)

	#when we get here a client has connected -
	# get the connection socket and address
	conn, addr = s.accept()

	print ('Client coming in from: ', addr    )

	#data comes in as bytes - here we receive 1024 bytes
	data = conn.recv(1024)

	#convert bytes to a string using decode so we can string concatenate
	serverData = data.decode()

	#do something with the incoming msg
	msg = processMsg(serverData)

	#use encode() to convert string back to bytes for transport back to client
	conn.sendall(msg.encode())

	keepListening = (serverData != 'bye')

#close down the connection and the server
conn.close()
