
import socket
import threading


HOST = "0.0.0.0"    
PORT = 9999


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f" Server started on {HOST}:{PORT}")

clients = []
nicknames = []


def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            if decoded.lower() == "bye":
                client.send("Goodbye!\n".encode())
                break
            broadcast(message, sender_socket=client)
        except:
            break

    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        nickname = nicknames[index]
        nicknames.remove(nickname)
        broadcast(f"{nickname} left the chat.\n".encode())
        client.close()
        print(f"{nickname} disconnected.")


def receive():
    while True:
        client, address = server.accept()
        print(f" Connected with {str(address)}")

        
        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f" {nickname} joined the chat!\n".encode())
        client.send("Connected to server.\n".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(" Waiting for connections...")
receive()
