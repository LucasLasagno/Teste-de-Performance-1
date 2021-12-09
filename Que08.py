#Questão 08

import os
arch = input("Informe o nome do arquivo:")
os.stat(arch)
bytes = os.stat(arch).st_size
KB = bytes/1024
print(f"O arquivo informado {arch} possui o tamanho de {KB} KB.")