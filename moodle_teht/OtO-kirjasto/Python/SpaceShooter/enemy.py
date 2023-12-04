import pygame

class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("img/enemy.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, dt):
        self.x -= self.speed * dt
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen, camera_offset):
        screen.blit(self.image, (self.x + camera_offset.x, self.y + camera_offset.y))

    def get_rect(self):
        return self.rect

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_speed(self):
        return self.speed

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_speed(self, speed):
        self.speed = speed

    def set_rect(self, rect):
        self.rect = rect

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image