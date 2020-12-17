from pygame import mixer
from datetime import datetime

def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a = input()
        if a==stopper:
            mixer.music.stop()
            break

def log():
    with open('log.txt','a') as f:
        dtmn = datetime.now()
        f.write(f'Water : {dtmn}\n')

if __name__ == '__main__':
    log()
    musicloop('elec.wav','stop')
    
