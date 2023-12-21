import pygame, math, functions, var
from bullet import Bullet

class Player:
    def __init__(self, x, y, speed, image, health, gun, upgrade):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.max_health = health
        self.gun = gun
        self.raka_ase_ammo = 0
        self.kakku_sinko_ammo = 0
        self.upgrade = upgrade
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (functions.correct_scale(300, 300)))
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
    
    def get_center(self):
        return self.rect.center
    
    def get_center_x(self):
        return self.rect.centerx

    def get_center_y(self):
        return self.rect.centery
    
    def get_radius(self):
        return self.rect.radius
    
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
    
    def shoot(self, angle): # dont know why but the bullet spawns at the wrong place
        bullet_x = self.get_center_x() - var.camera_offset.x - 30
        bullet_y = self.get_center_y() - var.camera_offset.y - 30
        if self.gun == "raka_ase":
            gun_type = "raka_ase"
            rand_x, rand_y = 50, 80
        elif self.gun == "kakku_sinko":
            gun_type = "kakku_sinko"
            rand_x, rand_y = 80, 120
                        
        return Bullet(bullet_x, bullet_y, 1000, angle, functions.rando_bullet(gun_type), var.gun_damage, rand_x, rand_y, gun_type)
    
    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health
        
    def get_max_health(self):
        return self.max_health
    
    def set_max_health(self, max_health):
        self.max_health = max_health

    def hitted(self, damage):
        var.invincibility_time = var.invincibility_time_max
        print("Player got hit for " + str(damage) + " damage! Player health: " + str(self.health))
        self.health -= damage
        print("Player health: " + str(self.health))
        if self.health <= 0:
            return True
    
    def is_dead(self):
        if self.health <= 0:
            return True
        return False
    
    def set_upgrade(self, gun, upgrade):
        if gun == "raka_ase":
            if upgrade == "MK1" or upgrade == "MK2" or upgrade == "MK3" or upgrade == "MK4" or upgrade == "MK5":
                self.damage = var.raka_ase[upgrade]["Damage"]
                var.firerate_max = var.raka_ase[upgrade]["Fire Rate"]
                var.reload_time_max = var.raka_ase[upgrade]["Reload Time"]
                var.reload_time = var.reload_time_max
                var.gun_damage = var.raka_ase[upgrade]["Damage"]
                self.upgrade = upgrade
                self.gun = gun
                var.ammo = self.get_raka_ase_ammo()
                var.ammo_max = var.raka_ase[upgrade]["Magazine Size"]
                
        elif gun == "kakku_sinko":
            if upgrade == "MK1" or upgrade == "MK2" or upgrade == "MK3" or upgrade == "MK4" or upgrade == "MK5":
                self.damage = var.kakku_sinko[upgrade]["Damage"]
                var.firerate_max = var.kakku_sinko[upgrade]["Fire Rate"]
                var.reload_time_max = var.kakku_sinko[upgrade]["Reload Time"]
                var.reload_time = var.reload_time_max
                var.gun_damage = var.kakku_sinko[upgrade]["Damage"]
                self.upgrade = upgrade
                self.gun = gun
                var.ammo = self.get_kakku_sinko_ammo()
                var.ammo_max = var.kakku_sinko[upgrade]["Magazine Size"]
                
    def get_upgrade(self):
        return self.upgrade
    
    def get_raka_ase_ammo(self):
        return self.raka_ase_ammo
    
    def set_raka_ase_ammo(self, raka_ase_ammo):
        self.raka_ase_ammo = raka_ase_ammo
        
    def get_kakku_sinko_ammo(self):
        return self.kakku_sinko_ammo
    
    def set_kakku_sinko_ammo(self, kakku_sinko_ammo):
        self.kakku_sinko_ammo = kakku_sinko_ammo
        
    def get_gun(self):
        return self.gun
