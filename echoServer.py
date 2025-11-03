import socket
import threading

def handle_client(conn, addr):
    print(f"Connected: {addr}")
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break
        print(f"Client: {data}")
        if data.lower() == 'bye':
            conn.sendall("Goodbye".encode())
            break
        else:
            conn.sendall(f"Echo: {data}".encode())
    conn.close()
    print(f"Closed: {addr}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen()
    print("Server listening on port 9999...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

main()
