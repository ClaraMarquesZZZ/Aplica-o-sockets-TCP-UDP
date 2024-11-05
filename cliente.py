import socket


def mensagem_tcp(message):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(('localhost', 5000))
    tcp_socket.send(message.encode())

    response = tcp_socket.recv(1024).decode()
    print("Resposta do servidor: TCP: Olá servidor!", response)

    tcp_socket.close()


def mensagem_udp(message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), ('localhost', 5001))

    response, _ = udp_socket.recvfrom(1024)
    print("Resposta do servidor: UDP: Ping", response.decode())

    udp_socket.close()


if __name__ == "__main__":
    protocolo = input("Escolha o protocolo (TCP/UDP): ").strip().upper()
    mensagem = input("Digite uma mensagem para enviar aos servidores: ")

    if protocolo == "TCP":
        mensagem_tcp(mensagem)
    elif protocolo == "UDP":
        mensagem_udp(mensagem)

    else:
        print("Protocolo inválido. Escolha entre TCP ou UDP.")
