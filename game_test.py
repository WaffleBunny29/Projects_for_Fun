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
enemy_rect = enemy.get_rect(midbottom = (400,400))

text_format = pygame.font.Font('game-played-font/font.ttf',20)
text = text_format.render(' Level1',False,'black')
text_rect = text.get_rect(center = (250,150))

player_ran = pygame.image.load("ran2.png")
rect = player_ran.get_rect(midbottom = (80,400))
gravity = 0


vel =15 # moves char by 10 pixels for every iteration in the while loop


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_SPACE:
	            print('Jump')
        if event.type == pygame.KEYUP:
            print('keyup')

                
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,400))
    pygame.draw.rect(screen,'white',text_rect,0,10)
    pygame.draw.rect(screen,'gold',text_rect,2,5)
    screen.blit(text,text_rect)
    enemy_rect.x -= 20
    if enemy_rect.x <= -50:
    	enemy_rect.x = 550
    screen.blit(enemy,enemy_rect)
    
    # player
    gravity += 10
    rect.y += gravity
    screen.blit(player_ran, rect)
    
    pygame.time.delay(100)
    
    # moving player around   
    get_input = pygame.key.get_pressed()
       	
    if get_input[pygame.K_LEFT]:
    	rect.x -=vel
    if get_input[pygame.K_RIGHT]:
    	rect.x +=vel
    if get_input[pygame.K_UP]:
    	rect.y-=vel
    if get_input[pygame.K_DOWN]:
    	rect.y+=vel
    	
    if rect.colliderect(enemy_rect):
        print('collision')
    	
    pygame.display.update()
    clock.tick(50)
    pygame.display.flip()
    