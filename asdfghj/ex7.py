import sys, time
#from pygame import mixer
import pygame
from pygame.locals import *

def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Sound(file).play()
    time.sleep(5)
    
if __name__  == "__main__":
	pmusic('elec.wav')

