#!/usr/bin/env python3

#WSL1:
#export DISPLAY=localhost:0


import sys, pygame
pygame.init()

# function
def player_animation():
	global player_ran, player_index
	if rect.bottom < 400:
		player_ran = player_jump
	elif rect.colliderect(enemy_rect):
		player_ran = player_collide
	else:
		player_index += 0.5
		if player_index >= len(player_walk):
			player_index=0
		player_ran = player_walk[int(player_index)]

pygame.display.set_caption("Journey of Knowledge")
clock = pygame.time.Clock() 

screen = pygame.display.set_mode((500,500))

sky = pygame.image.load("sky.png").convert()
ground = pygame.image.load("ground2.png").convert()

enemy = pygame.image.load("book.png").convert_alpha()
enemy_rect = enemy.get_rect(midbottom = (400,400))

text_format = pygame.font.Font('game-played-font/font.ttf',20)

player_walk1 = pygame.image.load("animations/walk1.png").convert_alpha()
player_walk2= pygame.image.load("animations/walk2.png").convert_alpha()
player_walk3= pygame.image.load("animations/walk3.png").convert_alpha()
player_walk = [player_walk1,player_walk2,player_walk3]
player_index = 0
player_ran = player_walk[player_index]
player_jump = pygame.image.load("animations/jump.png").convert_alpha()
player_collide = pygame.image.load("animations/collide.png").convert_alpha()

rect = player_ran.get_rect(midbottom = (80,400))
gravity = 0


vel =15 # moves char by 10 pixels for every iteration in the while loop
game_active = True

count = 0
text = text_format.render(' Score: '+str(count),False,'black')
text_rect = text.get_rect(center = (250,150))

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_SPACE and rect.bottom == 400:
                  gravity = -50
                  count+=1
	
    if game_active:            
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,400))
        pygame.draw.rect(screen,'white',text_rect,0,10)
        pygame.draw.rect(screen,'gold',text_rect,2,5)
        screen.blit(text,text_rect)
        
        text = text_format.render(' Score: '+str(count),False,'black')        
        enemy_rect.x -= 30
        if enemy_rect.x <= -50:
            enemy_rect.x = 550
        screen.blit(enemy,enemy_rect)
        
        # Display player
        gravity += 10
        rect.y += gravity
        if rect.bottom >= 400:
            rect.bottom = 400   
        player_animation() 	
        screen.blit(player_ran, rect)
                
        # moving player around   
        get_input = pygame.key.get_pressed()
        if get_input[pygame.K_LEFT]:
            rect.x -=vel
        if get_input[pygame.K_RIGHT]:
            rect.x +=vel

            
        if rect.colliderect(enemy_rect):
            game_active = False
                   
    else:
    	#screen.fill('pink')
        popup = pygame.image.load('retry.png').convert_alpha()
        popup_rect = popup.get_rect(center = (250,250))
        screen.blit(popup,popup_rect)
        count = 0
    get_input = pygame.key.get_pressed()
    if get_input[pygame.K_RETURN]:
    	enemy_rect = enemy.get_rect(midbottom = (600,400))
    	game_active = True
    	print('return')
    
    pygame.display.update()
    clock.tick(70)
    pygame.display.flip()