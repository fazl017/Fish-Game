from pygame import *
from random import *

init()

genislik, yukseklik= 600,600

win = display.set_mode((genislik,yukseklik))

fps = 60

clock = time.Clock()

durum = True
while durum:
    for i in event.get():
       if i.type == QUIT:
           durum = False

    display.update()
    clock.tick()
quit()