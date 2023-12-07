import pygame, bullet, math, functions, var

class Player:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, dt):
        self.x -= self.speed * dt
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen, rect, image):
        var.player_pos.x = self.x - var.camera_offset.x - 50
        var.player_pos.y = self.y - var.camera_offset.y - 60
        screen.blit(image, rect)

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
    def shoot(self, angle):
        return bullet.Bullet(self.x - 20 - var.camera_offset.x, self.y - 30 - var.camera_offset.y, 1000, angle, functions.rando_bullet(),)
