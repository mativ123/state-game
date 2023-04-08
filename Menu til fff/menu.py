import pygame 
import sys 
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
color_red = (255,0,0)  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Castellar',25) 
smallfont1 = pygame.font.SysFont('Castellar',55)   
# rendering a text written in 
# this font 
text = smallfont.render('Quit' , True , color) 
text1 = smallfont.render('Start Game' , True , color)
text2 = smallfont.render('Chronicles' , True , color)
textover = smallfont1.render('Funky Fowl Frenzy', True , color_red)

#Loads picture
andImg = pygame.image.load('./Menu til fff/and med pistol.png')

def andpic(x,y):
    screen.blit(andImg, (x,y))

x =  (width/14)
y = (height/7)


while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2-90 <= mouse[0] <= width/2+140-50 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
            
            if width/2-90 <= mouse[0] <= width/2+140-50 and height/2-60 <= mouse[1] <= height/2-20:
                print("lore")

            if width/2-90 <= mouse[0] <= width/2+140-50 and height/2-180 <= mouse[1] <= height/2-80:
                print("start")

    # fills the screen with a color 
    screen.fill((0,0,0)) 

    andpic(x,y)

    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if width/2-90 <= mouse[0] <= width/2+140-50 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2-90,height/2,180,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2-90,height/2,180,40]) 
    
    if width/2-90 <= mouse[0] <= width/2+140-50 and height/2-60 <= mouse[1] <= height/2-20: 
        pygame.draw.rect(screen,color_light,[width/2-90,height/2-60,180,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2-90,height/2-60,180,40]) 
    
    if width/2-90 <= mouse[0] <= width/2+140-50 and height/2-120 <= mouse[1] <= height/2-80: 
        pygame.draw.rect(screen,color_light,[width/2-90,height/2-120,180,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2-90,height/2-120,180,40]) 
    
    # superimposing the text onto our button 
    screen.blit(text , (width/2-90+50,height/2+5)) 
    
    screen.blit(text1 , (width/2-88,height/2-115)) 

    screen.blit(textover , (width/2-340,height/2-300)) 

    screen.blit(text2 , (width/2-88,height/2-55))

    # updates the frames of the game 
    pygame.display.update() 