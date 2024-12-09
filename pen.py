import pygame
screen = pygame.display.set_mode([500,500])

# color  variable
pink = (255,0,127)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
screen.fill(white)

class myCircle:
    def __init__(self,color,pos,rad,wid=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.width = wid
        self.screen = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.screen,
                                                self.color, 
                                                self.pos, 
                                                self.rad, 
                                                self.width)
    def grow(self, r):
        self.rad = self.rad + r
        self.draw_circle = pygame.draw.circle(self.screen,
                                                self.color, 
                                                self.pos, 
                                                self.rad, 
                                                self.width)

positn = (250,250)
#creating object
pinkcircle = myCircle(pink, positn, 30, 10) 
bluecircle = myCircle(blue, positn, 20,0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pinkcircle.draw()
            bluecircle.draw()
            pygame.display.update()
            
        elif event.type == pygame.MOUSEBUTTONUP:
            pinkcircle.grow(2)
            bluecircle.grow(2)
            pygame.display.update() 
       
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            greencircle = myCircle(green, pos,5, 0)
            greencircle.draw()
            pygame.display.update()
