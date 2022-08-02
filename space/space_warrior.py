import pygame
from random import randint
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sapce Warrior")

back = pygame.image.load('data/back.png')
ufo = pygame.image.load('data/ufo.png')
pygame.display.set_icon(ufo)

bg_music = pygame.mixer.Sound('data/background.wav')
bg_music.play(loops = -1)

lives = -1
start_time = 0

#texts
big_font = pygame.font.Font('data/Pixeltype.ttf',75)
mid_font = pygame.font.Font('data/Pixeltype.ttf',50)
small_font = pygame.font.Font('data/Pixeltype.ttf',25)

#Enemy
enemy_x = [0,0,0,0,0,0,0]
enemy_y = [0,0,0,0,0,0,0]
enemy_rect = [0,0,0,0,0,0,0]
enemy_surface = pygame.image.load('data/enemy.png').convert_alpha()

for i in range(7):
    enemy_x[i] = randint(25,775)
    enemy_y[i] = randint(-250,250)
    enemy_rect[i] = enemy_surface.get_rect(center = (enemy_x[i],enemy_y[i]))
    
def enemy(enemy_x,enemy_y):
    
    for i in range(7):
        screen.blit(enemy_surface,enemy_rect[i])
        enemy_rect[i].y += randint(3,5)
        if enemy_rect[i].y > 605:
            enemy_rect[i].y = -2
        if i%2==0:
            enemy_rect[i].x +=3
            if enemy_rect[i].x > 805:
                enemy_rect[i].x= -5
                
        else:
            enemy_rect[i].x -=3
            if enemy_rect[i].x < -5:
                enemy_rect[i].x = 805

#ufo/player    
ufo_surface = pygame.image.load('data/ufo.png').convert_alpha()
ufo_rect = ufo_surface.get_rect(center = (400,500))
ufo_x=ufo_rect.x
ufo_y=ufo_rect.y    
ball_surface = pygame.image.load('data/ball.png').convert_alpha()
ball_rect = ball_surface.get_rect(center = (400,500))

def player(ufo_x,ufo_y):
    screen.blit(ufo_surface,(ufo_rect.x,ufo_rect.y))    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and ufo_rect.x>25:
            ufo_rect.x -= 5
            if fire ==0:
                ball_rect.x -=5
        if event.key == pygame.K_RIGHT and ufo_rect.x<725:
            ufo_rect.x += 5
            if fire == 0:
                ball_rect.x +=5
    
#ball
fire = 0
shot = 0
over_s= 0
#score
def display_score():
	current_time = pygame.time.get_ticks() - start_time
	score_surf = small_font.render(f'Score: {current_time+shot}',False,('Yellow'))
	score_rect = score_surf.get_rect(center = (125,50))
	screen.blit(score_surf,score_rect)
	return current_time

#main loop   
while True:
    screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    if lives == -1:
        
        play_surface = big_font.render('     SPACE',False,'Green')
        play_surfacen = big_font.render('WARRIOR',False,'Green')
        play_rect = play_surface.get_rect(center = (350,150))
        play_rectn = play_surfacen.get_rect(center = (400,225))
        screen.blit(play_surfacen,play_rectn)
        screen.blit(play_surface,play_rect)
        
        info_surface = mid_font.render('Press Up to play.',False,'Blue')
        info_rect = info_surface.get_rect(center = (400,400))
        screen.blit(info_surface,info_rect)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                start_time = pygame.time.get_ticks()
                lives = 3
        
    if lives > 0:
        over=0
        player(ufo_rect.x,ufo_rect.y)
        enemy(enemy_x,enemy_y)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fire = 1
        if fire == 1:
            screen.blit(ball_surface,ball_rect)
            ball_rect.y -=5
            if ball_rect.y < 0:
                ball_rect.y = ufo_rect.y
                ball_rect.x = ufo_rect.x
                fire =0   
                        
        lives_surface = small_font.render(f'Lives: {lives}',False,'red')
        lives_rect = lives_surface.get_rect(center = (700,50))
        screen.blit(lives_surface,lives_rect)
        
        for i in range(7):
            if ufo_rect.colliderect(enemy_rect[i]):
                exp = pygame.mixer.Sound('data/bang.wav')
                exp.play()
                enemy_x[i] = randint(25,775)
                enemy_y[i] = randint(-200,200)
                enemy_rect[i] = enemy_surface.get_rect(center = (enemy_x[i],enemy_y[i]))
                lives -= 1
            
            if ball_rect.colliderect(enemy_rect[i]):
                exp = pygame.mixer.Sound('data/bang.wav')
                exp.play()
                fire =0
                shot += 3000
                enemy_x[i] = randint(25,775)
                enemy_y[i] = randint(-300,300)
                enemy_rect[i] = enemy_surface.get_rect(center = (enemy_x[i],enemy_y[i]))
                ball_rect = ball_surface.get_rect(center = ufo_rect.center)
                
        score = display_score()
                    
    if lives == 0:
        
        while over_s==0:
            over = pygame.mixer.Sound('data/over.wav')
            over.play()
            over_s +=1
        
        play_surface = big_font.render('GAME OVER',False,'Red')
        play_rect = play_surface.get_rect(center = (400,200))
        screen.blit(play_surface,play_rect)
        
        score_message = mid_font.render(f'Your score: {score}',False,('Yellow'))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(score_message,score_message_rect)
        screen.blit(info_surface,info_rect)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                start_time = pygame.time.get_ticks()
                lives = 3
                shot = 0
                fire = 0
                        
    pygame.display.update()
    clock.tick(60)