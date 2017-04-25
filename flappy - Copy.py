import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
yellow = (230,230,0)
brightyellow =(255,255,0)
red = (255,0,0)
darkgrey = (200,200,200)
grey = (230,230,230)
green = (0,170,0)
blue =(0,0,200)
lightblue = (0,0,100)

display_width = 700
display_height = 500
birdsize = 40
z = birdsize/2

background= pygame.image.load('wallpaper.jpg')
background = pygame.transform.scale(background,(display_width,display_height))
bird1 = pygame.image.load('bird1.png')
bird1 = pygame.transform.scale(bird1,(birdsize,birdsize))
bird2 = pygame.image.load('bird2.png')
bird2 = pygame.transform.scale(bird2,(birdsize,birdsize))
bird3 = pygame.image.load('bird3.png')
bird3 = pygame.transform.scale(bird3,(birdsize,birdsize))

gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flappy Birds')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,40)

b_height = 180
b_width = 100

def blitimage(img,x,y):
    myrect = img.get_rect()
    myrect.centerx = x
    myrect.centery = y

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    gamedisplay.blit(img,myrect)
    if myrect.left <= cur[0] <= myrect.right and myrect.top <= cur[1] <= myrect.bottom:
        if click[0] == 1 :
            return img

    return None

def button(msg,size,rectcol,inact,color,x,y,sizex,sizey,action = None):
    font = pygame.font.SysFont(None,size)

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < cur[0] < x+sizex and y < cur[1] < y+sizey:
        myrect = pygame.draw.rect(gamedisplay,inact,[x,y,sizex,sizey])
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "start":
                gameloop()
            
    else:
        myrect = pygame.draw.rect(gamedisplay,rectcol,[x,y,sizex,sizey])
    msg = font.render(msg,True,color)
    msgrect = msg.get_rect()
    msgrect.centerx = myrect.centerx
    msgrect.centery = myrect.centery
    gamedisplay.blit(msg,msgrect)

def pause():
    p = True
        
    while p:
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
            
        gamedisplay.blit(background,[0,0])

        gamedisplay.blit(font.render("Game Paused..!!",True,grey),[250,160])
        button("Resume",25,darkgrey,grey,black,250,200,100,25,"pause")
        if 250 < cur[0] < 350 and 200 < cur[1] < 225:
            if click[0] ==1:
                p=False
        button("Restart",25,darkgrey,grey,black,460,200,100,25,"start")
        button("Quit",25,darkgrey,grey,black,355,200,100,25,"quit")   

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    p = False

def selectbird():
    intro = True

    while intro:
        gamedisplay.blit(background,(0,0))
        blitimage(font.render("Select Bird",True,black),display_width/2,200)

        img1 = blitimage(bird1,display_width/2-150,display_height/2)
        img2 = blitimage(bird2,display_width/2,display_height/2)
        img3 = blitimage(bird3,display_width/2+150,display_height/2)

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if img1 != None:
            birdimg = img1
            intro = False
        elif img2 != None:
            birdimg = img2
            intro = False
        elif img3 != None:
            birdimg = img3
            intro = False

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    return birdimg
        

def randomb(blockers):
    p = True
    for xny in blockers:
        if xny[0] > display_width -350:
            p = False
            break

    if p == True:
        block = []
        block.append(display_width)
        block.append(0)
        
        height1 = random.randint(10,350)
        y2 = random.randint(height1 + 140,height1 + 250)

        while y2 > display_height-10:
            y2 = random.randint(height1 + 120,height1 + 250)
        
        block.append(height1)
        block.append(y2)
        block.append(display_height - y2)
        blockers.append(block)
    
def check(x,y,xny):
    if (xny[0] <= x <= xny[0] + b_width and xny[1] <= y <= xny[1] + xny[2]) or (xny[0] <= x <= xny[0] + b_width and xny[3] <= y <= xny[3] + xny[4]):
        return True
    else:
        return False

def gameloop():
    x = display_width/2
    y = display_height/2
    blockers = []
    gameexit = False
    gameover = False
    birdimg  = selectbird()

    
        
    while not gameexit:
            while gameover:
                gamedisplay.blit(background,[0,0])
            
                gamedisplay.blit(font.render("Game Over..!!",True,grey),[250,175])
                button("Restart",25,darkgrey,grey,black,250,200,100,25,"start")
                button("Quit",25,darkgrey,grey,black,355,200,100,25,"quit")   
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameover = False
                        gameexit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameloop()
                        elif event.key == pygame.K_c:
                            gameloop()
                            
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = True   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        y -= 70
                    if event.key == pygame.K_p:
                        pause()

            gamedisplay.blit(background,(0,0))
            bird = birdimg.get_rect()
            bird.centerx = x
            bird.centery = y
            gamedisplay.blit(birdimg,bird)

            randomb(blockers)

            for xny in blockers:
                pygame.draw.rect(gamedisplay,green,[xny[0],xny[1],b_width,xny[2]])
                pygame.draw.rect(gamedisplay,green,[xny[0],xny[3],b_width,xny[4]])

                xny[0] -= 5

                if check(x-z,y-z,xny) or check(x+z,y-z,xny) or check(x+z,y+z,xny) or check(x-z,y+z,xny) or y > display_height or y < 0:
                    gameover = True
                    
                if xny[0]  <= -100:
                    del blockers[0]
                
            y += 7 
            clock.tick(25)
            pygame.display.update()

    pygame.quit()
    quit()
    
gameloop()
