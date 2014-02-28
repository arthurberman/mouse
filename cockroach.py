import pygame, characters

class Cockroach(pygame.sprite.Sprite):
        def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                
                try:
                        self.image = pygame.image.load('cockroach.png').convert()
                except:
                        self.image = pygame.Surface((100, 63))
                self.rect = self.image.get_rect().move(x, y)
                self.moveVector = [0, 0]
                self.inAir = True
                self.grounded = False

                #create huge rect to see if player is on same level
                self.rectPlayerCheck = pygame.Rect(x - 100, y + self.image.get_size()[1], 200, 1) 

                #boolean to check it player is on same platform
                self.playerPlatform = False
                #self.currentXPlatform = None #does not start on a platform
                self.currentYPlatform = None

        def update(self, hero, platforms):
                #need to find a way to know if hero is on platform
                #this moves towards hero
                self.collide(platforms, hero) #make sure hero is passed here
                if (self.grounded == True and self.playerPlatform == True):
                    if (self.rect.x < hero.rect.x):
                        self.rect.x += 2
                    if (self.rect.x > hero.rect.x):
                        self.rect.x -= 2
                elif (self.grounded == True: #and self.currentYPlatform != None):
                    if (self.rect.x < self.currentYPlatform.x):
                        self.rect.x += 2
                    if (self.rect.x > self.currentYPlatform.x + self.currentYPlatform.width):
                        self.rect.x -= 2
                        
                        
                #this moves cockroach downward 
                if (self.inAir == True):
                        self.rect.y += 4 # 
                        
                
        def draw(self, screen, world):
                screen.blit(self.image, self.rect.move(world))

        def entityCollide(self, who):
                pass
                
        def collide(self, platforms, hero):
                self.platformCollide(platforms)
                self.HeroOnPlatform(hero)

                #check for player collision
                #do nothing with dynamics for now

        def HeroOnPlatform(self, hero):
                #if the player collides with this
                if (self.rectPlayerCheck.colliderect(hero.rect)):
                        self.playerPlatform = True
                else:
                        self.playerPlatform = False
                
                        
        def platformCollide(self, platforms):
                #self.grounded = False
                for platform in platforms:
                        rectx = self.rect.move((0, self.moveVector[1]))
                        col = platform.collides(rectx)
                        if col is not None:
                            self.currentYPlatform = rectx                   
                            if (self.rect.y > platform.rect.y):
                                self.rect.y = rectx.y + col.height
                                self.moveVector[1] = 0
                            if (self.rect.y < platform.rect.y):
                                self.inAir = False
                                self.grounded = True
                                self.rect.y = rectx.y - col.height
                                self.moveVector[1] = 0
                        rect = self.rect.move((self.moveVector[0], 0))
                        col = platform.collides(rect)
                        if col is not None:
                                if (self.rect.x < platform.rect.x):
                                        self.rect.x = rect.x - col.width
                                if (self.rect.x > platform.rect.x):
                                        self.rect.x = rect.x + col.width
                                self.moveVector[0] = 0
                if not self.grounded:
                        self.inAir = True



