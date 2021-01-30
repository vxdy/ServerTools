import socket
import os
import time
import shutil

host = "0.0.0.0"
transfer_folder = r'\home\pi\Transfer'
seperator = "<-->"
port = 4665
buffer = 1024

while True:
    time.sleep(3)
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print("Server open...")
    client_socket, address = s.accept()
    file, file_size = client_socket.recv(buffer).decode().split(seperator)

    file_name = os.path.basename(file).split("\\")[-1]
    file_size = int(file_size)
    with open(file_name, "wb") as f:
        bytes_recv = client_socket.recv(buffer)
        while bytes_recv:
            f.write(bytes_recv)
            bytes_recv = client_socket.recv(buffer)
    client_socket.close()
    s.close()
    try:
        shutil.move(r"/home/pi/"+file_name, transfer_folder)
    except shutil.Error:
        pass
    print(f"{address} sent a file Name: {file_name} Size: {file_size}")
    time.sleep(3)
