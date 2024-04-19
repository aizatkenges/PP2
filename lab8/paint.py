import pygame, sys, math
pygame.init()

#түстер
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

#default color of pen 
color = RED

#clock 
clock = pygame.time.Clock()
FPS = 60

#screen 
wd, wh = 1001, 601
screen = pygame.display.set_mode((wd, wh))
screen.fill(WHITE)

#pen
pen="mouse" 
last_event = None

pre, cur = None, None
pre_e, cur_e = None, None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #pen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pen="mouse"
            if event.key == pygame.K_w:
                pen="rectangle"
            if event.key == pygame.K_e:
                pen="circle"
            if event.key == pygame.K_r:
                pen="Eraser"
            if event.key==pygame.K_t:
                pen="square"
            
            

            
            if event.key == pygame.K_a:
                color=RED
            if event.key == pygame.K_s:
                color=GREEN
            if event.key == pygame.K_b:
                color=BLUE
            if event.key == pygame.K_f:
                color=BLACK
        
        #draw by mouse
        if pen == "mouse":
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pre = pygame.mouse.get_pos() 
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
            if pre:
                pygame.draw.line(screen, color, pre, cur, 1)
                pre = cur
            if event.type==pygame.MOUSEBUTTONUP:
                pre=None
        
        #draw rectangle
        if pen == "rectangle":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
            if last_event=="not press":
                #pygame.draw.rect(screen, color, (int(x), int(y), int(x1)-int(x), int(y1)-int(y) ))#бұл іші боялған тік төрт бұрыш салды
                pygame.draw.line(screen, color, (x, y), (x1, y), 1) #top side
                pygame.draw.line(screen, color, (x,y), (x, y1), 1) #left side
                pygame.draw.line(screen, color, (x, y1), (x1, y1), 1) #bottom side
                pygame.draw.line(screen, color, (x1, y), (x1, y1), 1) #right side
                last_event=None
        #draw circle
        if pen == "circle":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
            if last_event=="not press":
                pygame.draw.circle(screen, color, (((x+x1)//2), ((y+y1)//2)), abs((x1-x)/2))
                pygame.draw.circle(screen, WHITE, (((x+x1)//2), ((y+y1)//2)), abs((x1-x)/2)-0.5)
                last_event=None
        #Eraser
        if pen == "Eraser":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pre_e = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur_e = pygame.mouse.get_pos()
            if pre_e:
                pygame.draw.line(screen, WHITE, pre_e, cur_e, 10)
                pre_e=cur_e
            if event.type == pygame.MOUSEBUTTONUP:
                prev1 = None

        #square
        #x, y, x1, y1 = 0,0,0,0
        if pen=="square":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
               
            if last_event=="not press":
                if (x1-x)<=(y1-y):
                    y1=y+(x1-x)
                else:
                    x1=x+(y1-y)
    
                pygame.draw.line(screen, color, (x, y), (x1, y),  1)
                pygame.draw.line(screen, color, (x, y),(x, y1) , 1)
                pygame.draw.line(screen, color, (x, y1), (x1, y1), 1)
                pygame.draw.line(screen, color, (x1, y),(x1, y1) , 1)
                    
                
                last_event = None

        
    clock.tick(FPS)       
    pygame.display.flip()