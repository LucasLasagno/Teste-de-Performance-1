#Questão 9

import os
import time

arch = input(str("Informe o nome do arquivo:"))
path = os.path.abspath(arch)

t_s_c = os.path.getctime(arch)
t_s_m = os.path.getmtime(arch)
t_final_criação = time.ctime(t_s_c)
t_final_modificação = time.ctime(t_s_m)
print(f"O arquivo que se encontra em, {path}, foi criado no {t_final_criação} e foi modificado pela última vez em {t_final_modificação}")
