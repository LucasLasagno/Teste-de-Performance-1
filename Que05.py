#Questão 5
import os
import sys

arch = input("Informe o nome do arquivo:")
path = os.path.abspath(arch)

if(os.path.exists(path)):
  print("O arquivo existe")
else:
  print("O arquivo não existe")
  sys.exit()

if os.path.isfile(arch):
  print("O dado fornecido é um arquivo existente")

