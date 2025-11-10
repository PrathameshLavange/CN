# UDP File Transfer Client
import socket
import os

SERVER_IP = "127.0.0.1"  # Change to server's IP if different machine
PORT = 8080
BUFFER_SIZE = 1024

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter the filename to send: ")

if not os.path.exists(filename):
    print("❌ File not found!")
    exit()

# Send filename first
client_socket.sendto(filename.encode(), (SERVER_IP, PORT))

# Send file contents
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        client_socket.sendto(bytes_read, (SERVER_IP, PORT))

# Send EOF message to mark end of file
client_socket.sendto(b"EOF", (SERVER_IP, PORT))

print("✅ File sent successfully.")
client_socket.close()
