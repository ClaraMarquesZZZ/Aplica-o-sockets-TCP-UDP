import socket


def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    print("Servidor TCP aguardando conexões na porta 5000...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão estabelecida com {client_address}")

        message = client_socket.recv(1024).decode()
        print(f"Mensagem recebida: {message}")

        response = f"TCP: {message}"
        client_socket.send(response.encode())

        client_socket.close()


if __name__ == "__main__":
    start_tcp_server()
