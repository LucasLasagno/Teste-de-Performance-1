#Questão 13
import subprocess
import psutil

proc = subprocess.Popen('calc')
pid = proc.pid
p = psutil.Process(pid)

print(f"O processo:{p.name()} possui o PID {pid}.")


