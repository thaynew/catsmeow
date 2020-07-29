import pygame
# starts everything up, creates our screen (window)
pygame.init()
screen = pygame.display.set_mode([400,400])
running = True
# this loop runs until the game exits
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       screen.fill((0,0,255))
   pygame.draw.circle(screen, (255,255,0), (200,200), 20)
   pygame.display.flip()
pygame.quit()