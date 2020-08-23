import json

# Função para carregar o arquivo JSON e trasforma-lo em lista
def carregarJSON():

    # Lendo o arquivo JSON
    with open('questions.json') as json_data:
        questoes = json.load(json_data)
        json_data.close()
    
    return questoes

# Adaptar a mensagem de questão para o numero de questões
def carregarQuestoes(id):

    questoesAux = carregarJSON()[id]

    alternativaString =  f'\n{questoesAux["id"]}°) {questoesAux["titulo"]}\n'
    respostaCorreta = questoesAux["respostaCorreta"]
    possiveisRespostas = questoesAux["possiveisRespostas"]

    for alternativa in possiveisRespostas:
        alternativaString =  alternativaString +  f'\n{alternativa["numeroDeIdentificacao"]}) {alternativa["descricao"]}'
    
    return alternativaString, respostaCorreta

# Carrega o numero de questões cadastradas e as envia em formato de String
def numeroDeQuestoes():
    numeroDeQuestoes = f'{len(carregarJSON())}'
    return numeroDeQuestoes

# Campara os dois arrays para verificar a resposta e retorna uma string com o gabarito 
def comparar(escolhas, respostas):
    
    i = 0
    mensagens = []
    while i != len(respostas):
        msg = f'\n{i + 1}° Questão) '
        if escolhas[i] == respostas[i]:
            msg = msg + '\033[32mParabéns, sua resposta esta correta!! :) \033[0;0m'
        else:
            msg = msg + f'\033[31mSinto muito, a resposta correta é a alternativa "{respostas[i]}" :( \033[0;0m'
        mensagens.append(msg)
        i = i + 1
        
    return '\n '.join(mensagens)