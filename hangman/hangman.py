import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

list = ["speed","alive","school","table","project","travel","construction","architect","alligator"]
word = random.choice(list)
print(word)

point = 0
x= len(word)
mask= "____________________"

big_font = pygame.font.Font('Pixeltype.ttf', 50)
small_font = pygame.font.Font('Pixeltype.ttf',25)


lives = 3

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if lives == 4:
        start_surface = big_font.render(f'Press Sapce to start.',False,'Green')
        start_rect = start_surface.get_rect(center = (200,200))
        screen.blit(start_surface,start_rect)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            lives = 3
            
    
    if lives == 3:
        while True:
            word_surface = big_font.render(f'{mask}',False,'Red')
            word_rect = word_surface.get_rect(center = (200,200))
            screen.blit(word_surface,word_rect)
            enter_surface = small_font.render("Enter a letter to guess: ",False,('Yellow'))
            enter_rect = enter_surface.get_rect(center = (200,400))
            screen.blit(enter_surface,enter_rect)
            guess = input()
            letter_surface = small_font.render(f"{guess}",False,'Blue')
            letter_rect = letter_surface.get_rect(center = (315,400))
            screen.blit(letter_surface,letter_rect)

            c = 0
            for i in range(x):
                if word[i] == guess:
                    mask = mask[:i] + guess + mask[i+1:]
                    c +=1
            
            if guess in word:
                point += c
                
                print("Right letter, guess another.")
            if point == x:
                print(f"You win, word is {word}.")
                break
            elif guess not in word:
                print("Wrong guess, try again.")
                lives -= 1
            if lives == 0:
                break
    
    
    
    
    
    pygame.display.update()
    clock.tick(60)