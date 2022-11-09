import pygame
from random import randrange

res = 800
size = 40

x = randrange(0, res, size)
y = randrange(0, res, size)
apple = randrange(0, res, size), randrange(0, res, size)
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
length_snake = 1
snake = [(x,y)]
dx = 0
dy = 0
fps = 3
score = 0

pygame.init()
window = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()
#our inscriptions for the game
front_score = pygame.font.SysFont('Arial', 17, bold = True)
front_end = pygame.font.SysFont('Arial', 60, bold = True)

img = pygame.image.load('4.jpg').convert()
#display of game objects
while True:
    window.blit(img, (0,0))
    [(pygame.draw.rect(window, pygame.Color('light blue'), (i, j, size - 2, size - 2))) for i,j in snake]
    pygame.draw.ellipse(window, pygame.Color('pink'), (*apple, size, size))
    #game score
    render_score = front_score.render(f'СЧЕТ: {score}', 1, pygame.Color('white'))
    window.blit(render_score, (3,3))
    #how does a snake grow
    x += dx * size
    y += dy * size
    snake.append((x,y))
    snake = snake[-length_snake:]
    #apple eating mechanism
    if snake[-1] == apple:
        apple = randrange(0, res, size), randrange(0, res, size)
        length_snake += 1
        fps += 0.5
        score += 1
    #losing conditions
    if x < 0 or x > res - size \
            or y < 0 or y > res - size\
            or len(snake) != len(set(snake)):
        while True:
            render_end = front_end.render('ВЫ ПРОИГРАЛИ!', 1, pygame.Color('red'))
            window.blit(render_end, (res // 2 - 250, res // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #snake locomotion
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True}
    elif key[pygame.K_s] and dirs['S']:
        dirs = {'W': False, 'A': True, 'S': True, 'D': True}
        dx, dy = 0, 1
    elif key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False}
    elif key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True}







