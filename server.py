import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP and port
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

# Listen for connections
server_socket.listen(1)
print("Server is waiting for connection...")

# Accept client connection
conn, addr = server_socket.accept()
print("Connected to:", addr)

# Receive data from client
data = conn.recv(1024).decode()
print("Client says:", data)

# Send response to client
message = "Hello Client, message received!"
conn.send(message.encode())

# Close connection
conn.close()
server_socket.close()