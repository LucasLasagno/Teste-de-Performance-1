#Questão 4
import os

def obtem_caminho():
    print("A função usada para se obter o caminho absoluto é o path.")
    print("Ex:")
    caminho = os.getcwd()
    print(f"O caminho absoluto do diretório é {os.path.dirname(caminho)}")
obtem_caminho()
