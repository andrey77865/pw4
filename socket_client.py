import socket


def run_client(ip, port, send_data):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        server = ip, port
        sock.sendto(send_data, server)
        sock.close()
        print('socket client closed')
