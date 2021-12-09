#Questão 18
import psutil

def mem_fis():
    fisica = psutil.virtual_memory()
    total = fisica[0]/(1024*1024*1024)
    print(round(total,2),"GB")

def mem_swap():
    swap = psutil.swap_memory()
    total2 = swap[0]/(1024*1024*1024)
    print(round(total2,2),"GB")

mem_fis()
mem_swap()