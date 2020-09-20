import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = sock.bind(('localhost', 9000))
sock.listen(1)

message = "Ola Cliente"
message_size = len(message)

print("Aguardando conexao")
connection, address_client = sock.accept()    
connection.sendall(str(message_size).zfill(4).encode())
connection.sendall(message.encode())

while True:
    expected_data_size = ''

    while(expected_data_size == ''):
        expected_data_size += connection.recv(4).decode()
        expected_data_size = int(expected_data_size)
        received_data = ''

    while len(received_data) < expected_data_size:
        received_data += connection.recv(4).decode()
    print(received_data)

    if received_data == 'see ya':
        connection.close()

    time.sleep(3)

    message = raw_input("servidor: ").strip()
    send_data_size = len(message)
    connection.sendall(str(send_data_size).zfill(4).encode())
    connection.sendall(message.encode())

    if message == 'see ya':
        connection.close()
