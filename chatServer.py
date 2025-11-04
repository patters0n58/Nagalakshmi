
import socket
import threading
import random

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

clients = {}  # {client_socket: user_id}


def broadcast(message, sender=None):
    for client in list(clients.keys()):
        if client != sender:
            try:
                client.sendall(message.encode("utf-8"))
            except:
                client.close()
                del clients[client]


def private_message(sender, target_id, message):
    found = False
    for client, uid in list(clients.items()):
        if uid == target_id:
            try:
                client.sendall(f"[Private] {clients[sender]}: {message}".encode("utf-8"))
                sender.sendall(f"[To {target_id}] {message}".encode("utf-8"))
                found = True
                break
            except:
                client.close()
                del clients[client]

    if not found:
        sender.sendall(f"[System] User '{target_id}' not found.".encode("utf-8"))


def handle(client):
    user_id = clients[client]
    try:
        client.sendall(f"Your ID is {user_id}".encode("utf-8"))
        broadcast(f"[System] {user_id} joined the chat!", sender=client)

        while True:
            msg = client.recv(1024).decode("utf-8")
            if not msg:
                break

            if msg.startswith("/msg "):
                parts = msg.split(" ", 2)
                if len(parts) < 3:
                    client.sendall("[System] Usage: /msg <User-ID> <message>".encode("utf-8"))
                else:
                    _, target_id, private_text = parts
                    private_message(client, target_id.strip(), private_text.strip())
            else:
                broadcast(f"{user_id}: {msg}", sender=client)

    except Exception as e:
        print(f"[Error] {user_id}: {e}")

    finally:
        if client in clients:
            del clients[client]
            broadcast(f"[System] {user_id} left the chat.")
            client.close()
            print(f"[SERVER] {user_id} disconnected.")


def receive():
    while True:
        client, address = server.accept()
        user_id = f"User-{random.randint(1000, 9999)}"
        clients[client] = user_id
        print(f"[SERVER] {user_id} connected from {address}")

        threading.Thread(target=handle, args=(client,), daemon=True).start()


receive()
