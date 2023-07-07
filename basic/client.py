import socket
import time

serverIP = "10.0.1.2"

dst_ip = "10.0.1.2"
s = socket.socket()

print(dst_ip)

port = 12346

s.connect((dst_ip, port))


#Write your code here:
#1. Add code to send HTTP GET / PUT / DELETE request. The request should also include KEY.
#2. Add the code to parse the response you get from the server.\

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

#This request will delete a key if it is present in dictionary
s.send("DELETE /assignment1/k3 HTTP/1.1\r\n\r\n".encode())
print ("Client received: "+ s.recv(1024).decode())

#Closing the connection
s.close()
