import pygame, var

class Explosion:
    def __init__(self, x, y, radius):
        self.x = x - radius
        self.y = y - radius
        self.radius = radius
        self.image = pygame.image.load("img/explosion.png")
        self.image = pygame.transform.scale(self.image, (radius*2, radius*2))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y 
        self.frame = 0
        self.frame_rate = 0.1
        self.last_update = pygame.time.get_ticks()
        self.done = False
        
    def update(self, dt):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate * 1000:
            self.last_update = now
            self.frame += 1
            if self.frame == 16:
                self.done = True
            else:
                center = self.rect.center
                self.image = pygame.image.load("img/explosion.png")
                self.image = pygame.transform.scale(self.image, (self.radius*2, self.radius*2))
                self.image.set_colorkey((0, 0, 0))
                self.image.set_alpha(255 - (255 / 16) * self.frame)
                self.rect = self.image.get_rect(center=center)
                self.rect.x = self.x - var.camera_offset.x
                self.rect.y = self.y - var.camera_offset.y
                
    def draw(self, screen):
        screen.blit(self.image, (self.x + var.camera_offset.x,
                                 self.y + var.camera_offset.y))

    def get_center(self):
        return self.rect.center

    def get_rect(self):
        return self.rect
