import socket
import threading
import tkinter as tk
from tkinter import messagebox


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP = "138.68.140.83"  
SERVER_PORT = 9999

try:
    client.connect((SERVER_IP, SERVER_PORT))
except Exception as e:
    messagebox.showerror("Connection Failed", f"Could not connect to server:\n{e}")
    exit()

user_id = "Connecting..."

root = tk.Tk()
root.title("WeChat (Private Messaging)")
root.geometry("650x450")
root.configure(bg="#1E1E1E")

label_id = tk.Label(root, text="Connecting...", fg="#00FFAA", bg="#1E1E1E", font=("Segoe UI", 11))
label_id.pack(pady=5)

chat_box = tk.Text(root, height=18, width=75, font=("Consolas", 10), bg="#2B2B2B", fg="white", wrap="word")
chat_box.pack(pady=10)
chat_box.config(state=tk.DISABLED)

frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(pady=5)

entry_message = tk.Entry(frame, width=50, font=("Segoe UI", 11))
entry_message.grid(row=0, column=0, padx=10)


def display_message(msg):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"{msg}\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)


def send_message():
    msg = entry_message.get().strip()
    if not msg:
        return
    try:
        client.sendall(msg.encode("utf-8"))
    except Exception as e:
        messagebox.showerror("Send Error", f"Could not send message:\n{e}")
        return

    entry_message.delete(0, tk.END)
    if msg.lower() == "bye":
        try:
            client.shutdown(socket.SHUT_RDWR)
            client.close()
        except:
            pass
        root.destroy()


send_button = tk.Button(
    frame, text="Send", font=("Segoe UI", 11, "bold"),
    bg="#00FFAA", fg="#1E1E1E", width=10, command=send_message
)
send_button.grid(row=0, column=1)


def receive_messages():
    global user_id
    while True:
        try:
            data = client.recv(1024)
            if not data:
                raise ConnectionError("Server disconnected.")
            msg = data.decode("utf-8", errors="ignore")

            if "Your ID is" in msg:
                user_id = msg.split("Your ID is")[-1].strip()
                label_id.after(0, lambda: label_id.config(text=f"Logged in as {user_id}"))
            else:
                root.after(0, lambda m=msg: display_message(m))

        except ConnectionError:
            root.after(0, lambda: display_message("[System] Connection closed by server."))
            break
        except Exception as e:
            root.after(0, lambda: display_message(f"[Error] {e}"))
            continue

    try:
        client.close()
    except:
        pass
    root.after(0, lambda: display_message("[System] Disconnected."))


threading.Thread(target=receive_messages, daemon=True).start()
root.mainloop()

