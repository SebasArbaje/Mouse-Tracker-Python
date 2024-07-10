import time

import pygame

x = y = 0
running = 1
pygame.init()

print("Starting Mouse Tracker Vol 2")

time.sleep(1)
screen = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont(None, 30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    x, y = pygame.mouse.get_pos()

    text_X_image = font.render(f'X: {x}', True, (255,255,255))
    text_X_rect  = text_X_image.get_rect()
    text_X_rect.x = x + 10 
    text_X_rect.y = y + 10
 
    text_Y_image = font.render(f'Y: {y}', True, (255,255,255))
    text_Y_rect  = text_Y_image.get_rect()
    text_Y_rect.x = x + 10 
    text_Y_rect.y = y + 10 + 25

    # --- draw ---

    screen.fill((0,0,0))
 
    screen.blit(text_X_image, text_X_rect)
    screen.blit(text_Y_image, text_Y_rect)
    
    pygame.draw.line(screen, (255, 0, 0), (0, y), (800, y))
    pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, 600))
    
    pygame.display.flip()