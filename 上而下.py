import pygame
import random

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Feed the blue bird!")


#SET FPS
FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_STARTING_LIVES    = 5
PLAYER_VELOCITY          = 20
COIN_STARTING_VELOCITY   = 10
COIN_ACCELERATION        = 0.5 #加速度
BUFFER_DISTANCE          = 100

score = 0
lives          = PLAYER_STARTING_LIVES
coin_velocity  = COIN_STARTING_VELOCITY

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (206, 222, 225)
DARKBLUE = (30, 60, 130)

font = pygame.font.Font("Exthing.ttf", 32)
font2 = pygame.font.Font("Springtimeromance.ttf", 32)

score_text = font2.render("Score: "+str(score), True, DARKBLUE)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

title_text = font.render("Feed the blue bird", True, DARKBLUE)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH//2
title_text_rect.y = 10

lives_text = font2.render("Lives: "+str(lives), True, DARKBLUE)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH-10, 10)

gameover_text = font.render("GAMEOVER", True, DARKBLUE)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.topright = (WINDOW_WIDTH//2+50, WINDOW_HEIGHT//2)

continue_text = font.render("Press anykey to play again", True, DARKBLUE)
continue_text_rect = continue_text.get_rect()
continue_text_rect.topright = (WINDOW_WIDTH//2+250, WINDOW_HEIGHT//2+40)

coin_sound = pygame.mixer.Sound("bell.wav")
miss_sound = pygame.mixer.Sound("lost.wav")
miss_sound.set_volume(0.1)
pygame.mixer.music.load("backmusic.mp3")

player_image = pygame.image.load("bird.png")
player_rect = player_image.get_rect()
player_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT-32)

coin_image = pygame.image.load("bug.png")
coin_rect = coin_image.get_rect()
coin_rect.x = random.randint(32, WINDOW_WIDTH-32)
coin_rect.y = 67

pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
            
    #Key move
    keys = pygame.key.get_pressed() #偵測目前有哪個案件被按下
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += PLAYER_VELOCITY   
        
    
    #Coin move
    if coin_rect.y > WINDOW_HEIGHT:
        lives -= 1
        miss_sound.play()
        coin_rect.x = random.randint(32, WINDOW_WIDTH-32)
        coin_rect.y = 67
    else:
        coin_rect.y += coin_velocity
    
    
    #Check the collision
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = random.randint(32, WINDOW_WIDTH-32)
        coin_rect.y = 67
        
    #Update the text
    score_text = font2.render("Score: "+str(score), True, BLUE, DARKBLUE)
    lives_text = font2.render("Lives: "+str(lives), True, BLUE, DARKBLUE)
    
    
    #check_for_gameover
    if lives == 0:
        displayscreen.blit(gameover_text, gameover_text_rect)
        displayscreen.blit(continue_text, continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    is_paused = False
                    running = False
                    
                if event.type==pygame.KEYDOWN:
                    score = 0
                    lives = PLAYER_STARTING_LIVES
                    player_rect.centery = WINDOW_HEIGHT-32
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False

        
    displayscreen.fill(BLUE) 
            
    displayscreen.blit(score_text, score_text_rect)
    displayscreen.blit(title_text, title_text_rect)
    displayscreen.blit(lives_text, lives_text_rect)
    pygame.draw.line(displayscreen, WHITE, (0, 64), (WINDOW_WIDTH, 64), 3)
    
    displayscreen.blit(player_image, player_rect)
    displayscreen.blit(coin_image, coin_rect)
    
    pygame.display.update()
    clock.tick(FPS)




pygame.quit()