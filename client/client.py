import socket
import os


sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '../server/udp_socket_file'
client_address = '../client/udp_client_socket_file'

message = input().encode()

try:
    os.unlink(client_address)
except FileNotFoundError as err:
    print(err)
    os.exit(1)

sock.bind(client_address)

try:
    # メッセージの送信
    print('sending {!r}'.format(message))
    sock.sendto(message, server_address)

    # サーバからの応答待ち
    print('waiting to receive')

    data, server = sock.recvfrom(4096)

    print('received :{!r}'.format(data.decode('utf-8')))

finally:
    print('closing socket')
    sock.close()
