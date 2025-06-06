# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from time import sleep
import pygame

pygame.init()
pygame.mixer_music.load('midia/som.mp3')
pygame.mixer.music.play()
sleep(5)
