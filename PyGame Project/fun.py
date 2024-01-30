import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
font = pygame.font.Font('PyGame Project/OpenSans-Regular.ttf', 18) #font, font size

#BUTTON SETUP
BUTTONUP = pygame.image.load("PyGame Project/test.png").convert_alpha()
BUTTONDOWN = pygame.image.load("PyGame Project/testdown.png").convert_alpha()
BUTTONIMG = BUTTONUP
BUTTONRECT = BUTTONIMG.get_rect(topleft=((screen.get_width()/2)-74,400)) #button position on screen

#TEXTBOX SETUP
userText = ''
userText2 = ''
inputRect = pygame.Rect((screen.get_width() / 2) - 150,200,140,32)
inputRect2 = pygame.Rect((screen.get_width() / 2) - 150,300,140,32)
colorActive = pygame.Color('azure3')
colorPassive = pygame.Color('azure2')
color = colorPassive
color2 = colorPassive
active = False
active2 = False
canAcceptKeyTrue = True

while running:
    BUTTONIMG = BUTTONUP

    #This will quit out of the game when the quit function is called
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if BUTTONRECT.collidepoint(event.pos):
                        BUTTONIMG = BUTTONDOWN
                    if inputRect.collidepoint(event.pos): #username textbox
                         active = True
                    else:
                         active = False
                    if inputRect2.collidepoint(event.pos): #password textbox
                         active2 = True
                    else:
                         active2 = False
        if event.type == pygame.KEYDOWN:
             if canAcceptKey:
                #Username textbox
                if event.key == pygame.K_BACKSPACE and active == True:
                    userText = userText[:-1]
                elif event.key == pygame.K_TAB and active == True:
                    canAcceptKey = False
                    active = False
                    active2 = True
                    print("Tabbed 1")
                elif event.key != pygame.K_BACKSPACE and active == True:
                    userText += event.unicode
                
                #Password textbox
                if event.key == pygame.K_BACKSPACE and active2 == True:
                    userText2 = userText2[:-1]
                elif event.key == pygame.K_TAB and active2 == True and canAcceptKey:
                    canAcceptKey = False
                    active2 = False
                    print("Tabbed 2")
                elif event.key != pygame.K_BACKSPACE and active2 == True:
                    userText2 += event.unicode

        if event.type != pygame.KEYUP:
            canAcceptKey = True
        


    screen.fill("white")
    if active: 
        color = colorActive 
    else: 
        color = colorPassive

    if active2: 
        color2 = colorActive 
    else: 
        color2 = colorPassive

    # pygame.draw.circle(screen, "red", pos, 40) #screen, color, position as a vector, radius
    screen.blit(BUTTONIMG, BUTTONRECT)
    pygame.draw.rect(screen, color, inputRect)
    text_surface = font.render(userText, True, (0, 0, 0))

    pygame.draw.rect(screen, color2, inputRect2)
    text_surface2 = font.render(userText2, True, (0, 0, 0))

    screen.blit(text_surface, (inputRect.x+5, inputRect.y+5)) 
    inputRect.w = max(300, text_surface.get_width()+10)

    screen.blit(text_surface2, (inputRect2.x+5, inputRect2.y+5)) 
    inputRect2.w = max(300, text_surface2.get_width()+10)

    loginText = font.render("Username", True, (0,0,0), (255,255,255))
    screen.blit(loginText, ((screen.get_width() / 2) - 150,170))

    passText = font.render("Password", True, (0,0,0), (255,255,255))
    screen.blit(passText, ((screen.get_width() / 2) - 150,270))

    # text = font.render("Mouse Clicked", True, (0,0,0), (255,255,255)) #string, visible, text color, background color
    # if pygame.mouse.get_pressed()[0]:
    #     mouseClickPos = pygame.mouse.get_pos()
    #     screen.blit(text, mouseClickPos) #print to screen at position



    pygame.display.flip()

    clock.tick(60)
    dt = clock.tick(60) / 1000

pygame.quit()