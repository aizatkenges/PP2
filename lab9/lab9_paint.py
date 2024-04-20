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
            if event.key==pygame.K_y:
                pen="right triangle"
            if event.key==pygame.K_u:
                pen="equilateral triangle"
            if event.key==pygame.K_i:
                pen = "rhombus"
            
            

            
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
                #so x-> x1 is a diameter
                pygame.draw.circle(screen, color, (((x+x1)//2), ((y+y1)//2)), abs((x1-x)/2)) #center  and radius
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
                if (x1-x)<=(y1-y): #top <= bottom
                    y1=y+(x1-x) #bottom  line equals to the top line
                else:
                    x1=x+(y1-y) #in the same way but with top line
    
                pygame.draw.line(screen, color, (x, y), (x1, y),  1) #top
                pygame.draw.line(screen, color, (x, y),(x, y1) , 1) #left
                pygame.draw.line(screen, color, (x, y1), (x1, y1), 1) #bottom
                pygame.draw.line(screen, color, (x1, y),(x1, y1) , 1) #right
                    
                
                last_event = None
                
        if pen == "right triangle":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
            
            if last_event=="not press":
                
                pygame.draw.line(screen, color, (x, y),(x, y1) , 1) #the left line
                pygame.draw.line(screen, color, (x, y1),(x1, y1) , 1) #the bottom line
                pygame.draw.line(screen, color, (x, y),(x1, y1) , 1) #right line
                last_event=None
        if pen == "equilateral triangle":
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                last_event="press"
            if event.type==pygame.MOUSEBUTTONUP:
                x1, y1 = pygame.mouse.get_pos()
                last_event="not press"
            
            if last_event=="not press":
                h=y+((math.sqrt(3)*(x1-x))/2)# бұл биіктігі осы биіктік арқылы оренатция жасаймыз табан қабырғасынын жартысы 
                
                pygame.draw.line(screen, color, (x+(x1-x)/2, y), (x, h), 1)
                pygame.draw.line(screen, color, (x+(x1-x)/2, y), (x1, h), 1)
                pygame.draw.line(screen, color, (x1, h), (x, h), 1)
                #pygame.draw.line(screen, color, (x+(x1-x)/2, y), (x+(x1-x)/2, h), 1) #биіктігі
                last_event = None  
        #rhombus
        if pen == "rhombus":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y =pygame.mouse.get_pos()
                last_event = "press"
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 =pygame.mouse.get_pos()
                last_event = "not press"
            if last_event == "not press":
                pygame.draw.line(screen, color, (x, y+(y1-y)/2),(x+(x1-x)/2, y), 1)# төбелерінің коорлинттарын табу үшін 
                pygame.draw.line(screen, color, (x, y+(y1-y)/2),(x+(x1-x)/2, y1), 1)
                pygame.draw.line(screen, color, (x+(x1-x)/2, y1),(x1, y+(y1-y)/2), 1)
                pygame.draw.line(screen, color, (x+(x1-x)/2, y),(x1, y+(y1-y)/2), 1)
                last_event = None



        
    clock.tick(FPS)       
    pygame.display.flip()