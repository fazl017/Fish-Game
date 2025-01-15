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
    def __init__(self):
        pass

    def update(self, ):
        pass



class Balikci (sprite.Sprite):
    def __init__(self):
        pass

    def update(self,):
        pass

    def hareket(self):
        pass




durum = True
while durum:
    for i in event.get():
       if i.type == QUIT:
           durum = False

    display.update()
    clock.tick()
quit()