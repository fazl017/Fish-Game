from pygame import *
from random import *

init()

genislik, yukseklik= 600,600

win = display.set_mode((genislik,yukseklik))

fps = 60

clock = time.Clock()


class Game():
    def __init__(self):
        pass

    def update(self):
        pass

    def cizdir(self):
        pass

    def temas(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def guvenli_alan(self):
        pass

    def hedef_yenile(self):
        pass

    def hedefle(self):
        pass


class Fish(sprite.Sprite):
    def __init__(self,x,y,image,type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)
        self.type = type
        self.speed = randint(1,7)
        self.direction_X =choice([-1,1])
        self.direction_Y = choice([-1,1])

    def update(self,):
        self.rect.x += self.speed*self.direction_X
        self.rect.y += self.speed*self.direction_Y
        if self.rect.left<=0 or self.rect.right>=genislik:
            self.direction_X*=-1
        if self.rect.top<=0 or self.rect.bottom>=yukseklik:
            self.direction_Y*=-1



class Balikci (sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load("fisherman.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.life = 3
        self.speed = 10
    def update(self, ):
        pass

    def update(self,):
        self.hareket()

    def hareket(self):
        tus = key.get_pressed()

        if tus[K_LEFT]:
            self.rect.x -= self.speed

        elif tus[K_RIGHT]:
            self.rect.x += self.speed

        elif tus[K_UP]:
            self.rect.y -= self.speed

        elif tus[K_DOWN]:
            self.rect.y += self.speed

fisherman_group = sprite.Group()
fisherman =Balikci(genislik // 2, yukseklik // 2)
fisherman_group.add(fisherman)



fish2 = image.load("fish.png")
fish_group =sprite.Group()
fish = Fish(randint(0,genislik-32),randint(0,yukseklik-32),fish2,0)
fish_group.add(fish)

fish1 = image.load("clown-fish.png")
fish_group =sprite.Group()
fish = Fish(randint(0,genislik-32),randint(0,yukseklik-32),fish1,0)
fish_group.add(fish)

durum = True
while durum:
    for i in event.get():
       if i.type == QUIT:
           durum = False

    fisherman_group.update()
    fisherman_group.draw(win)
    fish_group.update()
    fish_group.draw(win)
    display.update()
    win.fill((0,0,0))
    clock.tick(fps)
quit()