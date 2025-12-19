import pygame
import random

pygame.init()

rows = {1:400,2:420,3:440,4:460,5:480,6:500,7:520,8:540,9:560,10:580}
collumns = {1:100,2:120,3:140,4:160,5:180,6:200,7:220,8:240,9:260,10:280,11:300,12:320,13:340,14:360,15:380,16:400,17:420,18:440,19:460,20:480}

score = 0
lineCount = 0
threshold = 1000

hit = dict((i, dict((j, False) for j in range(1,21))) for i in range(1, 11))

rS = dict((i, dict((j, -1) for j in range(1,21))) for i in range(1, 11))

types = {'T':0,'4x4':0,'zLeft':0,'zRight':0,'lLeft':0,'lRight':0,'straight':0}

sprite_list = ['dark_block.png', 'light_block.png', 'hole_block.png']


level = 0





class block:
    
    def __init__(self, xKing, yKing):
        i = 1
        self.rType = 0
        self.rotation = 0
        self.move = True
        self.others = []
        self.xKing = xKing
        self.yKing = yKing
        self.spType = 0
        self.rotate = False
        self.damn = random.randint(0, len(types) - 1)
        self.it = 0
        self.bType = ''
        for bums in types:
            
            if self.it == self.damn:
                
                self.bType = bums
            self.it += 1
        if self.xKing <= 10 and self.yKing <= 20:
            types[self.bType] +=1

        if self.xKing > 10 or self.yKing > 30:
            i = 20
        if self.bType == '4x4':
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing + i,self.yKing + i])
            self.others.append([self.xKing,self.yKing + i])
            self.spType = 2
        if self.bType == 'T':
            self.rotate = True
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing,self.yKing + i])
            self.spType = 2
        if self.bType == 'lLeft':
            self.rotate = True
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing - i,self.yKing + i])
            self.spType = 1
        if self.bType == 'lRight':
            self.rotate = True
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing + i,self.yKing + i])
            self.spType = 0
        if self.bType == 'zLeft':
            self.rotate = True
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing,self.yKing + i])
            self.others.append([self.xKing + i,self.yKing + i])
            self.spType = 1
        if self.bType == 'zRight':
            self.rotate = True
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing,self.yKing + i])
            self.others.append([self.xKing - i,self.yKing + i])
            self.spType = 0
        if self.bType == 'straight':
            self.rotate = True
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing + i * 2,self.yKing])
            self.spType = 1
            

    def reset(self, guide, bars, tp):
        self.move = True
        self.xKing = guide
        self.yKing = bars
        self.bType = tp
        self.others.clear()
        self.rotation = 0
        i = 1
        if self.xKing <= 10 and self.yKing <= 20:
            types[self.bType] +=1
        if self.xKing > 10 or self.yKing > 20:
            i = 20
        if self.bType == '4x4':
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing + i,self.yKing + i])
            self.others.append([self.xKing,self.yKing + i])
            self.spType = 2
        if self.bType == 'T':
            self.rotate = True
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing,self.yKing + i])
            self.spType = 2
        if self.bType == 'lLeft':
            self.rotate = True
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing - i,self.yKing + i])
            self.spType = 1
        if self.bType == 'lRight':
            self.rotate = True
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing + i,self.yKing + i])
            self.spType = 0
        if self.bType == 'zLeft':
            self.rotate = True
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing,self.yKing + i])
            self.others.append([self.xKing + i,self.yKing + i])
            self.spType = 1
        if self.bType == 'zRight':
            self.rotate = True
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing,self.yKing + i])
            self.others.append([self.xKing - i,self.yKing + i])
            self.spType = 0
        if self.bType == 'straight':
            self.rotate = True
            self.others.append([self.xKing - i,self.yKing])
            self.others.append([self.xKing + i,self.yKing])
            self.others.append([self.xKing + i * 2,self.yKing])
            self.spType = 1

    def spawn(self):
        sp = self.spType
        sprite = pygame.image.load(sprite_list[sp]).convert()
        sprite =  pygame.transform.scale(sprite, (18,18))
        if 0 <= self.xKing <= 20 and 1 <= self.yKing <= 30:
            for spot in self.others:
                screen.blit(sprite, (rows[spot[0]],collumns[spot[1]]))
            screen.blit(sprite, (rows[self.xKing],collumns[self.yKing]))
        else:
            for spot in self.others:
                screen.blit(sprite, (spot[0],spot[1]))
            screen.blit(sprite, (self.xKing,self.yKing))

    def getOthers(self):
        return self.others
    
    def fall(self):
        
        
        if self.move:
            self.yKing += 1
            
            i = 0
            while i < len(self.others):
                self.others[i][1] += 1
                i += 1
                
        
    def moveRight(self):
        
        if self.move:
            
                
            
            self.xKing += 1
            
            i = 0
            while i < len(self.others):
                self.others[i][0] += 1
                
                i += 1  
                  

    def moveLeft(self):
            
            if self.move:
                
                self.xKing -= 1
                
                i = 0
                while i < len(self.others):
                    self.others[i][0] -= 1
                    
                    i += 1  
                

    def spin(self):
        
        if self.rotate:
            i = 1
            
            if self.bType == 'T':
                if self.rotation == 3:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing,self.yKing + i])
                    self.rotation = 0
                elif self.rotation == 0:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing,self.yKing - i])
                    self.others.append([self.xKing,self.yKing + i])
                    self.rotation += 1
                elif self.rotation == 1:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing,self.yKing - i])
                    self.rotation += 1
                elif self.rotation == 2:
                    self.others.clear()
                    self.others.append([self.xKing,self.yKing + i])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing,self.yKing - i])
                    self.rotation += 1

            if self.bType == 'lLeft':
                
                if self.rotation == 3:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing - i,self.yKing + i])
                    self.rotation = 0
                elif self.rotation == 0:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing - i])
                    self.others.append([self.xKing,self.yKing - i])
                    self.others.append([self.xKing,self.yKing + i])
                    self.rotation += 1
                elif self.rotation == 1:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing - i])
                    self.rotation += 1
                elif self.rotation == 2:
                    self.others.clear()
                    self.others.append([self.xKing,self.yKing + i])
                    self.others.append([self.xKing + i,self.yKing + i])
                    self.others.append([self.xKing,self.yKing - i])
                    self.rotation += 1
            if self.bType == 'lRight':
                
                if self.rotation == 3:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing + i])
                    self.rotation = 0
                elif self.rotation == 0:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing + i])
                    self.others.append([self.xKing,self.yKing - i])
                    self.others.append([self.xKing,self.yKing + i])
                    self.rotation += 1
                elif self.rotation == 1:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing - i,self.yKing - i])
                    self.rotation += 1
                elif self.rotation == 2:
                    self.others.clear()
                    self.others.append([self.xKing,self.yKing + i])
                    self.others.append([self.xKing + i,self.yKing - i])
                    self.others.append([self.xKing,self.yKing - i])
                    self.rotation += 1

            if self.bType == 'zLeft':
                self.rType = 1
                if self.rotation == 1:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing + i])
                    self.others.append([self.xKing,self.yKing + i])
                    self.rotation = 0
                elif self.rotation == 0:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing,self.yKing - i])
                    self.others.append([self.xKing - i,self.yKing + i])
                    self.rotation += 1

            if self.bType == 'zRight':
                self.rType = 1
                if self.rotation == 1:
                    self.others.clear()
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing - i,self.yKing + i])
                    self.others.append([self.xKing,self.yKing + i])
                    self.rotation = 0
                elif self.rotation == 0:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing,self.yKing + i])
                    self.others.append([self.xKing - i,self.yKing - i])
                    self.rotation += 1
            if self.bType == 'straight':
                self.rType = 1
                if self.rotation == 1:
                    self.others.clear()
                    self.others.append([self.xKing - i,self.yKing])
                    self.others.append([self.xKing + i,self.yKing])
                    self.others.append([self.xKing + i * 2,self.yKing])
                    self.rotation = 0
                elif self.rotation == 0:
                    self.others.clear()
                    self.others.append([self.xKing,self.yKing - i * 2])
                    self.others.append([self.xKing,self.yKing - i])
                    self.others.append([self.xKing,self.yKing + i])
                    self.rotation += 1
       
            


def draw_used_spots():
    for spot in rS:
        g = 1
        while g <=20:
            
            if -1 < rS[spot][g] < 3 :
                sprite = pygame.image.load(sprite_list[rS[spot][g]]).convert()
                sprite = pygame.transform.scale(sprite, (18,18))
                screen.blit(sprite, (rows[spot],collumns[g]))
            g += 1

def check_lines():
    line_num = 0
    global lineCount
    global score
    things = 0
    j = 1
    k = 1
    while j <= 20:
        clear_break = False
        for spot in hit:
            if hit[spot][j]:
                things += 1

            else:
                clear_break = True
        if things == 10 and not clear_break:
            line_num += 1
            lineCount += 1
            score += 100
            for gen in hit:
                k = j
                hit[gen][j] = False
                rS[gen][j] = -1
                while k >= 1:
                    if hit[gen][k]:
                        n = hit[gen].get(k)
                        m = rS[gen].get(k)
                        
                        hit[gen][k + 1] = n
                        
                        rS[gen][k + 1] = m
                        
                        hit[gen][k] = False
                        rS[gen][k] = -1
                    k -= 1
                    
        things = 0
        j += 1
        
    
    


def draw_box(x,y,w,h):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(x,y,w,h),border_radius=5)
    pygame.draw.rect(screen, (0,225,225), pygame.Rect(x,y,w,h), 4,5)

def show_count():
    run = 0
    for gum in types:
        count = font2.render(str(types[gum]).zfill(3), True, (255,255,255))
        screen. blit(count, (250, 160 + run))
        run += 50
    extra = font1.render(str(score).zfill(6), True, (225,225,255))
    lines = font1.render('LINES - ' + str(lineCount).zfill(3), True, (255,255,255))
    mun = font1.render(str(level).zfill(2), True, (255,255,255))
    screen.blit(extra, (624, 154))
    screen.blit(lines, (304,54))
    screen.blit(mun, (664,404))

def make_ui():
    screen.fill(color)
    draw_box(396,96,208,408)
    draw_box(300,50,300,50)
    draw_box(600,50,200,150)
    draw_box(600, 225, 150,150)
    draw_box(600, 375, 175, 75)
    draw_box(100,150,300,354)

    screen.blit(next_up, (624,229))
    screen.blit(top, (624,54))
    screen.blit(thing, (624,84))
    screen.blit(scr, (624, 124))
    screen.blit(lv, (624,374))

    block2.spawn()
    draw_used_spots()
    t_block.spawn()
    sq_block.spawn()
    lLeft_block.spawn()
    lRight_block.spawn()
    str_block.spawn()
    zLeft_block.spawn()
    zRight_block.spawn()
    show_count()
    check_lines()
    try:
        block1.spawn()
    except KeyError:
            l = pygame.image.load(sprite_list[block1.spType]).convert()
            l = pygame.transform.scale(l, (18,18))

            lMax = block1.xKing
            rMax = block1.xKing
            for punks in block1.others:
                if punks[0] < lMax:
                    lMax = punks[0]
                elif punks[0] > rMax:
                    rMax = punks[0]
            if lMax == 0:
                block1.moveRight()
                
                
                make_ui()
                    
                
            elif rMax == 12:
                block1.moveLeft()
                block1.moveLeft()
                try:
                    make_ui()
                    
                except KeyError:
                    pass
            elif rMax == 11:
                block1.moveLeft()
                try:
                    make_ui()
                    
                except KeyError:
                    pass
            else:
                screen.blit(l, (rows[block1.xKing], collumns[block1.yKing]))
                for guy in block1.others:
                    if guy[1] < 1:
                        pass
                    else:
                        screen.blit(l, (rows[guy[0]],collumns[guy[1]]))
    

high_score= 5000

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
color = (125, 125, 125)
font1 = pygame.font.SysFont('liberationmono', 40)
font2 = pygame.font.SysFont('liberationmono', 30)

next_up = font1.render('NEXT', True, (255, 255, 255))
top = font1.render('TOP', True, (225,225,255))
thing = font1.render(str(high_score).zfill(6), True, (225,225,255))
scr = font1.render('SCORE', True, (255,255,255))
lv = font1.render('LEVEL', True, (255,255,255))


# Changing screen color
screen.fill(color)
# Board setup
draw_box(396,96,208,408)
draw_box(300,50,300,50)
draw_box(600,50,200,150)
draw_box(600, 225, 150,150)
draw_box(600, 375, 175, 75)
draw_box(100,150,300,354)

screen.blit(next_up, (624,229))
screen.blit(top, (624,54))
screen.blit(thing, (624,84))
screen.blit(scr, (624, 124))
screen.blit(lv, (624,374))
pygame.display.flip()
pygame.display.set_caption('Tetris')
# creating a bool value which checks
# if game is running
running = True
block1 = block(xKing=5, yKing=1)
block2 = block(xKing=660, yKing=289)
while block1.bType == block2.bType:
    types[block2.bType] -= 1
    block2 = block(xKing=660, yKing=289)
t_block = block(200, 200)
sq_block = block(200, 200)
lLeft_block = block(200, 200)
lRight_block = block(200, 200)
zLeft_block = block(200, 200)
zRight_block = block(200, 200)
str_block = block(200, 200)
t_block.reset(160, 160, 'T')
sq_block.reset(160, 210, '4x4')
zLeft_block.reset(160, 260, 'zLeft')
zRight_block.reset(160, 310, 'zRight')
lLeft_block.reset(160, 360, 'lLeft')
lRight_block.reset(160, 410, 'lRight')
str_block.reset(160, 460, 'straight')

















t = 0

# keep game running till running is true
while running:
    clock.tick(60)
    dela = int(100 / (1 + level))
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
        # if event is of type quit then 
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False
    
    make_ui()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        gaming = True
        
        try:
            h = -1
            w = -1
            if block1.bType == 'zLeft':
                if block1. rotation == 1:
                    if hit[block1.xKing + 1][block1.yKing + 1]:
                        gaming = False
                elif block1.rotation == 0:
                    if hit [block1.xKing - 1][block1.yKing + 1]:
                        gaming = False
            if block1.bType == 'zRight':
                if block1. rotation == 1:
                    if hit[block1.xKing - 1][block1.yKing - 1]:
                        gaming = False
                elif block1.rotation == 0:
                    if hit [block1.xKing - 1][block1.yKing + 1]:
                        gaming = False
            if block1.bType == 'lLeft':
                if block1. rotation == 3:
                    if hit[block1.xKing - 1][block1.yKing + 1]:
                        gaming = False
                elif block1.rotation == 0:
                    if hit [block1.xKing - 1][block1.yKing - 1]:
                        gaming = False
                elif block1.rotation == 1:
                    if hit[block1.xKing + 1][block1.yKing - 1]:
                        gaming = False
                elif block1.rotation == 2:
                    if hit[block1.xKing + 1][block1.yKing + 1]:
                        gaming = False
            if block1.bType == 'lRight':
                if block1. rotation == 3:
                    if hit[block1.xKing + 1][block1.yKing + 1]:
                        gaming = False
                elif block1.rotation == 0:
                    if hit [block1.xKing - 1][block1.yKing + 1]:
                        gaming = False
                elif block1.rotation == 1:
                    if hit[block1.xKing - 1][block1.yKing - 1]:
                        gaming = False
                elif block1.rotation == 2:
                    if hit[block1.xKing + 1][block1.yKing - 1]:
                        gaming = False

            while h < 2 or (block1.bType == 'straight' and h < 3):
                if hit[block1.xKing][block1.yKing + h]:
                    gaming = False
                h += 1
            while w < 2 or (block1.bType == 'straight' and w < 3):
                if hit[block1.xKing + w][block1.yKing]:
                    gaming = False
                w += 1
        except KeyError:
            pass
        if gaming:
            block1.spin()
            
            make_ui()
            pygame.time.delay(100)
            
            

    if keys[pygame.K_LEFT]:
        gaming = True
        lMax = block1.xKing
        try:
            if hit[block1.xKing - 1][block1.yKing]:
                gaming = False
        except KeyError:
            pass
        for punks in block1.others:
            if punks[0] < lMax:
                lMax = punks[0]
            try:
                if hit[punks[0] - 1][punks[1]]:
                    gaming = False
            except KeyError:
                pass
        if lMax > 1 and gaming:
            block1.moveLeft()
            make_ui()
            
            pygame.time.delay(100)
        else:
            continue
            
    if keys[pygame.K_RIGHT]:
        gaming = True
        rMax = block1.xKing
        try:
            if hit[block1.xKing + 1][block1.yKing]:
                gaming = False
        except KeyError:
            pass
        for punks in block1.others:
            if punks[0] > rMax:
                rMax = punks[0]
            try:
                if hit[punks[0] + 1][punks[1]]:
                    gaming = False
            except KeyError:
                pass
        if rMax < 10 and gaming:
            block1.moveRight()
            make_ui()
            
            pygame.time.delay(100)
        else:
            continue
                
            
    if keys[pygame.K_DOWN]:
        gaming = True
        yMax = block1.yKing
        try:
            if hit[block1.xKing][block1.yKing + 1]:
                gaming = False
        except KeyError:
            pass
        for punks in block1.others:
            if punks[1] > yMax:
                yMax = punks[1]
            try:
                if hit[punks[0]][punks[1] + 1]:
                    gaming = False
            except KeyError:
                pass
        if yMax < 20 and gaming:
            block1.fall()
            
            make_ui()
            
            pygame.time.delay(dela)
        else:
            
            
            block1.move = False
            rS[block1.xKing][block1.yKing] = block1.spType
            hit[block1.xKing][block1.yKing] = True
            
            for pair in range(len(block1.others)):
               
                rS[block1.others[pair][0]][block1.others[pair][1]] = block1.spType
                hit[block1.others[pair][0]][block1.others[pair][1]] = True
            
            block1.reset(5,1,block2.bType)
            block2 = block(xKing=660, yKing=289)
            while block1.bType == block2.bType:
                types[block2.bType] -= 1
                block2 = block(xKing=660, yKing=289)

            check_lines()
            
            pygame.time.delay(dela)
    
    if t >= 60:
        gaming = True
        yMax = block1.yKing
        try:
            if hit[block1.xKing][block1.yKing + 1]:
                gaming = False
        except KeyError:
            pass
        for punks in block1.others:
            if punks[1] > yMax:
                yMax = punks[1]
            try:
                if hit[punks[0]][punks[1] + 1]:
                    gaming = False
            except KeyError:
                pass
        if yMax < 20 and gaming:
            block1.fall()
            
            make_ui()
            t = 0
            
            
            
        else:
            
            
            
            rS[block1.xKing][block1.yKing] = block1.spType
            hit[block1.xKing][block1.yKing] = True
            
            for pair in range(len(block1.others)):
               
                rS[block1.others[pair][0]][block1.others[pair][1]] = block1.spType
                hit[block1.others[pair][0]][block1.others[pair][1]] = True
            
            block1.reset(5,0,block2.bType)
            block2 = block(xKing=660, yKing=289)
            while block1.bType == block2.bType:
                types[block2.bType] -= 1
                block2 = block(xKing=660, yKing=289)

            check_lines()
            
            pygame.time.delay(dela)
            
    else:
        t = t + (1 + level)
    if score >= threshold:
        level += 1
        threshold += 1000
    if score > high_score:
        high_score = score
    
    
    
    

    
    


    pygame.display.update()

pygame.quit()
