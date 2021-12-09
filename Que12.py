#Questão 12

import subprocess
import os


def use_OS():
    os.system("calc")

def use_SUBPROCESS():
    print(subprocess.run(["notepad", "arq_texto.txt"]))

use_OS()
use_SUBPROCESS()

