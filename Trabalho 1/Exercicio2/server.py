# OBJETIVO: Um programa servidor que envia duas questoes de multipla escolha para um cliente.

# O QUE SERÁ FEITO: Será feito um quiz sobre Harry Potter.

# ----------SERVIDOR----------
import socket
from utils import carregarQuestoes, numeroDeQuestoes, comparar

print("Servidor...")

# Endereco IP do Servidor
HOST = socket.gethostname()       
# Porta do Servidor
PORT = 57000         

# Realizando configurações
SocketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SocketServidor.bind((HOST,PORT)) # Associando o servidor ao endereço e porta
SocketServidor.listen(1) # Maximo um cliente na fila
SocketServidor.settimeout(100) # Tempo de espera

# Conexão com o cliente
clienteSocket, enderecoCliente = SocketServidor.accept()

# Numero de questoes
numeroDeQuestoes = numeroDeQuestoes()

# Arrays auxiliares
escolhasCliente = []
respostasCorretas = []

# Enviando a primeira pergunta
clienteSocket.send(numeroDeQuestoes.encode())

for i in range(int(numeroDeQuestoes)):   

    # Recebendo a questão e a resposta correta para a mesma
    questao, resposta = carregarQuestoes(i)

    # Enviando a questão para o cliente para que ele escolha uma alternativa
    clienteSocket.send(questao.encode())

    # Aguardando escolha do cliente
    opcao = int(clienteSocket.recv(1024).decode())

    print(f'Escolha = {opcao}')
    print(f'Resposta = {resposta}')

    # Adicionando as escolhas e as respostas os arrays correspondentes
    escolhasCliente.append(opcao)
    respostasCorretas.append(resposta)

resposta = comparar(escolhasCliente, respostasCorretas)

# Enviando o gabarito 
clienteSocket.send(resposta.encode())

# Fechando conexão
SocketServidor.close()


