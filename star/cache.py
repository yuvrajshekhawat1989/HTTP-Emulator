import socket

#Initializing an empty cache
map = {"":""}

s = socket.socket()

cache_ip = "10.0.1.2"
server_ip = "10.0.1.3"
port = 12346

s.bind((cache_ip,port))
s.listen(5)

#Making a socket to connect to server for put requests or in case if cache misses
g = socket.socket()
g.connect((server_ip,port))
print("Cache is connected to server 10.0.1.3")

#Extracts key from a get request
def get_key(req):
      #Now we should parse request to get key
      space_count = 0
      key = ""
      flag =False
      for c in req:
          # if c==' ':
          #     space_count+=1
          if c=='=':
              flag = True
          elif c==' ':
              flag = False
          if flag and c!='=':
              key+=c
      return key
#This function gets value from response of get from server
def get_value(resp):
    new_line_count = 0
    val=""
    for c in resp:
        if(new_line_count==2):
            val+=c;
        if c=='\n':
            new_line_count+=1
    return val



      # if key in map:
      #     response = "HTTP/1.1 200 OK\r\n\r\n"+map[key]
      # else:
      #     response = "HTTP/1.1 404 Not Found\r\n\r\n"
      # return response

c, addr = s.accept()
print ('Got connection from client: ', addr )

while True:
  req = c.recv(1024).decode()
  if req.startswith("PUT"):
      #This requests needs to be transferred to server
      g.send(req.encode())
      response = g.recv(1024).decode()
  elif req.startswith("GET"):
      #Check whether key in cache
      key = get_key(req)
      if key in map:
          response = "HTTP/1.1 200 OK\r\n\r\n"+map[key]
          print("Key present in cache")
      else:
          print("Key absent in cache")
          g.send(req.encode())
          response = g.recv(1024).decode()
          if(response.startswith("HTTP/1.1 200 OK\r\n\r\n")):
              map[key] = get_value(response)
              print("Key inserted in cache")
  elif req=="":
      break
  c.send(response.encode())

g.close()
c.close()
