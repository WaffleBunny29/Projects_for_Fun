#!/usr/bin/env python3

#WSL1:
#export DISPLAY=localhost:0


import sys, pygame
pygame.init()

pygame.display.set_caption("Ranjitha's Journey")
clock = pygame.time.Clock() 

screen = pygame.display.set_mode((500,500))

sky = pygame.image.load("sky.png").convert()
ground = pygame.image.load("ground2.png").convert()
enemy = pygame.image.load("book.png").convert_alpha()
enemy_rect = enemy.get_rect(midbottom = (400,410))
text_format = pygame.font.Font('game-played-font/font.ttf',20)
text = text_format.render('Bachelor of Biomedical Engineering',False,'black')
player_ran = pygame.image.load("ran2.png")
rect = player_ran.get_rect(midbottom = (80,425))

vel =15 # moves char by 10 pixels for every iteration in the while loop


while True:
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,400))
    screen.blit(text,(75,50))
    #enemy_rect -=20
    #if enemy_rect<=-50:
    #	enemy_rect=550
    screen.blit(enemy,enemy_rect)
    screen.blit(player_ran, rect)
    
    pygame.time.delay(100)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    get_input = pygame.key.get_pressed()
    if get_input[pygame.K_LEFT]:
    	rect.x -=vel
    if get_input[pygame.K_RIGHT]:
    	rect.x +=vel
    if get_input[pygame.K_UP]:
    	rect.y-=vel
    if get_input[pygame.K_DOWN]:
    	rect.y+=vel
	
    pygame.display.update()
    clock.tick(50)
    pygame.display.flip()
    