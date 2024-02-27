import pygame
import accountService as acc
import yaml
import os

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
font = pygame.font.Font('PyGameProject/bin/fonts/OpenSans-Regular.ttf', 18) #font, font size
fontUnderlined = pygame.font.Font('PyGameProject/bin/fonts/OpenSans-Regular.ttf', 18) #font, font size
fontUnderlined.set_underline(True)

#BUTTON SETUP
BUTTONUP = pygame.image.load("PyGameProject/bin/images/test.png").convert_alpha()
BUTTONDOWN = pygame.image.load("PyGameProject/bin/images/testdown.png").convert_alpha()
BUTTONIMG = BUTTONUP
submitRect = BUTTONIMG.get_rect(topleft=((screen.get_width()/2)+180,400)) #button position on screen

savedIMG = pygame.image.load("PyGameProject/bin/images/saved.png").convert_alpha()
newCharacterIMG = pygame.image.load("PyGameProject/bin/images/newCharacter.png").convert_alpha()
accountIMG = pygame.image.load("PyGameProject/bin/images/account.png").convert_alpha()
dndLogoIMG = pygame.transform.scale_by(pygame.image.load("PyGameProject/bin/images/dnd.png").convert_alpha(), .25)
dndTextIMG = pygame.transform.scale_by(pygame.image.load("PyGameProject/bin/images/dndtext.png").convert_alpha(), 1)

resetPassIMG = pygame.transform.scale_by(pygame.image.load("PyGameProject/bin/images/resetPass.png").convert_alpha(), 1)
clearDataIMG = pygame.transform.scale_by(pygame.image.load("PyGameProject/bin/images/clearData.png").convert_alpha(), 1)
deleteAccountIMG = pygame.transform.scale_by(pygame.image.load("PyGameProject/bin/images/deleteAccount.png").convert_alpha(), 1)
backButtonIMG = pygame.transform.scale_by(pygame.image.load("PyGameProject/bin/images/back.png").convert_alpha(), .15)
confirmButtonIMG = pygame.image.load("PyGameProject/bin/images/confirm.png").convert_alpha()

savedRect = savedIMG.get_rect(topleft=((10,150)))
newCharacterRect = newCharacterIMG.get_rect(topleft=((10,50)))
accountRect = accountIMG.get_rect(topleft=((10,250)))
dndLogoRect = dndLogoIMG.get_rect(topleft=((150,50)))
dndTextRect = dndTextIMG.get_rect(topleft=((80,350)))

resetPassRect = resetPassIMG.get_rect(topleft=((10,100)))
clearDataRect = clearDataIMG.get_rect(topleft=((10,200)))
deleteAccountRect = deleteAccountIMG.get_rect(topleft=((10,300)))
backButtonRect = backButtonIMG.get_rect(topleft=((0,0)))
confirmButtonRect = confirmButtonIMG.get_rect(topleft=((650,300)))

page = "login"

activeUser = []
#TEXTBOX SETUP
usernameTextboxData = ''
passwordTextboxData = ''
confirmPassData = ''
usernameTextbox = pygame.Rect((screen.get_width() / 2) + 100,200,140,32)
passwordTextbox = pygame.Rect((screen.get_width() / 2) + 100,300,140,32)
confirmPassTextbox = pygame.Rect((screen.get_width() / 2) + 100,400,140,32)
signupRect = pygame.Rect((screen.get_width() / 2) + 215,350,100,100)
loginRect = pygame.Rect((screen.get_width() / 2) + 235,350,100,100)
colorActive = pygame.Color('azure3')
colorPassive = pygame.Color('azure2')
color = colorPassive
color2 = colorPassive
color3 = colorPassive
usernameTextboxActive = False
passwordTextboxActive = False
confirmPassActive = False
canAcceptKeyTrue = True
signupButtonVisible = False
passwordWrong = False
userExists = False
deleting = False

displayText = "Filler"
changingPass = False



while running:
    BUTTONIMG = BUTTONUP

    #This will quit out of the game when the quit function is called
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#KEY ENTRY
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if submitRect.collidepoint(event.pos) and (page == "login" or page == "signup"): #submit button
                        BUTTONIMG = BUTTONDOWN
                        if page == "login":
                            form = acc.login(usernameTextboxData, passwordTextboxData)
                            if form == "404":
                                signupButtonVisible = True
                            elif form == "incpass":
                                passwordWrong = True
                                userExists = False
                                signupButtonVisible = False
                            else:
                                passwordWrong = False
                                userExists = False
                                signupButtonVisible = False
                                page = "menu"
                                activeUser = form
                        elif page == "signup":
                            form = acc.createProfile(usernameTextboxData, passwordTextboxData)
                            if form == "exists":
                                userExists = True
                                passwordWrong = False
                            else:
                                usernameTextboxData = ''
                                passwordTextboxData = ''
                    elif submitRect.collidepoint(event.pos) and page == "account":
                        BUTTONIMG = BUTTONDOWN
                        f = open("PyGameProject/profiles/"+activeUser['User']+".yaml","r")
                        list = yaml.full_load(f)
                        passTemp = list['Pass']
                        if passTemp == activeUser['Pass']:
                            if passwordTextboxData == confirmPassData:
                                activeUser['Pass'] = passwordTextboxData
                                f = open("PyGameProject/profiles/"+activeUser['User']+".yaml","wt")
                                yaml.dump(activeUser, f)
                                changingPass = False
                        
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
                    if confirmPassTextbox.collidepoint(event.pos):
                        confirmPassActive = True
                    else:
                        confirmPassActive = False
        if event.type == pygame.KEYDOWN:
             if canAcceptKey:
                #Username textbox
                if event.key == pygame.K_BACKSPACE and usernameTextboxActive == True:
                    usernameTextboxData = usernameTextboxData[:-1]
                elif event.key == pygame.K_TAB and usernameTextboxActive == True:
                    canAcceptKey = False
                    usernameTextboxActive = False
                    passwordTextboxActive = True
                elif event.key != pygame.K_BACKSPACE and usernameTextboxActive == True:
                    usernameTextboxData += event.unicode
                
                #Password textbox
                if event.key == pygame.K_BACKSPACE and passwordTextboxActive == True:
                    passwordTextboxData = passwordTextboxData[:-1]
                elif event.key == pygame.K_TAB and passwordTextboxActive == True and canAcceptKey and changingPass:
                    canAcceptKey = False
                    passwordTextboxActive = False
                    confirmPassActive = True
                elif event.key == pygame.K_TAB and passwordTextboxActive == True and canAcceptKey:
                    canAcceptKey = False
                    passwordTextboxActive = False
                elif event.key != pygame.K_BACKSPACE and passwordTextboxActive == True and canAcceptKey == True:
                    passwordTextboxData += event.unicode

                #Additional Textbox
                if event.key == pygame.K_BACKSPACE and confirmPassActive == True:
                    confirmPassData = confirmPassData[:-1]
                elif event.key != pygame.K_BACKSPACE and confirmPassActive == True and canAcceptKey == True:
                    confirmPassData += event.unicode

             if event.key == pygame.K_RETURN and passwordTextboxActive:
                passwordTextboxActive = False
                passwordTextboxData = passwordTextboxData[:-1]
                BUTTONIMG = BUTTONDOWN
                if page == "login":
                    form = acc.login(usernameTextboxData, passwordTextboxData)
                    if form == "404":
                        signupButtonVisible = True
                    elif form == "incpass":
                        passwordWrong = True
                        userExists = False
                        signupButtonVisible = False
                    else:
                        passwordWrong = False
                        userExists = False
                        signupButtonVisible = False
                        page = "menu"
                        activeUser = form
                elif page == "signup":
                    form = acc.createProfile(usernameTextboxData, passwordTextboxData)
                    if form == "exists":
                        userExists = True
                        passwordWrong = False
                    else:
                        usernameTextboxData = ''
                        passwordTextboxData = ''
             if event.key == pygame.K_RETURN and confirmPassActive:
                confirmPassActive = False
                confirmPassData = confirmPassData[:-1]
                BUTTONIMG = BUTTONDOWN
                f = open("PyGameProject/profiles/"+activeUser['User']+".yaml","r")
                list = yaml.full_load(f)
                passTemp = list['Pass']
                if passTemp == activeUser['Pass']:
                    if passwordTextboxData == confirmPassData:
                        activeUser['Pass'] = passwordTextboxData
                        f = open("PyGameProject/profiles/"+activeUser['User']+".yaml","wt")
                        yaml.dump(activeUser, f)
                        changingPass = False

        if event.type != pygame.KEYUP:
            canAcceptKey = True

            #MAIN MENU INTERACTIONS:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if savedRect.collidepoint(event.pos):
                    displayText = 'Saved Characters'
                if accountRect.collidepoint(event.pos):
                    displayText = 'Account Settings'
                    page = "account"
                if newCharacterRect.collidepoint(event.pos):
                    displayText = 'New Character Creator'
                if backButtonRect.collidepoint(event.pos):
                    page = "menu"
                    changingPass = False
                    deleting = False
                if resetPassRect.collidepoint(event.pos):
                    changingPass = True
                    usernameTextboxData = ''
                    passwordTextboxData = ''
                    confirmPassData = ''
                if deleteAccountRect.collidepoint(event.pos):
                    deleting = True
                if confirmButtonRect.collidepoint(event.pos):
                    os.remove("PyGameProject/profiles/"+activeUser['User']+".yaml")
                    pygame.quit()
        
#END OF KEY ENTRY AREA

    screen.fill("white")
    if usernameTextboxActive: 
        color = colorActive 
    else: 
        color = colorPassive

    if passwordTextboxActive: 
        color2 = colorActive 
    else: 
        color2 = colorPassive

    if confirmPassActive:
        color3 = colorActive
    else:
        color3 = colorPassive

    # pygame.draw.circle(screen, "red", pos, 40) #screen, color, position as a vector, radius
    if page == "login":
        #RENDER IMAGES AND INTERACTABLES
        screen.blit(BUTTONIMG, submitRect)
        screen.blit(dndLogoIMG, dndLogoRect)
        screen.blit(dndTextIMG, dndTextRect)
        pygame.draw.rect(screen, color, usernameTextbox)
        text_surface = font.render(usernameTextboxData, True, (0, 0, 0))

        pygame.draw.rect(screen, color2, passwordTextbox)
        text_surface2 = font.render(len(passwordTextboxData)*"*", True, (0, 0, 0))

        screen.blit(text_surface, (usernameTextbox.x+5, usernameTextbox.y+5)) 
        usernameTextbox.w = max(300, text_surface.get_width()+10)

        screen.blit(text_surface2, (passwordTextbox.x+5, passwordTextbox.y+5)) 
        passwordTextbox.w = max(300, text_surface2.get_width()+10)


        #RENDER TEXT
        if signupButtonVisible:
            signupText = fontUnderlined.render("Sign-Up", True, (0,0,0), (255,255,255))
            screen.blit(signupText, ((screen.get_width() / 2) + 215,350))

            wrongUserText = font.render("Username Not Found!", True, (255,0,0), (255,255,255))
            screen.blit(wrongUserText, ((screen.get_width() / 2) + 90,520))

        if passwordWrong:
            wrongPassText = font.render("Incorrect Password!", True, (255,0,0), (255,255,255))
            screen.blit(wrongPassText, ((screen.get_width() / 2) + 85,520))

        loginText = font.render("Login", True, (0,0,0), (255,255,255))
        screen.blit(loginText, ((screen.get_width() / 2) + 230,110))

        loginText = font.render("Username", True, (0,0,0), (255,255,255))
        screen.blit(loginText, ((screen.get_width() / 2) + 100,170))

        passText = font.render("Password", True, (0,0,0), (255,255,255))
        screen.blit(passText, ((screen.get_width() / 2) + 100,270))

    if page == "signup":
        signupButtonVisible = False
        #RENDER IMAGES AND INTERACTABLES
        screen.blit(BUTTONIMG, submitRect)
        screen.blit(dndLogoIMG, dndLogoRect)
        screen.blit(dndTextIMG, dndTextRect)
        pygame.draw.rect(screen, color, usernameTextbox)
        text_surface = font.render(usernameTextboxData, True, (0, 0, 0))

        pygame.draw.rect(screen, color2, passwordTextbox)
        text_surface2 = font.render(len(passwordTextboxData)*"*", True, (0, 0, 0))

        screen.blit(text_surface, (usernameTextbox.x+5, usernameTextbox.y+5)) 
        usernameTextbox.w = max(300, text_surface.get_width()+10)

        screen.blit(text_surface2, (passwordTextbox.x+5, passwordTextbox.y+5)) 
        passwordTextbox.w = max(300, text_surface2.get_width()+10)

        #RENDER TEXT
        if userExists:
            userExistsText = font.render("Username Taken!", True, (255,0,0), (255,255,255))
            screen.blit(userExistsText, ((screen.get_width() / 2) - 25,520))

        signupText = fontUnderlined.render("Login", True, (0,0,0), (255,255,255))
        screen.blit(signupText, ((screen.get_width() / 2) + 235,350))

        loginText = font.render("Sign-Up", True, (0,0,0), (255,255,255))
        screen.blit(loginText, ((screen.get_width() / 2) + 220,110))

        loginText = font.render("Username", True, (0,0,0), (255,255,255))
        screen.blit(loginText, ((screen.get_width() / 2) + 100,170))

        passText = font.render("Password", True, (0,0,0), (255,255,255))
        screen.blit(passText, ((screen.get_width() / 2) + 100,270))

    if page == "menu":
        usernameTextboxActive = False
        passwordTextboxActive = False
        canAcceptKeyTrue = True
        signupButtonVisible = False
        passwordWrong = False
        userExists = False

        screen.blit(savedIMG, savedRect)
        screen.blit(newCharacterIMG, newCharacterRect)
        screen.blit(accountIMG, accountRect)


        passText = font.render("User: "+activeUser['User'], True, (0,0,0), (255,255,255))
        screen.blit(passText, (10,10))

        displayTextS = font.render(displayText, True, (0,0,0), (255,255,255))
        screen.blit(displayTextS, (400,10))

    if page == "account":
        dpassText = font.render("User: "+activeUser['User'], True, (0,0,0), (255,255,255))
        screen.blit(passText, (800,10))

        screen.blit(resetPassIMG, resetPassRect)
        screen.blit(clearDataIMG, clearDataRect)
        screen.blit(deleteAccountIMG, deleteAccountRect)
        screen.blit(backButtonIMG, backButtonRect)

        if changingPass:
            submitRect = BUTTONIMG.get_rect(topleft=((screen.get_width()/2)+180,500))
            screen.blit(BUTTONIMG, submitRect)

            pygame.draw.rect(screen, color, usernameTextbox)
            text_surface = font.render(len(usernameTextboxData)*"*", True, (0, 0, 0))
            pygame.draw.rect(screen, color2, passwordTextbox)
            text_surface2 = font.render(len(passwordTextboxData)*"*", True, (0, 0, 0))
            pygame.draw.rect(screen, color3, confirmPassTextbox)
            text_surface3 = font.render(len(confirmPassData)*"*", True, (0, 0, 0))

            screen.blit(text_surface, (usernameTextbox.x+5, usernameTextbox.y+5)) 
            usernameTextbox.w = max(300, text_surface.get_width()+10)
            screen.blit(text_surface3, (confirmPassTextbox.x+5, confirmPassTextbox.y+5))
            confirmPassTextbox.w = max(300, text_surface3.get_width()+10)
            screen.blit(text_surface2, (passwordTextbox.x+5, passwordTextbox.y+5)) 
            passwordTextbox.w = max(300, text_surface2.get_width()+10)

            loginText = font.render("Current Password", True, (0,0,0), (255,255,255))
            screen.blit(loginText, ((screen.get_width() / 2) + 100,170))
            newPassText = font.render("New Password", True, (0,0,0), (255,255,255))
            screen.blit(newPassText, ((screen.get_width() / 2) + 100,270))
            confirmPassText = font.render("Confirm New Password", True, (0,0,0), (255,255,255))
            screen.blit(confirmPassText, ((screen.get_width() / 2) + 100,370))
        if deleting:
            screen.blit(confirmButtonIMG, confirmButtonRect)

            warningText = font.render("All data will be lost and unrecoverable, are you sure you want to delete your account?", True, (0,0,0), (255,255,255))
            screen.blit(warningText, (400,270))
    
    if page == "newChar":
        dothisthing

    if page == "savedChar":
        dothisthing

    # text = font.render("Mouse Clicked", True, (0,0,0), (255,255,255)) #string, visible, text color, background color
    # if pygame.mouse.get_pressed()[0]:
    #     mouseClickPos = pygame.mouse.get_pos()
    #     screen.blit(text, mouseClickPos) #print to screen at position



    pygame.display.flip()

    clock.tick(60)
    dt = clock.tick(60) / 1000

pygame.quit()