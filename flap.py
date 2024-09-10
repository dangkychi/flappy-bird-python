#import libary
import pygame
import time
import random
from pygame import mixer

pygame.init()

white=pygame.color.Color(255,255,255)
green =pygame.color.Color(0,255,0)

window_x=1024
window_y=768

#create window game
res=(1024,768)
screen = pygame.display.set_mode((window_x,window_y))

score=0
highscore=0

game_font=pygame.font.Font('04B_19.TTF',50)
def show_score():
    if gameplay:
        score_font = game_font.render('SCORE: '+ str(int(score)),True,white)
        score_rect = score_font.get_rect()
        score_rect.midtop=(window_x/2,0)
        screen.blit(score_font,score_rect)

def show_highscore():
    if gameplay== False:

        score_font = game_font.render('SCORE: '+ str(int(score)),True,white)
        score_rect = score_font.get_rect()
        score_rect.midtop=(window_x/2,0)
        screen.blit(score_font,score_rect)

        highscore_font = game_font.render('HIGHSCORE: '+ str(int(highscore)),True,green)
        highscore_rect = highscore_font.get_rect()
        highscore_rect.midtop=(window_x/2,100)
        screen.blit(highscore_font,highscore_rect)

pygame.display.set_caption('flappy bird')

icon=pygame.image.load(r'images\bird2.png')
pygame.display.set_icon(icon)

bg=pygame.image.load(r'images\bg1.png')
bg2=pygame.image.load(r'images\\floor.png')
bg2_x=0
bird=pygame.image.load(r'images\bird2.png')
bird=pygame.transform.scale2x(bird)
bird_rect=bird.get_rect(center=(150,315))
gover=pygame.image.load(r'images\\gameover.png')
gover=pygame.transform.scale2x(gover)

def music(url):
    bulletSound = mixer.Sound(url)
    bulletSound.play()

def colunm(self):
        maginColunm = 80
        yColunmChangeTop = -self.ySizeColunm/2 - maginColunm + \
            self.colunmChange   # Khoảng cách giữa cột trên và đưới là 80*2
        yColunmChangeBotton = self.ySizeColunm/2 + maginColunm+self.colunmChange
        self.image_draw(r'images\barrier1.png', self.xColunm,
                        yColunmChangeTop, self.xSizeColunm, self.ySizeColunm)
        self.image_draw(r'images\barrier2.png', self.xColunm,
                        yColunmChangeBotton, self.xSizeColunm, self.ySizeColunm)
        self.xColunm = self.xColunm - self.Vcolunm
        if self.xColunm < -100:  # Nếu cột đi qua màn hình
            self.xColunm = self.xScreen  # Tạo cột mới
            # Random khoảng cách cột
            self.colunmChange = random.randint(-150, 150)
            self.scores += 1
        return yColunmChangeTop+self.ySizeColunm, yColunmChangeBotton  # Trả về vị trí hai cột

p=0.1
bird_y=0

def check_bird():
    if bird_rect[1] < 0 or bird_rect[1] > window_y:
        return False
    else:
        return True

gameplay=True
play=True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           play=False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                music(r'sound\sfx_hit.wav')
            if event.key == pygame.K_SPACE and gameplay:
                bird_y -= 7
            if event.key == pygame.K_SPACE and gameplay==False:
                gameplay = True
                bird_y=0
                bird_rect.center=(150,315)

    
    screen.blit(bg,(0,0))
    bg2_x -=1
    screen.blit(bg2,(bg2_x,620))
    screen.blit(bg2,(bg2_x+336,620))
    screen.blit(bg2,(bg2_x+672,620))
    screen.blit(bg2,(bg2_x+1008,620))
    screen.blit(bg2,(bg2_x+1344,620))
    if bg2_x == -336:
        bg2_x = 0

    if gameplay:

        screen.blit(bird,bird_rect)
        bird_y += p
        bird_rect.centery += bird_y
        score += 0.01
        if score > highscore:
            highscore = score
        show_score()
        gameplay = check_bird()
    
    else:
        screen.blit(gover,(window_x/3,window_y/3))
        show_score()
        show_highscore()
        


    pygame.display.update()