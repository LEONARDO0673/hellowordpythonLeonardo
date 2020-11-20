#08:49:49 pm
import time
contador = 0
while True:
    hora_actual = time.localtime()
    reloj = time.strftime("%I:%M:%S", hora_actual)
    print(reloj,end="",flush=True)
    print("\r",end="",flush=True)
    time.sleep(1)
    contador +=1
    if contador ==60:
        break
