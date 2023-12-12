import pygame, math, var, random
# from functions import rando_bullet
from functions import correct_scale

class Bullet:
    def __init__(self, x, y, speed, angle, image, damage):
        random_size = random.randint(50, 80)
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.damage = damage
        self.upgrade = None
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(
        self.image, (correct_scale(random_size, random_size)))
        self.image = pygame.transform.rotate(self.image, -self.angle + 90)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, dt):
        self.x += self.speed * dt * math.cos(math.radians(self.angle))
        self.y += self.speed * dt * math.sin(math.radians(self.angle))
        self.rect.x = self.x + var.camera_offset.x
        self.rect.y = self.y + var.camera_offset.y

    def draw(self, screen):
        screen.blit(self.image, (self.x + var.camera_offset.x,
                    self.y + var.camera_offset.y))

    def get_center(self):
        return self.rect.center
    
    def get_rect(self):
        return self.rect
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_speed(self):
        return self.speed

    def get_angle(self):
        return self.angle

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_speed(self, speed):
        self.speed = speed

    def set_angle(self, angle):
        self.angle = angle

    def set_rect(self, rect):
        self.rect = rect

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image
    
    def get_damage(self):
        return self.damage
    
    def set_damage(self, damage):
        self.damage = damage
        
    def set_upgrade(self, gun, upgrade):
        if gun == "raka_ase":
            if upgrade == "MK1":
                self.damage = var.raka_ase["MK1"]["Damage"]
                var.firerate_max = var.raka_ase["MK1"]["Fire Rate"]
                var.reload_time_max = var.raka_ase["MK1"]["Reload Time"]
                var.ammo_max = var.raka_ase["MK1"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK2":
                self.damage = var.raka_ase["MK2"]["Damage"]
                var.firerate_max = var.raka_ase["MK2"]["Fire Rate"]
                var.reload_time_max = var.raka_ase["MK2"]["Reload Time"]
                var.ammo_max = var.raka_ase["MK2"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK3":
                self.damage = var.raka_ase["MK3"]["Damage"]
                var.firerate_max = var.raka_ase["MK3"]["Fire Rate"]
                var.reload_time_max = var.raka_ase["MK3"]["Reload Time"]
                var.ammo_max = var.raka_ase["MK3"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK4":
                self.damage = var.raka_ase["MK4"]["Damage"]
                var.firerate_max = var.raka_ase["MK4"]["Fire Rate"]
                var.reload_time_max = var.raka_ase["MK4"]["Reload Time"]
                var.ammo_max = var.raka_ase["MK4"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK5":
                self.damage = var.raka_ase["MK5"]["Damage"]
                var.firerate_max = var.raka_ase["MK5"]["Fire Rate"]
                var.reload_time_max = var.raka_ase["MK5"]["Reload Time"]
                var.ammo_max = var.raka_ase["MK5"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
        elif gun == "kakku_sinko":
            if upgrade == "MK1":
                self.damage = var.kakku_sinko["MK1"]["Damage"]
                var.firerate_max = var.kakku_sinko["MK1"]["Fire Rate"]
                var.reload_time_max = var.kakku_sinko["MK1"]["Reload Time"]
                var.ammo_max = var.kakku_sinko["MK1"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK2":
                self.damage = var.kakku_sinko["MK2"]["Damage"]
                var.firerate_max = var.kakku_sinko["MK2"]["Fire Rate"]
                var.reload_time_max = var.kakku_sinko["MK2"]["Reload Time"]
                var.ammo_max = var.kakku_sinko["MK2"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK3":
                self.damage = var.kakku_sinko["MK3"]["Damage"]
                var.firerate_max = var.kakku_sinko["MK3"]["Fire Rate"]
                var.reload_time_max = var.kakku_sinko["MK3"]["Reload Time"]
                var.ammo_max = var.kakku_sinko["MK3"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK4":
                self.damage = var.kakku_sinko["MK4"]["Damage"]
                var.firerate_max = var.kakku_sinko["MK4"]["Fire Rate"]
                var.reload_time_max = var.kakku_sinko["MK4"]["Reload Time"]
                var.ammo_max = var.kakku_sinko["MK4"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            elif upgrade == "MK5":
                self.damage = var.kakku_sinko["MK5"]["Damage"]
                var.firerate_max = var.kakku_sinko["MK5"]["Fire Rate"]
                var.reload_time_max = var.kakku_sinko["MK5"]["Reload Time"]
                var.ammo_max = var.kakku_sinko["MK5"]["Magazine Size"]
                var.ammo = var.ammo_max
                self.upgrade = upgrade
            
    def get_upgrade(self):
        return self.upgrade