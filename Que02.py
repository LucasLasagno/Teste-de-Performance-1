#Funções Questão 2

import os

def pergunta_B():
    print("Exemplo de Resposta:")
    print(f"Obtendo o drive: {os.environ['HOMEDRIVE']}")

def pergunta_C():
    print("Exemplo de resposta:")
    print(f"Obtendo o caminho completo do diretório de usuário atual: {os.environ['HOMEPATH']}")

pergunta_B()
pergunta_C()

