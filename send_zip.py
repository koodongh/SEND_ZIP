import socket

HOST = '202.31.34.154'  # 수신 서버의 IP 주소
PORT = 51906  # 사용할 포트 번호

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    with open('/root/log.tgz', 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)
    
    print("파일 전송 완료")

print("클라이언트 종료")
