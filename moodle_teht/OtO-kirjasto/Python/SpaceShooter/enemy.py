import pygame, var, math, random
from functions import correct_scale

class Enemy:
    def __init__(self, x, y, speed, image, health, coins, damage):
        random_side = random.randint(80, 120)*1.5
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.max_health = health
        self.coins = coins
        self.damage = damage
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (correct_scale(random_side, random_side)))
        self.rect = self.image.get_rect()
        self.rotated_image = self.image
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self, dt, enemies):
        # Move towards player
        player_x = var.player_pos.x
        player_y = var.player_pos.y
        angle = math.atan2(player_y - self.y, player_x - self.x)
        self.x += math.cos(angle) * self.speed * dt
        self.y += math.sin(angle) * self.speed * dt

        # Calculate net force to repel other enemies
        net_force = pygame.math.Vector2()
        repulsion_distance = (self.image.get_width() / 2) * (2 ** 0.5)

        for enemy in enemies:
            if enemy != self:  # Skip checking against itself
                offset = pygame.math.Vector2(self.x - enemy.x, self.y - enemy.y)
                distance = offset.length()

                if distance <= repulsion_distance:
                    force_strength = (repulsion_distance -
                                    distance) / repulsion_distance
                    net_force += offset.normalize() * force_strength

        # Update position based on net force
        self.x += net_force.x * self.speed * dt
        self.y += net_force.y * self.speed * dt

        # Rotate the image based on the movement direction
        self.rotated_image = pygame.transform.rotate(
            self.image, -math.degrees(angle))
        self.rect = self.rotated_image.get_rect(
            center=(self.x + var.camera_offset.x, self.y + var.camera_offset.y))

        # Update rect coordinates
        self.rect.x = self.x + var.camera_offset.x
        self.rect.y = self.y + var.camera_offset.y



    def draw(self, screen):
        screen.blit(self.rotated_image, (self.x +
                    var.camera_offset.x, self.y + var.camera_offset.y))

    def get_rect(self):
        return self.rect

    def get_health(self):
        return self.health
    
    def get_max_health(self):
        return self.max_health
    
    def set_max_health(self, max_health):
        self.max_health = max_health
        
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

    def set_health(self, health):
        self.health = health

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image
    
    def hitted(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.coins += var.coins
            return True
        else:
            return False

    def get_damage(self):
        return self.damage
    
    def set_damage(self, damage):
        self.damage = damage
