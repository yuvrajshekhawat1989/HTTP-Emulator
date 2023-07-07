import socket
import time

server_ip = "10.0.1.3"

cache_ip = "10.0.1.2"
s = socket.socket()

port = 12346

s.connect((cache_ip, port))
print("This client is now connected to cache %s"%(cache_ip))


#Let's insert some key-value pairs in dictionary
for i in range(6):
    key = "key"+str(i+1)
    value = "val"+str(i+1)
    s.send("PUT /assignment1/"+key+'/'+value+" HTTP/1.1\r\n\r\n".encode())
    print ("Client received: "+ s.recv(1024).decode())

#Now this get request will fetch the corresponding key
for i in range(6):
    for j in range(3):
        key = "key"+str(i+1)
        start = time.time()
        s.send("GET /assignment1?key="+key+" HTTP/1.1\r\n\r\n".encode())
        end = time.time()
        print ("Client received: "+ s.recv(1024).decode()+"\nTime took: "+str(end-start))

#Closing the connection
s.close()
