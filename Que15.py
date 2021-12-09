#Questão 15
import subprocess
import time

import psutil

proc = subprocess.Popen('calc')
pid = proc.pid
p = psutil.Process(pid)
tempo = p.create_time()
tempo2 = time.ctime(tempo)
memoria = p.memory_info()

print(f"O dono do processo é {p.username()}")
print(f"A data de criação do processo é: {tempo2}")
print(f"O uso da memória em KB:{memoria}")