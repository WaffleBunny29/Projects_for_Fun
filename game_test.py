#!/usr/bin/env python3

import sys, pygame
pygame.init()

pygame.display.set_caption("Ranjitha's Journey")
ran = pygame.image.load("ran.png")

rect = ran.get_rect()
screen = pygame.display.set_mode((500,500))
bg = pygame.image.load("bg_small.png")

vel =10 # moves char by 10 pixels for every iteration in the while loop


while True:
    screen.blit(bg,(0,0))
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
        	sys.exit()
    get_input= pygame.key.get_pressed()
    if get_input[pygame.K_LEFT]:
    	rect.x -=vel
    if get_input[pygame.K_RIGHT]:
    	rect.x +=vel
    if get_input[pygame.K_UP]:
    	rect.y-=vel
    if get_input[pygame.K_DOWN]:
    	rect.y+=vel
	

    screen.blit(ran, rect)
    pygame.display.flip()
    