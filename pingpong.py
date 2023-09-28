from pygame import*
window = display.set_mode((600,500))
display.set_caption('Пинг-понг')

window.fill((200,255,255))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_w,player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed 
    def update2 (self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed 

font.init()
player1=Player('Безымянный.png',30,200,4,50,150)
player2=Player('Безымянный.png',520,200,4,50,150)
ball = GameSprite('tennisball.png',200,200,4,50,50)
font1 = font.SysFont(None,35)
font2 = font.SysFont(None,35)
lose1 = font1.render(
    'Player 1 lose',True,(255,215,0)
)
lose2 = font2.render(
    'Player 2 lose',True,(255,215,0)
)

game = True
finish = False
clock = time.Clock()
speed_x = 4
speed_y = 4
while game:
   
    for e in event.get():
        if e.type==QUIT:
            game = False
    if finish != True: 
        window.fill((200,255,255))
        player1.update1()
        player2.update2()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if ball.rect.y > 450 or ball.rect.y<0:
            speed_y *= -1
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > 550:
            finish = True
            window.blit(lose2,(200,200))
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(60)
