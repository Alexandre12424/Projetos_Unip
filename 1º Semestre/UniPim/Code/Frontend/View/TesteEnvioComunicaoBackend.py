import socket
import json

HOST = '127.0.0.1'
PORT = 5050

# Mensagem a ser enviada para o servidor C
mensagem = {"acao": "registrar_aula", 
            "turma": "Turma A", 
            "professor": "Prof. Jean", 
            "conteudo": "Matemática"}

# Conecta, envia a mensagem e aguarda uma resposta
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(json.dumps(mensagem).encode('utf-8'))
    resposta = s.recv(4096)
    print("Resposta do servidor C:")
    print(resposta.decode('utf-8'))
