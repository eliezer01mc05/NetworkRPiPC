# Import socket module 
import socket                
  
# Create a socket object 
s1 = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345 

ip = '10.68.10.152'
  
# connect to the server on local computer 
s1.connect((ip, port)) 
print('Data sent to ', ip, 'Socket TCP')

# receive data from the server 
#print (s1.recv(size))
# close the connection
print ("Close connection - Socket TCP") 
s1.close()

hostMACAddressBT = '5C:C9:D3:65:98:93' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
portBT = 7 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s2 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s2.bind((hostMACAddressBT, portBT))
s2.listen(backlog)
try:
    client, address = s2.accept()
    while 1:
        dataBT = client.recv(size)
        if dataBT:
            print('Data received from - Socket Bluetooth')
            #print(dataBT)
            # client.send(data)
except:	
    print ("Close connection - Socket Bluetooth")	
    client.close()
    s2.close()  