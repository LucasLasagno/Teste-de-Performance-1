#Questão 16

import psutil, time

psutil.cpu_times(percpu = True)
for i in range(10):
    time.sleep(0.1)
    print(psutil.cpu_times(percpu = True))