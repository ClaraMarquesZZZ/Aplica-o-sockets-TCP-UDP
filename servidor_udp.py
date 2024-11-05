import socket


def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5001))

    print("Servidor UDP aguardando mensagens na porta 5001...")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Mensagem recebida de {client_address}: {message.decode()}")

        response = f"UDP: {message.decode()}"
        server_socket.sendto(response.encode(), client_address)


if __name__ == "__main__":
    start_udp_server()
