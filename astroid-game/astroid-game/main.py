import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}"),
    print(f"Screen width: { SCREEN_WIDTH }"),
    print(f"Screen height: { SCREEN_HEIGHT }")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0


while 1 == 1: 
    log_state()
    for event in pygame.event.get():
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()
        pass
    for event in pygame.event.get():
        dt = clock.tick(60) / 1000
        if event.type == pygame.QUIT:
            break
            
    

if __name__ == "__main__":
    main()
