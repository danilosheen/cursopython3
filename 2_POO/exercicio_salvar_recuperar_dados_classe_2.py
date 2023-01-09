import json
from exercicio_salvar_recuperar_dados_classe import CAMINHO_ARQUIVO, Pessoa


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
        
        
print(p1.nome, p2.nome, p3.nome)