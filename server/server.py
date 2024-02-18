import socket
import os
from faker import Faker

fake = Faker('ja-JP')

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = './udp_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError as err:
    print(err)
    os.exit(1)

print('starting up on {}'.format(server_address))

sock.bind(server_address)

while True:
    # データを受信
    print('waiting to receive message')
    data, address = sock.recvfrom(1024)

    print('received this message "{} "  from {}'.format(data.decode('utf-8'), address))

    message = 'hi! ' + fake.name()
    # データを送信
    if data:
        sent = sock.sendto(message.encode(), address)

        print('sent {} bytes back to {}'.format(sent, address))