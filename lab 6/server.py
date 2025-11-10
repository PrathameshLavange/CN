# UDP File Transfer Server
import socket

# Define IP and Port
IP = "0.0.0.0"   # Listen on all network interfaces
PORT = 8080
BUFFER_SIZE = 1024

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP, PORT))

print("UDP Server is ready and waiting for file...")

# Receive filename
filename, client_addr = server_socket.recvfrom(BUFFER_SIZE)
filename = filename.decode()
print(f"Receiving file: {filename}")

# Open file for writing in binary mode
with open(filename, "wb") as f:
    while True:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        if data == b"EOF":
            break
        f.write(data)

print("✅ File received successfully.")
server_socket.close()
