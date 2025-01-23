from pygame import *
from random import *
import pygame

init()

genislik, yukseklik= 600, 600

win = display.set_mode((genislik,yukseklik))

fps = 60

clock = time.Clock()


class Game():
    def __init__(self,fisherman,fish_geoup):
        self.fisherman = fisherman
        self.fish = fish_group
        self.time = 0
        self.fps_deger_sayaci = 0
        self.level = 0
        fish1 = image.load("fish.png")
        fish2 = image.load("fish (1).png")
        fish3 = image.load("goldfish.png")
        fish4 = image.load("clown-fish.png")
        self.fish_list = [fish1,fish2,fish3,fish4]
        self.fish_list_index_no = randint(0,3)
        self.goal_fish_image =  self.fish_list[self.fish_list_index_no]
        self.goal_fish_location = self.goal_fish_image.get_rect()
        self.goal_fish_location.top = 40
        self.goal_fish_location.centerx = genislik/2
        self.game_font = font.Font("Roboto-VariableFont_wdth,wght.ttf",40)
        self.fishing = mixer.Sound("levelUp.wav")
        self.The_sound_of_dying = mixer.Sound("game-over-arcade-6435.mp3")
        mixer.music.load("Background sound effect.mp3")
        mixer.music.play(-1)
        self.game_backgrauond = image.load("Underwater Cave.jpeg")
        self.game_over = image.load("game_over.jpg")





    def update(self):
        self.fps_deger_sayaci +=1
        if self.fps_deger_sayaci == fps:
            self.time += 1
            print(self.time)
            self.fps_deger_sayaci = 0
        self.temas()

    def cizdir(self):
        text = self.game_font.render("Time : " + str(self.time),True, (255,255,255))
        text_locastion = text.get_rect()
        text_locastion.top=30
        text_locastion.left=30

        text2 = self.game_font.render("Life: "+ str(self.fisherman.life),True, (255,255,255))
        text2_locastion = text2.get_rect()
        text2_locastion.top= 30
        text2_locastion.left = genislik-150
        win.blit(self.game_backgrauond,(0,0))
        win.blit(text,text_locastion)
        win.blit(text2,text2_locastion)


        win.blit(self.goal_fish_image,self.goal_fish_location)
        draw.rect(win,(255,0,0),(275,30,50,40),5)
        draw.rect(win,(255,255,255),(0,100,600,yukseklik-100),1)



    def temas(self):
        contacted = pygame.sprite.spritecollideany(self.fisherman,self.fish)
        if contacted:
            if contacted.type == self.fish_list_index_no:
                contacted.remove(self.fish)
                self.fishing.play()
                if self.fish:
                     self.hedef_yenile()
                else:
                    self.hedefle()
            else:
                 self.fisherman.life -= 1
                 self.The_sound_of_dying.play()
                 self.guvenli_alan()
                 if  self.fisherman.life():
                     self.stop()




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
fish2 = Fish(randint(0,genislik-32),randint(0,yukseklik-32),fish2,0)
fish_group.add(fish2)

fish1 = image.load("clown-fish.png")
fish_group =sprite.Group()
fish = Fish(randint(0,genislik-32),randint(0,yukseklik-32),fish1,0)
fish_group.add((fish,fish2))
game = Game(fisherman,fish)

durum = True
while durum:
    for i in event.get():
       if i.type == QUIT:
           durum = False

    game.update()
    game.cizdir()
    fish_group.update()
    fisherman_group.update()
    fisherman_group.draw(win)
    fish_group.draw(win)
    display.update()
    win.fill((0,0,0))
    game.update()
    clock.tick(fps)
quit()