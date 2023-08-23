import pygame,time,random
pygame.init()
s=pygame.display.set_mode((400,400))
pygame.display.set_caption("Snake Game")
a,b=10,10
x,y=200,200
food_x,food_y=0,0
snake=[[x,y],[x-a,y],[x-2*a,y]]
font=pygame.font.SysFont(None,30)
def disp_text(msg,color):
    txt=font.render(msg,True,color)
    s.blit(txt,[s.get_width()/6,s.get_height()/3])
game_over=False

clock=pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                a,b=0,-10
            elif event.key==pygame.K_DOWN:
                a,b=0,10
            elif event.key==pygame.K_LEFT:
                a,b=-10,0
            elif event.key==pygame.K_RIGHT:
                a,b=10,0
    x+=a
    y+=b
    if x<0 or x>=s.get_width() or y<0 or y>=s.get_height():
        game_over=True
    s.fill((0,0,0))
    pygame.draw.rect(s,(0,255,0),[x,y,10,10])
    for i in snake:
        pygame.draw.rect(s,(255,255,255),[i[0],i[1],10,10])
    if x==food_x and y==food_y:
        food_x=round(random.randrange(0,s.get_width()-10)/10.0)*10.0
        food_y=round(random.randrange(0,s.get_height()-10)/10.0)*10.0
        snake.insert(0,[x,y])
    else:
        snake.insert(0,[x,y])
        snake.pop()
    pygame.draw.rect(s,(255,0,0),[food_x,food_y,10,10])
    pygame.display.update()
    clock.tick(15)
disp_text("Game Over, Press any key to quit",(255,255,255))
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()