#Questão 17

import psutil, time

psutil.cpu_times_percent()
for i in range(20):
    time.sleep(1)
    print(psutil.cpu_times_percent())


