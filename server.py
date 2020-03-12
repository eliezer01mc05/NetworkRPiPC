import socket

# next create a socket object 
socketTCP = socket.socket()      
print ("Socket TCP successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
portTCP = 12345
serverMACAdressBT = "5C:C9:D3:65:98:93"
portBT = 7

socketTCP.bind(('', portTCP))        
print ("socket binded to", portTCP) 

# put the socket into listening mode 
socketTCP.listen(5)  
print ("socket is listening")           

# a forever loop until we interrupt it or 
# an error occurs 
while True: 

    # Establish connection with client. 
    c, addr = socketTCP.accept()     
    print ('Data received from', addr, '- Socket TCP')
    #c.send(bytes('RPi - PC - TCP/IP\n', encoding = 'utf-8'))
    print ("Close connection - Socket TCP")
    c.close()
    
    # Create the client socket
    socketBT = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    socketBT.connect((serverMACAdressBT, portBT))
    socketBT.send(bytes("hello hello", 'UTF-8'))
    print ('Data sent to', serverMACAdressBT, '- Socket Bluetooth')
    print ("Close connection - Socket Bluetooth")
    socketBT.close()