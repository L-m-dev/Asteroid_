import pygame
from logger import log_state
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from logger import log_event
from shot import Shot
import sys

def main():
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
        
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable,)
    AsteroidField.containers = (updatable,)
    Shot.containers = (drawable, updatable, shots)
    
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    score = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('black')
        updatable.update(dt)
        
        for a in asteroids:
            
            
            if(p1.collides_with(a)):
                if p1.lives <= 1:
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
                else:
                    p1.lives -=1
                    p1.take_damage(dt)
                    print(f'Current lives: {p1.lives}')
                
            for s in shots:
                if s.collides_with(a):
                    add_score_boolean = a.split()
                    if add_score_boolean:
                        score += 1
                        print(score)
                    s.kill()
                    log_event("asteroid_shot")
                    
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
    
if __name__ == "__main__":
    main()