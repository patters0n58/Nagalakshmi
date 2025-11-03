import socket
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = "127.0.0.1"  
SERVER_PORT = 9999

try:
    client.connect((SERVER_IP, SERVER_PORT))
except Exception as e:
    messagebox.showerror("Connection Failed", f" Could not connect to server:\n{e}")
    exit()



def send_message():
    msg = entry_message.get().strip()
    if msg == "":
        return

    full_msg = f"You: {msg}"
    client.sendall(msg.encode())
    chat_box.insert(tk.END, f"{full_msg}\n")
    entry_message.delete(0, tk.END)

    if msg.lower() == "bye":
        client.close()
        root.destroy()


def receive_messages():
    while True:
        try:
            data = client.recv(1024).decode()
            if data == "NICK":
                client.send(nickname.encode())
            else:
                chat_box.insert(tk.END, f"Server: {data}\n")
        except:
            print(" Disconnected from server.")
            client.close()
            break



root = tk.Tk()
root.title("WeChat")
root.geometry("600x400")
root.configure(bg="#1E1E1E")

tk.Label(root, text="WeChat Client", font=("Segoe UI", 16, "bold"), fg="#00FFAA", bg="#1E1E1E").pack(pady=10)

chat_box = tk.Text(root, height=15, width=70, font=("Consolas", 10), bg="#2B2B2B", fg="white", wrap="word")
chat_box.pack(pady=10)


frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(pady=5)

entry_message = tk.Entry(frame, width=50, font=("Segoe UI", 11))
entry_message.grid(row=0, column=0, padx=10)

nickname = simpledialog.askstring("Nickname", "Choose your nickname:")

send_button = tk.Button(
    frame,
    text="Send",
    font=("Segoe UI", 11, "bold"),
    bg="#00FFAA",
    fg="#1E1E1E",
    activebackground="#00CC88",
    activeforeground="white",
    width=10,
    command=send_message
)
send_button.grid(row=0, column=1)


threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
