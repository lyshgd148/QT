import socket

# 配置服务器信息
server_ip = "0.0.0.0"  # 监听所有网络接口
server_port = 7871

# 创建 TCP 服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)  # 最多允许一个连接

print("Waiting for connection...")

# 等待客户端连接
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)
while True:
    # 接收数据
    data = client_socket.recv(1024)
    print("Received data:", data.decode())

    # 发送响应给客户端
    response = "Hello from server!"
    client_socket.send(response.encode())

# 关闭连接
client_socket.close()
server_socket.close()