import pygame
import accountService as acc

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
font = pygame.font.Font('PyGameProject/OpenSans-Regular.ttf', 18) #font, font size
fontUnderlined = pygame.font.Font('PyGameProject/OpenSans-Regular.ttf', 18) #font, font size
fontUnderlined.set_underline(True)

#BUTTON SETUP
BUTTONUP = pygame.image.load("PyGameProject/test.png").convert_alpha()
BUTTONDOWN = pygame.image.load("PyGameProject/testdown.png").convert_alpha()
BUTTONIMG = BUTTONUP
submitRect = BUTTONIMG.get_rect(topleft=((screen.get_width()/2)-74,400)) #button position on screen

page = "login"

#TEXTBOX SETUP
usernameTextboxData = ''
passwordTextboxData = ''
usernameTextbox = pygame.Rect((screen.get_width() / 2) - 150,200,140,32)
passwordTextbox = pygame.Rect((screen.get_width() / 2) - 150,300,140,32)
signupRect = pygame.Rect((screen.get_width() / 2) - 30,350,70,32)
loginRect = pygame.Rect((screen.get_width() / 2) - 30,350,50,32)
colorActive = pygame.Color('azure3')
colorPassive = pygame.Color('azure2')
color = colorPassive
color2 = colorPassive
usernameTextboxActive = False
passwordTextboxActive = False
canAcceptKeyTrue = True
signupButtonVisible = False

while running:
    BUTTONIMG = BUTTONUP

    #This will quit out of the game when the quit function is called
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if submitRect.collidepoint(event.pos): #submit button
                        BUTTONIMG = BUTTONDOWN
                        if page == "login":
                            form = acc.login(usernameTextboxData, passwordTextboxData)
                            if form == "404":
                                signupButtonVisible = True
                            elif form == "incpass":
                                print("Wrong password")
                        elif page == "signup":
                            form = acc.createProfile(usernameTextboxData, passwordTextboxData)
                            if form == "exists":
                                print("Username exists")
                            else:
                                print("created")
                    if signupButtonVisible and signupRect.collidepoint(event.pos): #SIGN UP BUTTON
                        page = "signup"
                    if page == "signup" and loginRect.collidepoint(event.pos): #LOGIN BUTTON
                        page = "login"
                    if usernameTextbox.collidepoint(event.pos): #username textbox
                         usernameTextboxActive = True
                    else:
                         usernameTextboxActive = False
                    if passwordTextbox.collidepoint(event.pos): #password textbox
                         passwordTextboxActive = True
                    else:
                         passwordTextboxActive = False
        if event.type == pygame.KEYDOWN:
             if canAcceptKey:
                #Username textbox
                if event.key == pygame.K_BACKSPACE and usernameTextboxActive == True:
                    usernameTextboxData = usernameTextboxData[:-1]
                elif event.key == pygame.K_TAB and usernameTextboxActive == True:
                    canAcceptKey = False
                    usernameTextboxActive = False
                    passwordTextboxActive = True
                    print("Tabbed 1")
                elif event.key != pygame.K_BACKSPACE and usernameTextboxActive == True:
                    usernameTextboxData += event.unicode
                
                #Password textbox
                if event.key == pygame.K_BACKSPACE and passwordTextboxActive == True:
                    passwordTextboxData = passwordTextboxData[:-1]
                elif event.key == pygame.K_TAB and passwordTextboxActive == True and canAcceptKey:
                    canAcceptKey = False
                    passwordTextboxActive = False
                    print("Tabbed 2")
                elif event.key != pygame.K_BACKSPACE and passwordTextboxActive == True and canAcceptKey == True:
                    passwordTextboxData += event.unicode

        if event.type != pygame.KEYUP:
            canAcceptKey = True
        


    screen.fill("white")
    if usernameTextboxActive: 
        color = colorActive 
    else: 
        color = colorPassive

    if passwordTextboxActive: 
        color2 = colorActive 
    else: 
        color2 = colorPassive

    # pygame.draw.circle(screen, "red", pos, 40) #screen, color, position as a vector, radius
    if page == "login":
        #RENDER IMAGES AND INTERACTABLES
        screen.blit(BUTTONIMG, submitRect)
        pygame.draw.rect(screen, color, usernameTextbox)
        text_surface = font.render(usernameTextboxData, True, (0, 0, 0))

        pygame.draw.rect(screen, color2, passwordTextbox)
        text_surface2 = font.render(passwordTextboxData, True, (0, 0, 0))

        screen.blit(text_surface, (usernameTextbox.x+5, usernameTextbox.y+5)) 
        usernameTextbox.w = max(300, text_surface.get_width()+10)

        screen.blit(text_surface2, (passwordTextbox.x+5, passwordTextbox.y+5)) 
        passwordTextbox.w = max(300, text_surface2.get_width()+10)

        #RENDER TEXT
        if signupButtonVisible:
            signupText = fontUnderlined.render("Sign-Up", True, (0,0,0), (255,255,255))
            screen.blit(signupText, ((screen.get_width() / 2) - 30,350))

        loginText = font.render("Login", True, (0,0,0), (255,255,255))
        screen.blit(loginText, ((screen.get_width() / 2) - 25,110))

        loginText = font.render("Username", True, (0,0,0), (255,255,255))
        screen.blit(loginText, ((screen.get_width() / 2) - 150,170))

        passText = font.render("Password", True, (0,0,0), (255,255,255))
        screen.blit(passText, ((screen.get_width() / 2) - 150,270))

    if page == "signup":
        signupButtonVisible = False
        #RENDER IMAGES AND INTERACTABLES
        screen.blit(BUTTONIMG, submitRect)
        pygame.draw.rect(screen, color, usernameTextbox)
        text_surface = font.render(usernameTextboxData, True, (0, 0, 0))

        pygame.draw.rect(screen, color2, passwordTextbox)
        text_surface2 = font.render(passwordTextboxData, True, (0, 0, 0))

        screen.blit(text_surface, (usernameTextbox.x+5, usernameTextbox.y+5)) 
        usernameTextbox.w = max(300, text_surface.get_width()+10)

        screen.blit(text_surface2, (passwordTextbox.x+5, passwordTextbox.y+5)) 
        passwordTextbox.w = max(300, text_surface2.get_width()+10)

        #RENDER TEXT
        signupText = fontUnderlined.render("Login", True, (0,0,0), (255,255,255))
        screen.blit(signupText, ((screen.get_width() / 2) - 30,350))

        loginText = font.render("Sign-Up", True, (0,0,0), (255,255,255))
        screen.blit(loginText, ((screen.get_width() / 2) - 40,110))

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