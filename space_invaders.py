import pygame 

class Player:
    player = pygame.image.load("space-ship(1).png")
    x = 500
    y = 900
    x_change = 0


class Enemy:
    ecx = 0.5
    def __init__(self,en,x,y):
        self.enemy = en
        self.ex = x
        self.ey = y
        self.ecx = 0.3


class Bullet:
    bullet = pygame.image.load("bullet.png")
    bx = 500
    by = 900
    bcy = 0.9


class Object:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.enm=[Enemy(pygame.image.load("alien.png"),0,0),
                  Enemy(pygame.image.load("spaceship.png"),100,0),
                  Enemy(pygame.image.load("alien.png"),200,0),
                  Enemy(pygame.image.load("spaceship.png"),300,0),
                  Enemy(pygame.image.load("alien.png"),400,0),
                  Enemy(pygame.image.load("spaceship.png"),500,0),
                  Enemy(pygame.image.load("alien.png"),600,0),
                  Enemy(pygame.image.load("spaceship.png"),700,0),
                  Enemy(pygame.image.load("alien.png"),800,0),
                  Enemy(pygame.image.load("spaceship.png"),900,0)]
        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("space invadors")

        #bullet
        self.flag = 'ready'
        self.q = True
        self.event()
        
    def event(self):
        while self.q:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.q=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Player.x_change = -0.5
                    if event.key == pygame.K_RIGHT:
                        Player.x_change = 0.5
                    if event.key == pygame.K_SPACE:
                        if self.flag == 'ready':
                            Bullet.bx = Player.x
                            self.flag = 'shoot'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        Player.x_change = 0

            Player.x += Player.x_change         
            if Player.x<=0:
                Player.x=0
            elif Player.x>1000-65:
                Player.x = 1000-65

            #bullet shoot
            if Bullet.by<=0:
                Bullet.by=900
                self.flag = 'ready'
            if self.flag=='shoot':
                Bullet.by -= Bullet.bcy
                self.s_bullet()
                
            self.attack()
            self.s_player(Player.x,Player.y)

            # score 
            self.distance(Bullet.bx,Bullet.by)

            pygame.display.update()
    def s_player(self,x,y):
        self.screen.blit(Player.player,(x,y))
    def attack(self):
        for j in range(10):
            self.enm[j].ex += self.enm[j].ecx
            if self.enm[j].ex<=0:
                self.enm[j].ecx = 0.3
                self.enm[j].ey += 100
            elif self.enm[j].ex>1000-65:
                self.enm[j].ey += 100
                self.enm[j].ecx = -0.3
            self.enm[j].ex += self.enm[j].ecx
            self.screen.blit(self.enm[j].enemy,(self.enm[j].ex,self.enm[j].ey))
            if self.enm[j].ey == 900:
                print("Quiting...")
                print("your score is",self.score)
                self.q = False
            
    def s_bullet(self):
        self.screen.blit(Bullet.bullet,(Bullet.bx+24,Bullet.by))

    def distance(self,x,y):
        for i in range(10):
            dx = x-self.enm[i].ex
            dy = y-self.enm[i].ey
            if (dx<=64 and dx>0 and dy<=64 and dy>0):
                Bullet.by=900
                self.flag = 'ready'
                self.score += 1
                print(self.score)
                self.enm[i].ex = 0
                self.enm[i].ey = 0

player1 = Object()

