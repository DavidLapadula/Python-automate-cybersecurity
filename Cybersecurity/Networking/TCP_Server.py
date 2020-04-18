import socket

host = socket.gethostname()
port = 9337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print ("\n Server started")

conn, addr = sock.accept()

print("\n Conn established with: " + str(addr))

message = "Thanks for connecting " + str(addr)

conn.send(message.encode("ascii"))
conn.close()