import socket

HOST = 'appdev.lyle.smu.edu'        # localhost means your machine acts as server for local clients
PORT = 5742# Arbitrary non-reserved port

#create socket object for Internet V4 and use streams to get/send data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set up the socket on our PORT
s.bind((HOST, PORT))

#display a message to show we are alive
print ("server waiting for a client...")

keepListening = True

# loop to keep the server running
while (keepListening):

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
    msg = "APPDEV talking back to you: " + serverData
    
    #use encode() to convert string back to bytes for transport back to client
    conn.sendall(msg.encode())

    # Use encode() to convert string back to bytes
    keepListening = (serverData != 'bye')
  
#close down the connection and the server
conn.close()
