import pygame
from Paddle import Paddle
from Ball import Ball
from pygame import mixer
from random import randint

pygame.init()
mixer.init()
mixer.music.load('epic.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(100)
isPaused = False
playerLost = False

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (600, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

 
paddleA = Paddle(WHITE, 10, 100)
paddleB = Paddle(WHITE, 10, 100)
ball = Ball(WHITE,10,10)

sprites_list = pygame.sprite.Group()
 
gameLoop = True
 
clock = pygame.time.Clock()
 
scoreA = 0
scoreB = 0

def init():
    screen.fill(BLACK)
    playerLost = False
    scoreA = 0
    scoreB = 0
    paddleB.rect.x = 580
    paddleB.rect.y = 200
    paddleA.rect.x = 10
    paddleA.rect.y = 200
    sprites_list.add(paddleA)
    sprites_list.add(paddleB)
    sprites_list.add(ball)
    pygame.display.flip()
    mixer.music.load('epic.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    gameLoop = True
    print(playerLost)
    print(gameLoop)

init()
 
while gameLoop:
    pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
              gameLoop = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     gameLoop=False
 
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
 
 
    sprites_list.update()
    
    #Check if the ball is bouncing against any of the walls:
    if ball.rect.x>=595:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
 
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    
    paddleB.rect.y = (ball.rect.y - 50)

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [305, 0], [305, 500], 5)
    
    sprites_list.draw(screen) 
 
    font = pygame.font.Font('Shitzu.ttf',75)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (335,10))
    
    if(scoreB > 9 or scoreA > 9):
          gameOver = True
          mixer.music.stop()
          mixer.music.load('nevergonnagive.mp3')
          mixer.music.set_volume(0.2)
          mixer.music.play()
          screen.fill(BLACK)
          result = ("Player 1 wins." if (scoreA > scoreB) else "Player 2 wins.")
          text = font.render(result, 1, WHITE)
          screen.blit(text, (50,100))
          text = font.render("Enjoy Rick Astley.", 1, WHITE)
          screen.blit(text, (50,200))
          text = font.render("Press r to exit.", 1, WHITE)
          screen.blit(text, (50,300))
          gameLoop = False
 

    pygame.display.flip()
     
    clock.tick(60)
while gameOver:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                gameLoop = True
                gameOver = False
                pygame.quit()