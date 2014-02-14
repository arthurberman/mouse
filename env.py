import pygame

class Hero(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('mouse.png').convert()
                self.image = pygame.transform.scale(self.image, (50, 50))
                self.rect = pygame.rect.Rect(100, 100, 50, 50)
                self.moveVector = [0, 0]
                self.inAir = True
                self.canJump = True
                self.speed = 3
        def move(self, keys):
                if (keys[pygame.K_d]):
                        if not self.inAir:
                                self.moveVector[0] += 1
                        else:
                                self.moveVector[0] += 0.125
                elif (keys[pygame.K_a]):
                        if not self.inAir:
                                self.moveVector[0] -= 1
                        else:
                                self.moveVector[0] -= 0.125
                        
                else:
                        if not self.inAir:
                                if (self.moveVector[0] < -0.5):
                                        self.moveVector[0] += 1
                                elif self.moveVector[0] > 0.5:
                                        self.moveVector[0] -= 1
                                else:
                                        self.moveVector[0] = 0
                if (keys[pygame.K_j] and not self.inAir):
                        if (self.canJump):
                                self.moveVector[1] = -18
                        self.canJump = False
                if not keys[pygame.K_j] and not self.inAir:
                        self.canJump = True
                self.moveVector[1] += 1
                if (self.moveVector[0] > self.speed):
                        self.moveVector[0] = self.speed
                if (self.moveVector[0] < -self.speed):
                        self.moveVector[0] = -self.speed

        def update(self):
                self.rect.x += self.moveVector[0]
                self.rect.y += self.moveVector[1]
        def draw(self, screen):
                screen.blit(self.image, self.rect)

        def collide(self, platforms):
                grounded = False
                for platform in platforms:
                        rect = self.rect.move((0, self.moveVector[1]))
                        col = platform.collides(rect) 
                        if col is not None:
                                if (self.rect.y > platform.rect.y):
                                        self.rect.y = rect.y + col.height
                                        self.moveVector[1] = 0

                                if (self.rect.y < platform.rect.y):
                                        self.inAir = False
                                        grounded = True
                                        self.rect.y = rect.y - col.height
                                        self.moveVector[1] = 0
                        rect = self.rect.move((self.moveVector[0], 0))
                        col = platform.collides(rect)
                        if col is not None:
                                if (self.rect.x < platform.rect.x):
                                        self.rect.x = rect.x - col.width
                                if (self.rect.x > platform.rect.x):
                                        self.rect.x = rect.x + col.width
                                self.moveVector[0] = 0
                if not grounded:
                        self.inAir = True
class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, w, h):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.surface.Surface((w, h))
                self.image.fill(16777215)
                self.rect = pygame.rect.Rect(x, y, w, h)
        def update(self):
                pass
        def collides(self, rect):
                if (rect.colliderect(self.rect)):
                        return rect.clip(self.rect)
                return None
        def draw(self, screen):
                screen.blit(self.image, self.rect)
