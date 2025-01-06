"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
"""
import pygame

pygame.mixer.init()

pygame.mixer.music.load("Bohemian_Rhapsody.mp3")
pygame.mixer.music.play()

input("Você está ouvindo Bohemian Rhapsody, do Queen. Pressione enter para parar a reprodução")

pygame.mixer.music.stop()
