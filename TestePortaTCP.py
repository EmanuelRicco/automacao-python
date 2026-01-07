import socket
import sys

def main():
    host = '0.0.0.0'  # Escuta em todas as interfaces de rede
    port = int(sys.argv[1])  # Porta que o serviço irá escutar

    # Cria um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Associa o socket à porta
        s.bind((host, port))
        # Começa a escutar por conexões
        s.listen()

        print(f'Serviço rodando e escutando na porta {port}')

        # Aceita conexões entrantes
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__":
    main()