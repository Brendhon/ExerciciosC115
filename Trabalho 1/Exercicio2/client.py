# OBJETIVO: Um programa servidor que envia duas questoes de multipla escolha para um cliente.

# O QUE SERÁ FEITO: Será feito um quiz sobre Harry Potter.

# ----------CLIENTE----------
import socket

# Endereco IP do Servidor
serverHOST = socket.gethostname()          
# Porta do Servidor
serverPORT = 57000     

# Configuração da conexão
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverHOST,serverPORT))
clientSocket.settimeout(100) 

# Recebendo o numero de questões presentes
num = int(clientSocket.recv(1024).decode())

# Respondendo o Quiz
for i in range(num):

    # Recebendo e mostrando a questão
    questao = clientSocket.recv(1024).decode()
    print(questao) 

    # Escolhendo e enviando a resposta
    opcao = input('\nEntre com numero de sua opção: ')
    clientSocket.send(opcao.encode())

# Recebendo e mostrando o gabarito 
gabarito = clientSocket.recv(1024).decode()
print(gabarito)

# Fechando conexão
clientSocket.close()