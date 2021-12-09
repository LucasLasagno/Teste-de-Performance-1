#Questão 19

import psutil

def part_livre():
    system = psutil.disk_usage('C:')
    disp = system[2] / (1024 * 1024 * 1024)
    print(round(disp, 2), "GB")

part_livre()








