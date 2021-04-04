from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 625:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <=470:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x +=self .speed

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode(
    (win_width,win_height)
)
display.set_caption("Maze")
background = transform.scale(
    image.load("background.jpg"),
    (win_width,win_height)
)
wall1 = Wall(0,0,0,180,0,20,420)
wall2 = Wall(0,0,0,270,75,20,420)
wall4 = Wall(0,0,0,360,0,20,420)
wall3 = Wall(0,0,0,450,75,20,420)
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
game = True
hero = Hero("hero.png",100,100,5)
treasure = GameSprite("treasure.png",500,300,10)
cyborg = Enemy("cyborg.png",420,150,2)
font.init()
font = font.Font(None,70)

win = font.render(
    "U WIN!",True,(255,215,0)
)
lose = font.render(
    "haha!",True,(255,25,0)
)
clock = time.Clock()
FPS = 60
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background,(0,0))
        hero.update()
        hero.reset()
        wall1.update()
        wall1.draw_wall()
        wall2.update()
        wall2.draw_wall()
        wall3.update()
        wall3.draw_wall()
        wall4.update()
        wall4.draw_wall()
        if sprite.collide_rect(hero,wall1) or sprite.collide_rect(hero,wall2) or sprite.collide_rect(hero,wall3) or sprite.collide_rect(hero,wall4) or sprite.collide_rect(hero,cyborg):
            finish = True
            window.blit(lose, (200, 200))
        if sprite.collide_rect(hero,treasure):
            finish = True
            window.blit(win, (200, 200))
        treasure.reset()
        cyborg.reset()
        cyborg.update()
        clock.tick(FPS)
        display.update()