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
    pass


class Balikci (sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load("fisherman (1).png")
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
fisherman_group.add()


durum = True
while durum:
    for i in event.get():
       if i.type == QUIT:
           durum = False

    display.update()
    clock.tick()
quit()