import pygame
pygame.init()
screen=pygame.display.set_mode((600,300))
colors=(0,0,0)
pygame.display.set_caption(f'Az ablak háttérszínének RGB értéke: {colors}')

RED=(255,0,0)
GRAY=(100,100,100)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(250,250,0)
backround=('white')

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                backround=RED
                colors=RED
            elif event.key==pygame.K_g:
                backround=GREEN
                colors=GREEN
            elif event.key==pygame.K_b:
                backround=BLUE
                colors=BLUE
            elif event.key==pygame.K_y:
                backround=YELLOW
                colors=YELLOW
    pygame.display.set_caption(f'Az ablak háttérszínének RGB értéke: {colors}')
    pygame.display.update()
    screen.fill(backround)


pygame.quit()
