import pygame
from pygame.locals import *
from random import randint
import random


pygame.init()


def on_grid_random():
    x = random.randint(0, 30) * 25
    y = random.randint(0, 21) * 25
    return (x, y)

def collision(c1, c2):
    return c1 == c2

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption("Shenlong Game")

comida = pygame.Surface((25, 25))
comida_po = on_grid_random()
cor_comida = [(255, 105, 180), (72, 209, 204), (255, 128, 0), (144, 238, 144)]
comida_cor = random.choice(cor_comida)

snake = [{'position': (200, 200), 'color': ((255, 128, 0))}]
snake_b = pygame.Surface((25, 25))

direction = UP
font = pygame.font.SysFont("Times New Roman", 26)
score = 0
perdeu_playboy = False
snake_speed = 7

timer = pygame.time.Clock()

mensagem_inicio = font.render("Inicie com as teclas WASD", True, (220, 20, 60))

while True:
    timer.tick(snake_speed)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:                 
            if event.key == K_w and direction != DOWN:
                direction = UP
            elif event.key == K_s and direction != UP:
                direction = DOWN
            elif event.key == K_d and direction != LEFT:
                direction = RIGHT
            elif event.key == K_a and direction != RIGHT:
                direction = LEFT

    if not perdeu_playboy:

        if snake[0]['position'][0] < 0 or snake[0]['position'][0] >= 800 or snake[0]['position'][1] < 0 or snake[0]['position'][1] >= 640:
            perdeu_playboy = True

        for i in range(1, len(snake)):
            if collision(snake[0]['position'], snake[i]['position']):
                perdeu_playboy = True


        if collision(snake[0]['position'], comida_po):
            comida_po = on_grid_random()

            if snake[0]['color'] == comida_cor:
                if len(snake) > 1:
                    snake.pop(0)
            else:

                Insere = {'position': snake[-1]['position'], 'color': comida_cor}
                snake.append(Insere)
                score += 1
            comida_cor = random.choice(cor_comida)
            snake_speed += 1

        for i in range(len(snake) - 1, 0, -1):
            snake[i]['position'] = snake[i - 1]['position']

        if direction == UP:
            snake[0]['position'] = (snake[0]['position'][0], snake[0]['position'][1] - 25)
        if direction == DOWN:
            snake[0]['position'] = (snake[0]['position'][0], snake[0]['position'][1] + 25)
        if direction == RIGHT:
            snake[0]['position'] = (snake[0]['position'][0] + 25, snake[0]['position'][1])
        if direction == LEFT:
            snake[0]['position'] = (snake[0]['position'][0] - 25, snake[0]['position'][1])

    
    screen.fill((0, 0, 0))
    screen.blit(comida, comida_po)
    comida.fill(comida_cor)

    for segment in snake:
        snake_b.fill(segment['color'])
        screen.blit(snake_b, segment['position'])

    if perdeu_playboy:
        
        info = font.render("END GAME, SCORE: " + str(score) + " points", True,
                                (220,20,60))
        screen.blit(info, (250, 250))

    txt_score = font.render("SCORE: " + str(score), True, (220,20,60))
    screen.blit(txt_score, (340, 600))

    if not perdeu_playboy and score == 0:
        screen.blit(mensagem_inicio, (0, 0))

        #Juan, Renato e Breno .  - Todos os Direitos Reservados©

    pygame.display.update()