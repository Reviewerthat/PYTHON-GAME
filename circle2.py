import pygame
screen = pygame.display.set_mode((550,550))

# colours
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)


screen.fill(white)

pygame.display.update()
class Circle:
    def __init__(self,color,position,radius,width):
        self.circle_clr = color
        self.circle_pos = position
        self.circle_rad = radius
        self.circle_width = width
        self.circle_surf = screen
        
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surf, 
                                                self.circle_clr,
                                                self.circle_pos, 
                                                self.circle_rad, 
                                                self.circle_width )
    
    def grow(self, r):
        self.circle_rad  = self.circle_rad + r
        self.draw_circle = pygame.draw.circle(self.circle_surf, 
                                                self.circle_clr,
                                                self.circle_pos, 
                                                self.circle_rad, 
                                                self.circle_width )

        

        

# creating objects of class circle
c1 = Circle(blue, (225,225),25, 15)
c2 = Circle('red', (115,115),10,0)



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(white)
            c1.draw()
            c2.draw()
            
            pygame.display.update()
        
        elif  event.type == pygame.MOUSEBUTTONUP:
            screen.fill(white)
            c1.grow(5)
            c2.grow(15)

            pygame.display.update()
