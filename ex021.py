'''
Faça um programa em Python que abra e reproduzao áudio de um arquivo MP3.
'''
from time import sleep
import pygame
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer.music.play()
sleep(5)
