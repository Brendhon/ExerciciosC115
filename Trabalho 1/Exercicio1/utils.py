import json

# Função para carregar o arquivo JSON e trasforma-lo em lista
def carregarJSON():

    # Lendo o arquivo JSON com os candidatos
    with open('candidates.json') as json_data:
        candidatos = json.load(json_data)
        json_data.close()
    
    return candidatos

# Adaptar a mensagem inicial para o numero de candidatos
def mensagemInicial(candidatos):
    
    mensagemInicial = "\nBom dia, sobre qual candidato gostaria de receber mais informações?\n"
    for candidato in candidatos:
        mensagemInicial = mensagemInicial + f'\n{candidato["id"]} - {candidato["nome"]}'

    return mensagemInicial
    