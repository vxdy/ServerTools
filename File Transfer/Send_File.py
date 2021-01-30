import socket
import os
import time
import shutil

folder_path = r'C:\Users\Vxdy\Desktop\Transfer\\'
sent_folder = r'C:\Users\Vxdy\Desktop\Transfer\Sent\\'
host = "192.168.178.54"
seperator = "<-->"
port = 4665

for file_name in os.listdir(folder_path):
    if os.path.isdir(f"{folder_path}{file_name}"):
        continue
    file_path = folder_path + file_name
    print(file_path)
    file_size = os.path.getsize(file_path)
    if seperator in file_path:
        print("Filename is invalid!!!")
        exit()

    s = socket.socket()
    s.connect((host, port))
    s.send(f"{file_path}{seperator}{file_size}".encode())

    buffer = 1024
    with open(file_path, "rb") as f:
        while True:
            file_bytes = f.read(buffer)
            if not file_bytes:
                break
            s.sendall(file_bytes)
    s.close()
    shutil.move(folder_path+file_name, sent_folder)
    time.sleep(5)
