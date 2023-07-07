import socket

map = {}
s = socket.socket()

server_ip = "10.0.1.3"
port = 12346

s.bind((server_ip, port))
s.listen(5)

#Below functions parses different requests based on their type and sends back response
def put(req):
      #Now we should parse request to get key val pair
      slash_count = 0
      space_count = 0
      key = ""
      val = ""
      for c in req:
          if c=='/':
              slash_count+=1
          elif c==' ':
              space_count+=1
          if slash_count==2 and c!='/':
              key+=c
          if slash_count==3 and space_count==1 and c!='/':
              val+=c

      if key in map:
          map[key] = val
          #It will modify the resource
          response = "HTTP/1.1 204 No Content\r\n\r\n"
      else:
          map[key] = val
          #It will create new resource
          response = "HTTP/1.1 201 Resource Created\r\n\r\n"
      return response


def get(req):
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

      if key in map:
          response = "HTTP/1.1 200 OK\r\n\r\n"+map[key]
      else:
          response = "HTTP/1.1 404 Not Found\r\n\r\n"
      return response

#server accepting connection from cache
c, addr = s.accept()
print ('Got connection from cache: ', addr )

while True:
  req = c.recv(1024).decode()
  if req.startswith("PUT"):
      response = put(req)
  elif req.startswith("GET"):
      response = get(req)
  elif req=="":
      break
  c.send(response.encode())

c.close()
