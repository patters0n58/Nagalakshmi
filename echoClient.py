import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

while True:
    msg = input("You: ")
    client.sendall(msg.encode())
    data = client.recv(1024).decode()
    print("Server:", data)
    if msg.lower() == 'bye':
        break

client.close()

