import pygame
#dimensions of the screen
screen = pygame.display.set_mode((600,600))

#color variables
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green =(0,255,0)
blue = (0,0,255)
screen.fill(white)
pygame.display.update()

# creating a Rectangle class // surf = surface
class Rect:
    def __init__(self,color,dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):
        self.draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)
      


# creating objects of class rectangle
greenRect = Rect(green, (50,20,100,100))
redRect = Rect(red, (165,130,150,150))
blueRect = Rect(blue, (325,290,200,200))




run = True

while run:
    greenRect.draw()
    redRect.draw()
    blueRect.draw()
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
