import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 32)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0
    score_value = 0
    

    

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids: 
            for shot in shots: 
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    score_value += 10

            if asteroid.collides_with(player):
                sys.exit(f"Game over! \nYour score was: {score_value}")

        screen.fill("lightblue")

        for obj in drawable: 
            obj.draw(screen)

        score_text_surface = font.render(f"Score: {score_value}", True, "white")
        screen.blit(score_text_surface, SCORE_POSITION)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
