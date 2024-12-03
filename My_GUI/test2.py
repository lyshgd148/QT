import socket

server_ip = "0.0.0.0"
server_port = 7898

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)  # 最多允许一个连接

print("Waiting for connection...")

# 等待客户端连接
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)
while True:
    data = client_socket.recv(128)
    print("Received:", data.decode())
    response = "Hello I am PC!"
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()
