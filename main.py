from time import sleep
import os
from datetime import datetime

counter = 10

def padre():
    for i in range(counter):
        
        pid = os.fork()
        if pid == 0:
            hijo()
        else:
            sleep(10)
def hijo():
    now = datetime.now()
    print("Iniciando proceso hijo con pid:", os.getpid(), "a las:", now.hour ,":", now.minute , ":" , now.second)
    sleep(3)
    print("Terminando el proceso con pid :", os.getpid())
    os._exit(0)

if __name__ == "__main__":
    padre()