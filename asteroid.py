
from constants import *
import pygame
from circleshape import CircleShape
from logger import log_event
import random
import pygame
class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)
            
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            
            return True
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
         
        rotated_vector1 = self.velocity.rotate(angle)
        rotated_vector2 = self.velocity.rotate(-angle)
        self.radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)    

        asteroid1.velocity = rotated_vector1 * 1.2
        asteroid2.velocity = rotated_vector2 * 1.2
    
        return False

        
        