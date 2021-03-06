import pygame, sys, random
pygame.init()
from pygame.color import THECOLORS
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for i in range(100):
    width = random.randint(0, 250); height = random.randint(0, 100)
    top = random.randint(0, 400); left = random.randint(0, 500)
    color_name = random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    line_width = random.randint(1, 3)
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)
    pygame.display.flip()
    pygame.time.delay(50)
running = True
while running:
    pygame.display.flip()
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
