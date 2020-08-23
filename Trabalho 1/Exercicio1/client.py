# OBJETIVO: Criar um chatbot que atende um cliente e envia algumas mensagens para ajudar o mesmo.

# INSPIRAÇÃO: Em 2018 o G1 trouxe informações para o público sobre os candidatos à Presidência através de um Chatbot.

# O QUE SERÁ FEITO: O chatbot trará informações sobre candidatos (fictícios) para eleições.

# ----------CLIENTE----------
import socket

# Endereco IP do Servidor
serverHOST = socket.gethostname()          
# Porta do Servidor
serverPORT = 57000     

# Configuração da conexão
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverHOST,serverPORT))
clientSocket.settimeout(10) 

# Recebendo primeira pergunta
msg = clientSocket.recv(1024).decode()
print(msg)

# Respondendo primeira pergunta
escolha = input('\nEntre com numero do candidato: ')
clientSocket.send(escolha.encode())

# Recebendo segunda pergunta
msg = clientSocket.recv(1024).decode()
print(msg)

# Respondendo segunda pergunta
opcao = input('\nEntre com numero de sua opcao: ')
print('\n')
clientSocket.send(opcao.encode())

# Recebendo resposta final
msg = clientSocket.recv(1024).decode()
print(msg)

# Recebendo comentario final
msg = clientSocket.recv(1024).decode()
print(msg)

# Encerrando conexão
clientSocket.close()