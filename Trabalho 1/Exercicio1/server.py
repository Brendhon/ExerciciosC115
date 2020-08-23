# OBJETIVO: Criar um chatbot que atende um cliente e envia algumas mensagens para ajudar o mesmo.

# INSPIRAÇÃO: Em 2018 o G1 trouxe informações para o público sobre os candidatos à Presidência através de um Chatbot.

# O QUE SERÁ FEITO: O chatbot trará informações sobre candidatos para eleições.

# ----------SERVIDOR----------
import socket
from utils import carregarJSON, mensagemInicial

print("Servidor...")

# Carregando a lista de candidatos
candidatos = carregarJSON()

# Endereco IP do Servidor
HOST = socket.gethostname()       
# Porta do Servidor
PORT = 57000                                            

# Realizando configurações
SocketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SocketServidor.bind((HOST,PORT)) # Associando o servidor ao endereço e porta
SocketServidor.listen(1) # Maximo um cliente na fila
SocketServidor.settimeout(100) # Tempo de espera

# Mensagens do Chatbot
primeiraPergunta = mensagemInicial(candidatos)
segundaPergunta = "\n0 - Para sair \n1 - Propostas \n2 - Sobre"
mensagemDespedida = "\n\nVote consciente! :)"

# Conexão com o cliente
clienteSocket, enderecoCliente = SocketServidor.accept()

# Enviando a primeira pergunta
clienteSocket.send(primeiraPergunta.encode())

# Aguardando resposta
candidatoEscolhido = int(clienteSocket.recv(1024).decode()) - 1

# Enviando a segunda pergunta
clienteSocket.send(segundaPergunta.encode())

# Aguardando resposta
opcao = clienteSocket.recv(1024).decode()

if opcao == '1':
    # Trasformando a lista em String e a enviando codificada
    clienteSocket.send('\n'.join(candidatos[candidatoEscolhido]['propostas']).encode())
elif opcao == '2': 
    # Trasformando a lista em String e a enviando codificada
    clienteSocket.send('\n'.join(candidatos[candidatoEscolhido]['descricao']).encode())

# Enviando a mensagem de despedida
clienteSocket.send(mensagemDespedida.encode())
        
# Encerrando conexão
print("Fechando conexão...")
SocketServidor.close()