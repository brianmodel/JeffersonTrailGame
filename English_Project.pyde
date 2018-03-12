from time import sleep
import random

def setup():
    global part
    colorMode(RGB)
    size(1020, 650)
    background(0)
    part = 0
    
    #Intro Screen
    global font, font2, img, state, temp1, hold, topwrite, wordswrite
    font = loadFont('PlantagenetCherokee-48.vlw')
    font2 = createFont('8bitoperator_jve.ttf', 32) #The two fonts that I have
    img = loadImage('curl.png')
    state = False
    temp1=0
    hold = 0
    topwrite = False
    wordswrite = False

    #The Background and Landscape
    global treeImg, treeImg2, treeImg3, treeplace, treeplace2, treeplace3
    treeImg = loadImage('tree.png')
    treeImg.resize(100,100)
    treeImg2 = loadImage('tree.png')
    treeImg2.resize(100,100)
    treeImg3 = loadImage('tree.png')
    treeImg3.resize(100,100)
    treeplace = -40
    treeplace2 = 535
    treeplace3 = 220
    
    #The Map Part
    global mapImg
    mapImg= loadImage('map.jpg')
    mapImg.resize(700, 500)
    
    #The character part
    global xloc, yloc, characters, temp2, characters_2
    xloc = 50 #where the information will be written
    yloc = 50
    characters = ['Darl','Jewel','Addie','Anse','Vardaman','Dewey Dell', 'Cash']
    temp2 = False
    characters_2 = ['Anse', 'Addie', 'Cash', 'Jewel', 'Dewey Dell', 'Darl', 'Vardaman']
    
    '''
    It will scroll, so when an arrow key is pressed, the value of 
    one of these variables will change. Only these two are needed, 
    and I will use pushMatrix() in order to have all the text be 
    in different positions while using the same variable
    '''
    
    
    #The Walking Part 
    global img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, num, xcor, ycor

    img1 = loadImage('1.png')
    img2 = loadImage('2.png')
    img3 = loadImage('3.png')
    img4 = loadImage('4.png')
    img5 = loadImage('5.png')
    img6 = loadImage('6.png')
    img7 = loadImage('7.png')
    img8 = loadImage('8.png')
    img9 = loadImage('9.png')
    img10 = loadImage('10.png')
    img11 = loadImage('11.png')
    img12 = loadImage('12.png')

    num=1

    #Condition screen
    global xpos, ypos, write, button
    xpos = 215
    ypos = 350
    write = False
    button=0
    condit_part = 0
    
    #Running the game
    global option, times, game_part
    #Game_part is specifically telling what part you are in the gameplay area
    option = 0 
    times =0
    game_part = 0

    #The Locations that we will go to, and the dates
    global locations, area, church, house,xpic, prevent, ready, firstgo, secondgo, keep, speed, churchbig, burninghouse, year_place, sams, river_pic, cem_pic, mottsbig, school, armstends, mottsons
    locations = ['Bundrens', 'New Hope Church', "Samson's", "Tulls' & Ford", "Armstids'", "Frenchman's Bend", "Mottson", "Gillespies'", "Cemetery"]
    area = 0
    date = area+19 #Just here for the sake of knowing relationship between date and area
   
    house = loadImage('Farmhouse.png')
    house.resize(200,200)
    church = loadImage('whitechurch.png')
    church.resize(200,200)
    burninghouse = loadImage('Burningbarn.png')
    burninghouse.resize(200,200)
    sams = loadImage('Sams.png')
    sams.resize(200,200)
    river_pic = loadImage('river.png')
    river_pic.resize(600,200)
    cem_pic = loadImage('tomb.png')
    cem_pic.resize(100,100)
    school = loadImage('school.png')
    school.resize(200,200)
    armstends = loadImage('ARMSTIDS.png')
    armstends.resize(500,500)
    mottsons = loadImage('Mottson.png')
    mottsons.resize(200,200)
    
    global cemeterybig, samsonsbig, riverbig, schoolbig, armstidbig, gilbig
    
    churchbig = loadImage('church.jpg')
    churchbig.resize(300, 450)
    mottsbig = loadImage('mottson.jpg')
    mottsbig.resize(400,450)
    cemeterybig = loadImage('cemeterybig.jpg')
    cemeterybig.resize(400,400)
    samsonsbig = loadImage('Samsonsbig.jpg')
    samsonsbig.resize(400,400)
    riverbig = loadImage('riverbig.jpg')
    riverbig.resize(400,400)
    schoolbig = loadImage('schoolbig.jpg')
    schoolbig.resize(400,400)
    armstidbig = loadImage('armstidebig.jpg')
    armstidbig.resize(400,400)
    gilbig = loadImage('gillbig.jpg')
    gilbig.resize(400,400)
    
    xpic = 600
    prevent = 0
    ready=False
    firstgo = True
    secondgo=False
    keep=0
    speed = 20
    if area!=6:
        year_place=1929
    else:
        year_place=1900
    
    #Health possibilities
    global health, health_part
    health = ['Good', "Bad", "Real Bad"]
    health_part = 0
    
    #Minigames
    global repeat, minichoice, minichoicetemp, finalize, firstmini
    repeat = 0
    minichoice = 0
    minichoicetemp=0
    finalize=False
    firstmini=True
    
    #Sound Stuff
    global intro_sound, brian_model, game_sound, no, jewel_dream_sound, juul_one_sound, condtion_screen_music, condition_screen_bool, brian_model_2, location_sound, location_sound_file, game_sound_2, sad_music, sad_music_bool
    no=False
    brian_model = 0
    brian_model_2=0
    add_library('sound')
    intro_sound = SoundFile(this, 'Jefferson_Trail_intro.mp3')
    game_sound = SoundFile(this, 'Jefferson-Trail-Dramatic_1.mp3')
    jewel_dream_sound = SoundFile(this, 'Jewel_dreaming.mp3')
    juul_one_sound = False
    condtion_screen_music = SoundFile(this, 'Condscreen.mp3')
    condition_screen_bool=False
    location_sound=0
    location_sound_file = SoundFile(this, 'locationarea.mp3')
    game_sound_2 = SoundFile(this, 'Walking_2.mp3')
    sad_music_bool = False
    sad_music = SoundFile(this, 'Jefferson-Trail-Game-Over.mp3')
    
    global adam_music, adam_music_bool
    adam_music=SoundFile(this,'Walking_2.mp3')
    adam_music_bool=False
    
    global arman_music, arman_music_bool
    arman_music = SoundFile(this,'Sad.mp3')
    arman_music_bool=False
    
    #Text Box
    global showbox
    showbox = False
    
    #Jewel intro
    global canwork, Jewel, setbutton, final, once
    canwork = False
    Jewel=False
    setbutton = 0
    final=False
    once=0

    #fishing intro
    global fishing, single_final
    fishing=False
    single_final = 0
    
    #highway intro
    global highway
    highway = False
    
    #quiz intro
    global bundrenquiz, single_time_andrew
    bundrenquiz = False
    single_time_andrew = 0
    
    #minigames start from within the game
    global frog_ingame, fish_ingame, highway_ingame, jewel_ingame, ready_for_brian, model, juul_value, highway_value, frog_value, fish_value, single_brian, juul_once, highway_once, frog_once, fish_once, quiz_ingame, quiz_once, quiz_value, just_once_time, quiz_once_time, please_work
    frog_ingame = False
    fish_ingame = False
    highway_ingame = False
    jewel_ingame = False
    ready_for_brian = False #yeah, im a prankster!
    model=0
    juul_value=False
    highway_value=False
    frog_value=False
    fish_value=False
    single_brian=0
    juul_once = False
    highway_once = False
    frog_once = False
    fish_once = False
    quiz_ingame =False 
    quiz_once = False
    quiz_value = False
    quiz_once_time = 0
    just_once_time = 0
    please_work=0
    
    #Jewel's game
    global w_a,w_x,w_y,w_c,w_z,w_t, w_temp,w_hitcountCASH,w_throws,w_g,w_h,w_hitcountVARDAMAN,w_r,w_u,w_hitcountdDELL,w_q,w_b,w_hitcountANSE
    global w_CASHimg, w_VARDAMANimg, w_ANSEimg, w_dDELLimg, w_ADDIEimg, w_JUULimg
    w_a = 0
    w_x = 0
    w_y = 0
    w_c = 0
    w_z = 0
    w_t = 0
    w_i = 0
    w_o = 0
    w_g = 0
    w_h = 0
    w_r = 0
    w_u = 0
    w_q = 0
    w_b = 0
    w_hitcountCASH = 0
    w_hitcountVARDAMAN = 0
    w_hitcountdDELL = 0
    w_hitcountANSE = 0
    w_throws = 0
    w_temp = False
    w_CASHimg = loadImage("smilly.jpg")
    w_CASHimg.resize(15,15)
    w_VARDAMANimg = loadImage("fish.png")
    w_VARDAMANimg.resize(15,15)
    w_ANSEimg = loadImage("teeth.jpg")
    w_ANSEimg.resize(15,15)
    w_dDELLimg = loadImage("abortion.jpg")
    w_dDELLimg.resize(15,15)
    w_ADDIEimg = loadImage("ruler.png")
    w_ADDIEimg.resize(15,15)
    w_JUULimg = loadImage("horse.jpg")
    w_JUULimg.resize(15,15)
    
    #Armans game
    global whiteballX, whiteballY, whitenum, arman_img, arman_img2, whiteballimg_fish,blueballX, blueballY, blueballRadius, arman_time, whiteball, arman_temp_value
    size(1020, 650)
    noStroke()
    textSize(50)
    arman_img = loadImage("fish_img.png")
    imageMode(CENTER)
    arman_img2= loadImage("Back of hand.png")
    imageMode(CENTER)
    whiteball = 0
    whiteballX = []
    whiteballY = []
    whitenum = 5
    img_fish = whitenum
    blueballX = 400
    blueballY = 300
    blueballRadius = 20 #the smaller the ball, the harder the game. In my opinion at least
    arman_time = 0
    for i in range(0, whitenum):
        whiteballX.append(random.randrange(30, width-30))
        whiteballY.append(random.randrange(30, height-30))
    arman_temp_value=False
    
    #Andrews game
    global Bundrensbegin
    Bundrensbegin = 0
    
    #Nick's game
    global single_time_nick, ready_nick,nick_game_temp1
    single_time_nick = 0
    ready_nick = True
    nick_game_temp1=0
    
    
    frameRate(30)
    # VARIABLES
    global CASHspeed, CASHgoal, CASHframe, CASHgameStart, CASHcrashed, CASHrobMode, CASHvictory
    CASHcrashed = False
    CASHgameStart = False
    CASHframe = 0
    CASHspeed = 0
    CASHgoal = 45
    CASHrobMode = False
    CASHvictory = True

    global CASHbumpX, CASHbumpY, CASHsprBump
    CASHbumpX = [0, 0, 0]
    CASHbumpY = 490
    CASHsprBump = loadImage("sprDitch.png")

    global CASHplayerpos, CASHsprL, CASHsprR, CASHsprN, CASHplayerimg, CASHlives, CASHlifedown
    CASHplayerpos = [320, 420]
    CASHsprL = loadImage("sprWagonL.png")
    CASHsprR = loadImage("sprWagonR.png")
    CASHsprN = loadImage("sprWagonN.png")
    CASHplayerimg = CASHsprN
    CASHlives = 3
    CASHlifedown = False

    # FONTS AND SPRITES
    global CASHfont
    CASHfont = createFont("Cone.ttf", 36, True)

    global CASHroad, CASHbg, CASHbg2, orig
    CASHroad = loadImage("road.png")
    CASHbg = loadImage("bg.png")
    CASHbg2 = loadImage("bg2.png")
    orig = loadImage("bg.png")
    
    #Frogger
    global p1X, p1Y, logPic1, logPic2, logPic3, riverPic, p1Pic, dirtPic, logPos, t, t1, t2, gameRun, adam_speed, raaab
    p1X = (width/2)-10
    p1Y = (height/5)+352
    logPic1 = loadImage("log1.png")
    logPic2 = loadImage("log2.png")
    logPic3 = loadImage("log3.png")
    riverPic = loadImage("water.png")
    p1Pic = loadImage("p1.png")
    dirtPic = loadImage("dirt2.png")
    
    logPos = []
    t = 0
    t1 = 0
    t2 = 0
    gameRun = 0
    adam_speed = []
    raaab = 60
    
    global frogger_bool, adam_once
    frogger_bool=False
    adam_once = 0
    
    global nick_music, nick_music_bool
    nick_music=SoundFile(this,'chill.mp3')
    nick_music_bool=False
    
    #Final quotes section
    global single_temp_final, value_temp_final,textboxbool
    single_temp_final = False
    value_temp_final = True
    textboxbool=True
    
def draw():   
    global part, adam_once,single_time_nick, highway, option, times, game_part, locations, area, health, health_part, ready, keep, minichoice, churchbig,intro_sound, brian_model, game_sound, Jewel, canwork, final, once, fishing, year_place, frog_ingame, fish_ingame, highway_ingame, jewel_ingame, juul_value, highway_value, frog_value, fish_value, quiz_ingame, quiz_once, quiz_value, single_brian, sams, mottsbig, cemeterybig, samsonsbig, riverbig, schoolbig, armstidbig, gilbig, single_time_andrew, single_final, condtion_screen_music, condition_screen_bool, brian_model_2, location_sound, location_sound_file
    global single_temp_final, value_temp_final, textboxbool
    #Intro Screen
    if part==0:
        intro()
        if part==0 and brian_model==0:
            intro_sound.play()
            brian_model+=2
    #The actual Game
    if part == 1:
        intro_sound.stop()
        minis_ingame()
        if game_part==0:
            #deleting the intro screen
            if times==0:
                background(0)
                times+=1
            #Starting off with condition screen
            condition_screen(locations[area],'June {}, {}'.format(area+19, year_place),health[health_part])
        elif game_part==1:
            if times==1:
                background(0)
                times=0
            brian_model+=1
            game_background()
            walk(1240, 250, .7)
            if brian_model==3:
                game_sound.play()
                brian_model+=1
            places()
            if condition_screen_bool==True:
                condtion_screen_music.stop()
                condition_screen_bool=False                
        elif game_part==2:
            if times==1:
                background(0)
                times=0
            charHealth()
        elif game_part==3:
            if times==1:
                background(0)
                times=0
            mapLook()
        elif game_part==4:
            if times==1:
                background(0)
                times=0
            talk_to_family()
        elif game_part==5: #where the big image of where you are is drawn
            game_sound.stop()
            brian_model=1
            if keep==0:
                background(0)
                keep+=1
            fill(255)
            textSize(40)
            textAlign(CENTER)
            text('Press Space to go back', width/2, height/2+275)
            textAlign(LEFT)
            #Each of these will show an image when a certain location is reached
            if area==1:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(churchbig, width/2,285)
                imageMode(CORNER)
                #quiz_value=True #//Add this idea to wherever you want the minigame screen to appear\\
            if area==2:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(samsonsbig, width/2,285) #image of samsons
                imageMode(CORNER)
            if area==3:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(riverbig, width/2,285) #image of tulls and ford
                imageMode(CORNER)
            if area==4:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(armstidbig, width/2,285) #image of armstids
                imageMode(CORNER)
            if area==5:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(schoolbig, width/2,285) #image of frenchman's bend
                imageMode(CORNER)
            if area==6:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(mottsbig, width/2,285) #image of mottson
                imageMode(CORNER)
            if area==7:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(gilbig, width/2,285) #image of gillespies
                imageMode(CORNER)
            if area==8:
                textAlign(CENTER)
                text(str(locations[area]), width/2, 40)
                textAlign(LEFT)
                imageMode(CENTER)
                image(cemeterybig, width/2,285) #image of cemetery
                imageMode(CORNER)
            global sad_music
            if location_sound==0 and area!=8:
                location_sound_file.play()
                location_sound+=1
            elif location_sound==0 and area==8:
                sad_music.play()
                location_sound+=1
            
            global single_temp_final, value_temp_final,textboxbool, characters_2

            if keyPressed and key==' ' and ready:
                if (not juul_value) and (not highway_value) and (not frog_value) and (not fish_value):
                    ready=False
                    game_part=1
                    keep=0
                    location_sound_file.stop()
                    location_sound=0
                    brian_model=0
                '''elif (not juul_value) and (not highway_value) and (not frog_value) and (not fish_value) and area==8:
                    if single_final==0:
                        background(0)
                        game_part=-1
                        single_final+=1
                    if textboxbool and value_temp_final:
                        textBox()   
                        textboxbool=False'''
                        
    
                if juul_value:
                    if single_brian==0:
                        background(0)
                        game_part=-1
                        single_brian+=1
                    jewel_ingame=True
                if highway_value:
                    if single_brian==0:
                        background(0)
                        game_part=-1
                        single_brian+=1
                    highway_ingame=True
                if frog_value:
                    if single_brian==0:
                        background(0)
                        game_part=-1
                        single_brian+=1                    
                    frog_ingame=True
                if fish_value:
                    if single_brian==0:
                        background(0)
                        game_part=-1
                        single_brian+=1                    
                    fish_ingame=True
                if quiz_value:
                    if single_brian==0:
                        background(0)
                        game_part=-1
                        single_brian+=1
                    quiz_ingame=True
                    
    if part ==2: #Learning about the characters
        characterInfo()
    if part==3: #There is where the minigames should go
        minigames_screen()
        if minichoice==1:
            jewel_intro()
            if Jewel==True:
                background(0)
                #aaronsgame.aarons_game()
                aarons_game()
        if minichoice==2:
            fishing_game()
            if fishing==True:                
                background(0)
                armans_game_full()
        if minichoice==3:
            frogger_game()
            if frogger_bool==True:
                if adam_once ==0:
                    background(0)
                    adam_once+=1
                frogger_game_full()
        if minichoice==4: #Highway Star
            highway_game()
            if highway==True:
                if single_time_nick==0:
                    background(0)
                    frame.setSize(640,480)
                    single_time_nick+=1
                cashDraw()
        '''if minichoice==5:
            quiz_game()
            if bundrenquiz==True:
                if single_time_andrew==0:
                    background(0)
                    frame.setSize(1150,600)
                    single_time_andrew+=1
                KnowYourBundrens()'''

    if part==4: #If the player says to end the game in the beginning
        background(0)
        noLoop()
        exit()
        
def intro():
    global img, font,font2, part, state, temp1, hold, topwrite, wordswrite, no
    imageMode(CORNER)
    xplace = width/2-350
    yplace=height/2
    textFont(font2)
    fill(244, 180, 66)
    textSize(90)
    textAlign(CENTER)
    if not topwrite:
        text("The Jefferson Trail", width/2, TOP)
        topwrite=True
    
    image(img, 0,120,width,40)
    
    #The text on the screen
    textAlign(LEFT)
    textSize(40)
    fill(255)
    if not wordswrite:
        text('You may:', xplace, yplace-80)
        text('1. Travel the trail', xplace+50, yplace-25)
        text('2. Learn about the characters', xplace+50, yplace+15)
        text('3. Play minigames', xplace+50, yplace+55)
        text('4. End', xplace+50, yplace+95)
        text('What is your choice? ', xplace, yplace+160)
        wordswrite = True
    
    #Taking user's input, printing it on the screen and storing a bool
    if keyPressed and key=='1' and hold==0:
        text(key, xplace+350,yplace+160)
        state=True #Now it can be deleted or enter can be pressed
        temp1+=1 #how much to add to the part, which tells where in the game we are
        hold+=1 #To prevent it counting more when someone holds the button
    elif keyPressed and key=='2' and hold==0:
        text(key, xplace+350,yplace+160)
        state=True
        temp1+=2
        hold+=1
    elif keyPressed and key=='3' and hold==0:
        text(key, xplace+350,yplace+160)
        state=True
        temp1+=3
        hold+=1
    elif keyPressed and key=='4' and hold==0:
        text(key, xplace+350,yplace+160)
        state=True
        temp1+=4
        hold+=1
    if keyPressed and key == BACKSPACE:
        background(0)
        state=False
        hold=0
        temp1=0
        topwrite = False
        wordswrite=False
    if keyPressed and key == ENTER and state==True:
        part+=temp1
        sleep(1)
        state=False
        hold=0

def walk(xcor, ycor, scaleFactor): #Animation for the thing to walk
    global img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, num
    #background(0) //Background does not change here because it would be behind the setting\\
    imageMode(CORNER)
    
    #Various images for the animation
    for i in range(12):
        if num==12:
            pushMatrix()
            scale(scaleFactor)
            image(img12,xcor, ycor)
            popMatrix()
            num=0
        elif num==11:
            pushMatrix()
            scale(scaleFactor)
            image(img11,xcor, ycor) 
            popMatrix()          
        elif num==10:
            pushMatrix()
            scale(scaleFactor)          
            image(img10,xcor, ycor)     
            popMatrix()       
        elif num==9:
            pushMatrix()
            scale(scaleFactor)        
            image(img9,xcor, ycor)  
            popMatrix()          
        elif num==8:
            pushMatrix()
            scale(scaleFactor)                 
            image(img8,xcor, ycor)
            popMatrix()          
        elif num==7:
            pushMatrix()
            scale(scaleFactor)          
            image(img7,xcor, ycor) 
            popMatrix()           
        elif num==6:
            pushMatrix()
            scale(scaleFactor)          
            image(img6,xcor, ycor)    
            popMatrix()        
        elif num==5:
            pushMatrix()
            scale(scaleFactor)       
            image(img5,xcor, ycor)  
            popMatrix()          
        elif num==4:
            pushMatrix()
            scale(scaleFactor)           
            image(img4,xcor, ycor)  
            popMatrix()          
        elif num==3:
            pushMatrix()
            scale(scaleFactor)          
            image(img3,xcor, ycor) 
            popMatrix()           
        elif num==2:
            pushMatrix()
            scale(scaleFactor)          
            image(img2,xcor, ycor)  
            popMatrix()          
        elif num==1:
            pushMatrix()
            scale(scaleFactor)          
            image(img1,xcor, ycor)   
            popMatrix()
    sleep(.1)  
    num+=1    

def game_background():
    global game_part,brian_model, game_sound,button, write, state, hold, locations, area, health, health_part, write, treeImg, treeImg2, treeImg3, treeplace, treeplace2, treeplace3, year_place
    background(0) #Background changes here so that it is behind the walking animation
    
    rectMode(CORNER)
    fill(41, 158, 33)
    rect(0,height/2-50, width, 100)
    
    fill(255)
    rect(0,height/2+100, width, 250)
    
    textAlign(CENTER)
    textSize(30)
    
    text('Press Space to size up the situation', width/2, height/2+85)
    
    textAlign(LEFT)
    fill(0)
    
    if area!=8:
        text('Date: June {}, {}'.format(area+19, year_place), 50, 475)
        text('Weather: Hot',50, 515)
        text('Health: {}'.format(health[health_part]),50, 555)
        text('Next Landmark: {}'.format(locations[area+1]),50, 595)
    
    if keyPressed and key==' ':
        game_part=0
        game_sound.stop()
        brian_model=0
        button =0
        write=False
        state=False
        hold=0
        textSize(40)
            
    if treeplace<width:
        treeplace+=5
        image(treeImg, treeplace, 175)
    if treeplace==width:
        treeplace=-100
    if treeplace2<width:
        treeplace2+=5
        image(treeImg2, treeplace2, 175)
    if treeplace2==width:
        treeplace2=-100
    if treeplace3<width:
        treeplace3+=5
        image(treeImg3, treeplace3, 175)
    if treeplace3==width:
        treeplace3=-100


def condition_screen(place, date, health):
    global xpos, ypos, hold, state, write, button, option, hold, game_part, condtion_screen_music, condition_screen_bool, intro_sound, area
    global single_final, game_part, textboxbool, value_temp_final
    if condition_screen_bool==False:
        intro_sound.stop()
        condtion_screen_music.play()
        condition_screen_bool=True
    fill(255)
    rectMode(CENTER)
    rect(width/2, height/2-175, 600, 70)
    fill(0)
    textSize(40)
    text('Weather: Hot', width/2-295, 150)
    text('Health: {}'.format(health), width/2-295, 175)
    if not write:
        fill(255)
        text('You may:', xpos, ypos-80)
        text('1. Continue on the trail', xpos+50, ypos-25)
        text('2. Check health', xpos+50, ypos+15)
        text('3. Look at map', xpos+50, ypos+55)
        text('4. Talk to family', xpos+50, ypos+95)
        text('What is your choice? ', xpos, ypos+150)
        fill(255)
        textAlign(CENTER)
        textSize(50)
        text(place, width/2, 40)
        text(date, width/2, 90)
        textAlign(LEFT)
        write=True
        
    fill(255)
    if keyPressed and key=='1' and hold==0: #Continue trail
        text(key, xpos+350, ypos+150)
        state=True
        hold+=1
        button+=1
    elif keyPressed and key=='2' and hold==0: #Check health
        text(key, xpos+350, ypos+150)
        state=True
        hold+=1
        button +=2
    elif keyPressed and key=='3' and hold==0: #look at map
        text(key, xpos+350, ypos+150)
        state=True
        hold+=1
        button+=3
    elif keyPressed and key=='4' and hold==0: #talk to family
        text(key, xpos+350, ypos+150)
        state=True
        hold+=1
        button +=4
    if keyPressed and key == BACKSPACE:
        background(0)
        state=False
        hold=0
        temp1=0
        write=False
        button =0
    if keyPressed and key == ENTER and state==True:
        if area!=8:
            game_part=button
        elif area==8:
            if button==1:
                if single_final==0:
                    background(0)
                    game_part=-1
                    single_final+=1
                if textboxbool and value_temp_final:
                    textBox()   
                    textboxbool=False
            else:
                game_part=button
                
def characterInfo():
    global xloc, yloc, characters, part, topwrite, wordswrite, temp1, hold, temp2
    frameRate(60)
    background(0)
    for i in range(len(characters)-1):
        pushMatrix()
        translate(0,i*250)
        text('{}:'.format(characters[i]), xloc, yloc+300)
        popMatrix()
    text('Cash:', xloc, yloc+1870)
    textSize(20)
    
    #Jefferson trail introduction
    text("The Jefferson Trail is a path leading from the rural farming communities of Yoknapatawpha County to the county's central", xloc-10, yloc)
    text("town of Jefferson, Missouri. Travelers must cross bridges and rivers along the way to Jefferson. The Bundren family,", xloc-10, yloc+30)
    text("farmers from Yoknapatawpha County, are on their way to Jefferson to hold a funeral for Addie, their mother. Although", xloc-10, yloc+60)
    text("the overall purpose of embarking on the Jefferson Trail is to bury Addie in Jefferson, each member of the family has a" , xloc-10, yloc+90)
    text("unique and selfish motive for accompanying Addie's remains on the trail. Let's examine each character and their reasoning", xloc-10, yloc+120)
    text("for traveling on this long, and at times, dangerous journey.", xloc-10, yloc+150)
    
    #Darl text
    text("The second oldest child in the family, and a war veteran. Darl served in the U.S. Army in France during World", xloc+100, yloc+300) 
    text("War I and eventually returned home to Yoknapatawpha County. He sees the extra affection that Addie shows to", xloc+100, yloc+330) 
    text("Jewel compared to the rest of her children, and becomes jealous. Darl seems to know everything about his ", xloc+100, yloc+360) 
    text("family, including family secrets. Darl also has the ability to communicate with his siblings without the use" , xloc+100, yloc+390) 
    text("of words. He is the only one in the family that does not appear to have an additional motive for traveling", xloc+100, yloc+420) 
    text("this path.", xloc+100, yloc+450)
    
    #Jewel text
    text("The third Bundren child and Addie's illegitimate son. Jewel was the result of an affair that Addie had",xloc+120, yloc+550) 
    text("with Whitfield. He and his mother had the strongest relationship in the family and it was clear to",xloc+120, yloc+580) 
    text("Jewel's siblings that he was Addie's favorite child. Jewel hates Anse and his siblings and hopes to leave",xloc+120, yloc+610) 
    text("the family's farm after Addie's burial. After secretly working on his neighbor's land for a while, Jewel",xloc+120, yloc+640) 
    text("bought his own horse, which he uses to detach himself from the rest of the Bundren family. Throughout",xloc+120, yloc+670) 
    text("this trip Jewel will be riding ahead on his horse rather than in the wagon with the rest of the family.",xloc+120, yloc+700) 
    
    #Addie text
    text("Anse's wife and the mother of five children. She was a schoolteacher before she married Anse, who she",xloc+120, yloc+800)
    text("hates. Addie despises Anse for making her feel like her life has no purpose. As a way of taking revenge",xloc+120, yloc+830)
    text("against her husband, Addie had an illegitimate child with Whitfield, the local minister. Addie has passed",xloc+120, yloc+860)
    text("away and requested to be buried with her family in Jefferson, as another way of taking revenge against",xloc+120, yloc+890)
    text("Anse. Her family obliges her request and is traveling to Jefferson for a funeral.",xloc+120, yloc+920)
    
    #Anse text
    text("The patriarch of the Bundren family. Anse is a senseless, unmotivated farmer who causes problems for his", xloc+120, yloc+1050)
    text("neighbors and does not repay them for their courtesies. He and Addie have had their share of marital", xloc+120, yloc+1080)
    text("troubles; Addie refused to give Anse children for ten years and had a child out of wedlock. Anse's teeth", xloc+120, yloc+1110)
    text("have fallen out of his mouth and he is eager to buy a new set of teeth in town as well as find a new", xloc+120, yloc+1140)
    text("wife now that Addie has passed away.", xloc+120, yloc+1170)
    
    #Vardaman text
    text("The youngest member of the Bundren family. Vardaman is not quite able to grasp the idea of his", xloc+190, yloc+1300)
    text("mother's passing. After thinking about the circumstances he reaches the conclusion that his", xloc+190, yloc+1330)
    text("mother must be a fish and the woman lying in the coffin is not his mother. Vardaman is excited", xloc+190, yloc+1360)
    text("for this trip to Jefferson because he hopes to get bananas and a toy train upon arrival.", xloc+190, yloc+1390)
    
    #Dewey Dell text
    text("The second youngest of the children and the first girl. When Addie died, Dewey Dell became", xloc+220, yloc+1550)
    text("the mother figure in the family and took over the tasks that Addie had performed. Shortly", xloc+220, yloc+1580)
    text("before Addie passed away, Dewey Dell was in a relationship with a boy named Lafe. She", xloc+220, yloc+1610)
    text("became pregnant and did not tell anyone in her family. However, Darl figured out her secret.", xloc+220, yloc+1640)
    text("Because Darl knows of her pregnancy and is attracted to Dewey Dell, she resents him. Before", xloc+220, yloc+1670)
    text("the family left for Jefferson, Dewey Dell angered Anse by telling him that one of her goals", xloc+220, yloc+1700)
    text("of the trip was to sell cakes, when in reality she was carrying clothes to wear to the town", xloc+220, yloc+1730)
    text("pharmacy in hopes of getting an abortion.", xloc+220, yloc+1760)
    
    #Cash text
    text("The oldest of the Bundren children. Cash is a carpenter in his early thirties and is a very logical thinker", xloc+100, yloc+1870)
    text("and a perfectionist. He expresses his love for his mother by building Addie's coffin just outside her window", xloc+100, yloc+1900)
    text("and showing her each plank he saws. Although Cash is the voice of reason in the family, he is mostly ignored", xloc+100, yloc+1930)
    text("by his siblings and Anse. On the Bundren family's trip to Jefferson, Cash hopes to earn extra money by fixing", xloc+100, yloc+1960)
    text("a neighbor's barn. He also hopes to buy a gramophone in town.", xloc+100, yloc+1990)
    
    fill(0)
    rect(0,600, width,50)
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text('Press Space to go back', width/2, 640) 
    if keyPressed and key ==' ' :
        background(0)
        topwrite = False
        wordswrite = False
        temp1=0
        hold=0
        part=0
    textAlign(LEFT)
    if keyPressed:
        temp2=True
    else:
        temp2=False
    if key==CODED and keyCode==UP and temp2==True:
        yloc+=5
    elif key==CODED and keyCode==DOWN and temp2==True:
        yloc-=5

def mapLook():
    global mapImg, game_part, write, state, hold, button
    imageMode(CENTER)
    image(mapImg, width/2,height/2-75)
    textAlign(CENTER)
    fill(255)
    text('Press Space to go back', width/2, height/2+275)
    if keyPressed and key==' ':
        game_part=0
        button =0
        write=False
        state=False
        hold=0
        textAlign(LEFT)
    
def charHealth():
    global characters, xloc, yloc, game_part, button, write, state, hold, area
    background(0)
    for i in range(len(characters)):
        pushMatrix()
        translate(0,i*50)
        fill(255)
        text('{}:'.format(characters[i]), 50, 50)
        stroke(255)
        strokeWeight(5)
        noFill()
        translate(0,i*2)
        rect(450, 30, 400, 20)
        popMatrix()
    noStroke()
    textAlign(CENTER)
    fill(255)
    text('Press Space to go back', width/2, height/2+275)
    if keyPressed and key==' ':
        game_part=0
        button =0
        write=False
        state=False
        hold=0
    textAlign(LEFT)
    
    rectMode(CORNER)
    global health_part
    #//PUT WHAT THE HEALTH SHOULD BE FOR EACH AREA HERE\\#
    if area==0:
        fill(30, 204, 30)
        rect(253,23,395,15)
        rect(253,75,395,15)
        rect(253,127,0,0)
        rect(253,179,395,15)
        rect(253,231,395,15)
        rect(253,283,395,15)
        rect(253,335,360,15)
        
        fill(255)
        text('Healthy', 700, 40)
        text('Healthy', 700, 92)
        text('Dead', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Healthy', 700, 300)
        text('Limp', 700, 352)
        
    if area==1:
        fill(30, 204, 30)
        rect(253,23,395,15)
        rect(253,75,395,15)
        rect(253,127,0,0)
        rect(253,179,395,15)
        rect(253,231,395,15)
        rect(253,283,395,15)
        rect(253,335,360,15)
        
        fill(255)
        text('Healthy', 700, 40)
        text('Healthy', 700, 92)
        text('Dead', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Healthy', 700, 300)
        text('Limp', 700, 352)
    if area==2:
        fill(30, 204, 30)
        rect(253,23,395,15)
        rect(253,75,395,15)
        rect(253,127,0,0)
        rect(253,179,395,15)
        rect(253,231,395,15)
        rect(253,283,350,15)
        rect(253,335,360,15)
        
        fill(255)
        text('Healthy', 700, 40)
        text('Healthy', 700, 92)
        text('Dead', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Nauseous', 700, 300)
        text('Limp', 700, 352)
    if area==3:
        fill(30, 204, 30)
        rect(253,23,395,15)
        rect(253,75,395,15)
        rect(253,127,0,0)
        rect(253,179,395,15)
        rect(253,231,395,15)
        rect(253,283,350,15)
        rect(253,335,300,15)
        
        fill(255)
        text('Mentally stable', 700, 40)
        text('Tired', 700, 92)
        text('Dead', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Nauseous', 700, 300)
        text('Low', 700, 352)
        health_part=1
    if area==4:
        fill(30, 204, 30)
        rect(253,23,395,15)
        rect(253,75,395,15)
        rect(253,127,0,0)
        rect(253,179,395,15)
        rect(253,231,395,15)
        rect(253,283,350,15)
        rect(253,335,250,15)
        
        fill(255)
        text('Mentally stable', 700, 40)
        text('Healthy', 700, 92)
        text('Dead', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Nauseous', 700, 300)
        text('Low', 700, 352)
    if area==5:
        fill(30, 204, 30)
        rect(253,23,0,0)
        rect(253,75,0,0)
        rect(253,127,395,15)
        rect(253,179,395,15)
        rect(253,231,0,0)
        rect(253,283,0,0)
        rect(253,335,0,0)
        
        fill(255)
        text('--UNBORN--', 700, 40)
        text('--UNBORN--', 700, 92)
        text('Healthy', 700, 144)
        text('Healthy', 700, 196)
        text('--UNBORN--', 700, 248)
        text('--UNBORN--', 700, 300)
        text('--UNBORN--', 700, 352)
    if area==6:
        fill(30, 204, 30)
        rect(253,23,395,15)
        rect(253,75,395,15)
        rect(253,127,-50,0)
        rect(253,179,395,15)
        rect(253,231,395,15)
        rect(253,283,280,15)
        rect(253,335,100,15)
        health_part=0
        
        fill(255)
        text('Mentally stable', 700, 40)
        text('Healthy', 700, 92)
        text('Dead and  very smelly', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Very nauseous', 700, 300)
        text('Very low', 700, 352)
        health_part=2
    if area==7:
        fill(30, 204, 30)
        rect(253,23,200,15)
        rect(253,75,300,15)
        rect(253,127,0,0)
        rect(253,179,395,15)
        rect(253,231,395,15)
        rect(253,283,280,15)
        rect(253,335,50,15)
        
        fill(255)
        text('Insane', 700, 40)
        text('Burnt', 700, 92)
        text('Dead', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Very nauseous', 700, 300)
        text('Very low', 700, 352)
    if area==8:
        fill(30, 204, 30)
        rect(253,23,50,15)
        rect(253,75,300,15)
        rect(253,127,0,0)
        rect(253,179,430,15)
        rect(253,231,395,15)
        rect(253,283,220,15)
        rect(253,335,25,15)
        
        fill(255)
        text('Very insane', 700, 40)
        text('Burnt', 700, 92)
        text('Dead', 700, 144)
        text('Healthy', 700, 196)
        text('Healthy', 700, 248)
        text('Pregnant', 700, 300)
        text('Very low', 700, 352)
    rectMode(CENTER)
def places():
    global locations, area, church, house, xpic, prevent, ready, firstgo, secondgo, game_part, speed, burninghouse, sams, river_pic, cem_pic, school, armstends, mottsons
    
    #What will show up once you reach a new location
    if ready:
        game_part=5
        
    #Moving the Bundren farm image from the right side of the screen to off
    if area ==0 and xpic<1100 and firstgo and (not ready):
        pushMatrix()
        translate(xpic, 0)
        image(house, 0, 123) #//This should be the image of the Bundren house\\
        popMatrix()
        xpic+=speed
    elif area==0 and xpic>=1100 and firstgo and (not ready):
        xpic=-125
        firstgo=False
        secondgo=True
        
    #waiting for the bundren house to be off the screen, and then brings the church out onto the screen
    if area==0 and xpic<900 and prevent==0 and secondgo:
        pushMatrix()
        translate(xpic, 0)
        image(church, 0, 95)
        popMatrix()
        xpic+=speed
        
    #waits until church reaches right side of the screen, and once it does, it says that it is ready for the big image of the church to
    #appear on the screen
    
    elif area==0 and xpic >=900 and prevent==0 and secondgo:
        prevent+=1
        area+=1
        secondgo=False
        ready=True
        xpic=-10
    
    
    if area==1 and xpic<950 and not ready:
        prevent=0
        pushMatrix()
        translate(xpic,0)
        image(sams,-100,112)#Image of Samsons
        popMatrix()
        xpic+=speed
    
    elif area==1 and xpic>=950 and prevent==0 and not ready:
        prevent+=1
        area+=1 
        ready=True
        xpic=-10
    
    if area==2 and xpic<700 and not ready:
        prevent=0
        pushMatrix()
        translate(xpic,0)
        image(river_pic,-200,173)#Image of Tull' and Ford
        popMatrix()
        xpic+=speed
    elif area==2 and xpic>=700 and prevent==0 and not ready:
        prevent+=1
        area+=1 
        ready=True
        xpic=-50
        
    if area==3 and xpic<950 and not ready:
        prevent=0
        pushMatrix()
        translate(xpic,0)
        image(armstends,0,14)#Image of Armstids'
        popMatrix()
        xpic+=speed
    elif area==3 and xpic>=950 and prevent==0 and not ready:
        prevent+=1
        area+=1 
        ready=True
        xpic=-50
    
    if area==4 and xpic<950 and not ready:
        prevent=0
        pushMatrix()
        translate(xpic,0)
        image(school,0,93)#Image of Frenchman's Bend
        popMatrix()
        xpic+=speed
    
    elif area==4 and xpic>=950 and prevent==0 and not ready:
        prevent+=1
        area+=1 
        ready=True
        xpic=-50
      
    if area==5 and xpic<950 and not ready:
        prevent=0
        pushMatrix()
        translate(xpic,0)
        image(mottsons,0,90)#Image of Mottson's
        popMatrix()
        xpic+=speed
    elif area==5 and xpic>=950 and prevent==0 and not ready:
        prevent+=1
        area+=1 
        ready=True
        xpic=-50
      
    if area==6 and xpic<950 and not ready:
        prevent=0
        pushMatrix()
        translate(xpic,0)
        image(burninghouse,0,110)#Image of Gillespies
        popMatrix()
        xpic+=speed
    elif area==6 and xpic>=950 and prevent==0 and not ready:
        prevent+=1
        area+=1 
        ready=True
        xpic=-50
        
    if area==7 and xpic<950 and not ready:
        prevent=0
        pushMatrix()
        translate(xpic,0)
        image(cem_pic,0,218)#Image of Cemetery
        popMatrix()
        xpic+=speed
    elif area==7 and xpic>=950 and prevent==0 and not ready:
        prevent+=1
        area+=1 
        ready=True
        xpic=-50
    
def minigames_screen():
    global repeat, part, topwrite, wordswrite, temp1, hold, minichoicetemp, minichoice, finalize, firstmini
    if repeat==0:
        background(0)
        textAlign(CENTER)
        textSize(60)
        text('Minigames:', width/2, 60)
        textAlign(LEFT)
        textSize(40)
        text("1. Jewel's Special Dream", 100, 200)
        text('2. Fishing for Mom', 100, 250)
        text('3. Crossy River', 100, 300)
        text('4. Jefferson Star', 100, 350)
        repeat+=1
        textAlign(CENTER)
        text('Press Space to go back', width/2, height/2+275)
        textAlign(LEFT)
        text('Your Choice: ', 100,450)
    if keyPressed and (key=='1' or key=='2' or key=='3' or key=='4') and firstmini:
        text(key, 325, 450)
        minichoicetemp= int(key)
        finalize=True
    if keyPressed and key==ENTER and finalize==True and firstmini:
        minichoice=minichoicetemp
        firstmini=False
    if keyPressed and key==BACKSPACE and firstmini==True:
        background(0)
        finalize=False
        minichoicetemp=0
        repeat=0
    if keyPressed and key ==' ' and firstmini==True:
        background(0)
        topwrite = False
        wordswrite = False
        temp1=0
        hold=0
        part=0
        repeat=0

def textBox():
    global sad_music, sad_music_bool, brian_model, game_sound,condtion_screen_music, condition_screen_bool, brian_model_2, location_sound, location_sound_file, game_sound_2, sad_music, sad_music_bool
    global topwrite, wordswrite, temp1, hold, part
    rectMode(CENTER)
    fill(0)
    noStroke()
    rect(width/2, 473, 511,115)
    strokeWeight(5)
    stroke(255)
    fill(0)
    rect(width/2, height/2, 600, 100, 7)
    rectMode(CORNER)
    fill(255)
    noStroke()
    fill(255)
    textAlign(CENTER, CENTER)
    textSize(30)
    text('Addie left your group and Mrs. Bundren 2 joined', width/2, height/2)
    textMode(CENTER)
def talk_to_family():
    global area, game_part, button, write, state, hold, characters_2
    textAlign(CENTER)
    text('Press Space to go back', width/2, height/2+275)
    textAlign(LEFT)
    if keyPressed and key==' ':
        game_part=0
        button =0
        write=False
        state=False
        hold=0
    for i in range(len(characters_2)):
        pushMatrix()
        translate(0,i*75)
        text('{}:'.format(characters_2[i]), 50, 50)
        popMatrix()
        
    #//PUT WHAT EACH FAMILY MEMBER SHOULD SAY HERE\\#
    if area==0: #Bundrens
        text('''"My wife is dead. Darn. I guess I'll go to town ''', 275, 50)
        text('''and find a new wife and some teeth."''', 275, 80)
        text('"I hate my family."', 275, 125)
        text('"The coffin has to be on the bevel."', 275, 200)
        text('"Where can I find some heavy rocks?"', 275, 275)
        text('"Lafe is really good at picking cotton."', 275, 350)
        text('"Dewey Dell is SO HOT."', 275, 425)
        text('"I caught a fish for my mother."', 275, 500)
    if area==1: #New Hope Church
        text('"We have to get to town. I NEED TEETH."', 275, 50)
        text('"They put me in the coffin upside-down? I', 275, 125)
        text('never thought they were this stupid."', 275, 155)
        text('"None of them understand carpentry. The coffin', 275, 200)
        text('has to be made on the bevel."', 275, 230)
        text('"She left me all alone with them. I hate my', 275, 275)
        text('family."', 275, 305)
        text('''"How did Lafe fit a baby inside of me? I don't''', 275, 350)
        text('''understand my body."''', 275, 380)
        text('"I can teach Dewey Dell a thing or two about her', 275, 425)
        text('body."', 275, 455)
        text('"My mother is a fish."', 275, 500)
    if area==2: #Samson's
        text('"Now I can get them teeth. That will be a', 275, 50) 
        text('comfort. It will."', 275, 80)
        text('''"He's focused on getting new teeth now?''', 275, 125)
        text('''After I'm dead? Seriously??"''', 275, 155)
        text('''"Look at that coffin I built. It's perfect.''', 275, 200)
        text('''I'm the best son. I'm the best son ever."''', 275, 230)
        text('''"Good thing I have my horse. I can't wait''', 275, 275)
        text('to get out of here."', 275, 305)
        text('''"I'm going to take the knife out of that''', 275, 350)
        text('fish and kill Darl."', 275, 380)
        text('''"Oh my god, she's SO HOT."''', 275, 425)
        text('''"What's that thing circling around up there?"''', 275, 500)
    if area==3: #Tulls and Ford
        text('"If it was just up, we could drive across."', 275, 50)
        text('''"But it's not up, you moron. It would be''', 275, 125)
        text('''hilarious if Anse told them to cross."''', 275, 155)
        text('"We should probably be careful crossing this', 275, 200)
        text('river."', 275, 230)
        text('''"I need to get across this river, or I'll''', 275, 275)
        text('''never be free from these idiots."''', 275, 305)
        text('''"I need to get across this river, or I'll''', 275, 350)
        text('''never get my abortion."''', 275, 380)
        text('''"Do I look sexy when I'm soaking wet?"''', 275, 425)
        text('''"I hope Cash doesn't get hurt crossing the''', 275, 500)
        text('river."', 275, 530)
    if area==4: #Armstids
        text('"Whitfield is a kind man. He came a long way to', 275, 50)
        text('pay his respects."', 275, 80)
        text('"I hate my kids. I wish I could whip', 275, 125)
        text('them..."', 275, 155)
        text('"My tools! Where are my tools?"', 275, 200)
        text('"My horse is gone and my dream is over."', 275, 275)
        text('"I wish Darl had drowned back at the river.', 275, 350)
        text('If only, if only..."', 275, 380)
        textSize(33)
        text('"Cash needs to get over his obsession with those tools.', 275, 425) 
        text('''Just get a new hammer; it's not a big deal!"''', 275, 455)
        textSize(40)
        text('"There are seven birds following us now;', 275, 500)
        text('yesterday there were four."', 275, 530)
    if area==5: #Frenchmans bend
        text('"I just met the hottest babe. I think I got her', 275, 50)
        text('with my dazzling smile."', 275, 80)
        text('"I LOVE TO WHIP CHILDREN!"', 275, 125)
        text('--UNBORN--', 275, 200)
        text('--UNBORN--', 275, 275)
        text('--UNBORN--', 275, 350)
        text('--UNBORN--', 275, 425)
        text('--UNBORN--', 275, 500)
    if area==6: #Mottson
        text('"We never aimed to bother nobody...but people', 275, 50)
        text('sure are generous!"', 275, 80)
        text('"Sorry, everyone! I apologize for the smell. I', 275, 125)
        text('''haven't taken a bath in eight days."''', 275, 155)
        text('''"I don't want cement on my leg, but I don't want''', 275, 200)
        text('to be rude. Should I say something?"', 275, 230)
        textSize(30)
        text('''"My horse is gone. This is rock bottom. At least I'm not injured''', 275, 275)
        textSize(25)
        text('like Cash. It would be awful if I broke my leg or my skin got burned."', 275, 305)
        textSize(40)
        text('"Lafe lied to me. I should have seen that', 275, 350)
        text('coming, but he was amazing in the sack."', 275, 380)
        text('''"Yes! Dewey Dell didn't get her abortion. I'm''', 275, 425)
        textSize(30)
        text('going to torture her about it until she falls in love with me."', 275, 455)
        textSize(40)
        text('"There are ten of them now."', 275, 500)
    if area==7: #Gillespies
        text('''"I'm real sorry 'bout your barn Gillespie,''', 275, 50)
        text('think I can I borrow a few bucks?"', 275, 80)
        text('''"Darl tried to cremate me. I think it's safe to''', 275, 125)
        text('''say that he's my least favorite kid."''', 275, 155)
        text('''"I'm good. Let's just keep moving."''', 275, 200)
        text('''"I'm the only one who actually cares about''', 275, 275)
        text('my mother."', 275, 305)
        text('"Finally, Darl will be locked up and away', 275, 350)
        text('from me."', 275, 380)
        text('"Yes Yes Yes Yes."', 275, 425)
        text('''"Dewey Dell says I can't tell no one what''', 275, 500)
        text('I saw."', 275, 530)
    if area==8: #Cemetery
        text('"Now I got my new Mrs. Bundren!"', 275, 50)
        text('"Run away, new Mrs. Bundren! Run away!"', 275, 125)
        text('''"Mmmm...I'm lovin' that music..."''', 275, 200)
        text('''"I'm not going back to Yoknapatawpha with''', 275, 275)
        text('these goddamn idiots."', 275, 305)
        text('"I wish I could have landed one more punch', 275, 350)
        text('on Darl."', 275, 380)
        text('"Ha ha ha ha ha ha ha ha!"', 275, 425)
        text('"I want a toy train and bananas and a bicycle."', 275, 500)
        
def jewel_intro():
    global canwork, Jewel, setbutton, final, topwrite, wordswrite, temp1, hold, part, once, firstmini, minichoice, repeat, minichoicetemp, finalize
    fill(255)
    if once==0:
        background(0)
        text("Do you want to enter Jewel's dream?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        once+=1
    if keyPressed and key=='1' or key=='2' and not firstmini:
        text(str(key), 475, 335)
        canwork=True
        setbutton= int(key)
    if keyPressed and key==ENTER and canwork and (not firstmini):
        if setbutton==1:
            Jewel=True
        if setbutton==2:
            background(0)
            final=True
            topwrite = False
            wordswrite = False
            canwork=False
            setbutton=0
            temp1=0
            hold=0
            part=0
            minichoice=0
            firstmini=True
            once=0
            finalize=False
            minichoicetemp=0
            repeat=0
            
    if keyPressed and key==BACKSPACE and firstmini==False:
        background(0)
        canwork=False
        once=0
        minichoicetemp=0
        
def fishing_game():
    global canwork, fishing, setbutton, final, topwrite, wordswrite, temp1, hold, part, once, firstmini, minichoice, repeat, minichoicetemp, finalize
    global arman_music, arman_music_bool, intro_music, brian_model
    
    intro_sound.stop()
    
    fill(255)

    if once==0:
        background(0)
        text("Ya like fishing?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        once+=1
    if keyPressed and (key=='1' or key=='2') and not firstmini:
        text(str(key), 475, 335)
        canwork=True
        setbutton= int(key)
    if keyPressed and key==ENTER and canwork and (not firstmini):
        if setbutton==1:
            fishing=True
            if arman_music_bool==False:
                arman_music.play()
                arman_music_bool=True
        if setbutton==2:
            background(0)
            final=True
            topwrite = False
            wordswrite = False
            canwork=False
            setbutton=0
            temp1=0
            hold=0
            part=0
            minichoice=0
            firstmini=True
            once=0
            finalize=False
            minichoicetemp=0
            repeat=0
            brian_model=0
    if keyPressed and key==BACKSPACE and firstmini==False:
        background(0)
        canwork=False
        once=0
        minichoicetemp=0
        
def highway_game():
    global canwork,ready_nick , highway, setbutton, final, topwrite, wordswrite, temp1, hold, part, once, firstmini, minichoice, repeat, minichoicetemp, finalize, nick_game_temp1
    global intro_sound, brian_model,nick_music, nick_music_bool
    intro_sound.stop()
    fill(255)
    if once==0:
        background(0)
        text("Ready to drive?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        once+=1
    if keyPressed and (key=='1' or key=='2') and not firstmini:
        text(str(key), 475, 335)
        canwork=True
        setbutton= int(key)
    if keyPressed and key==ENTER and canwork and (not firstmini):
        if setbutton==1:
            highway=True
            if nick_music_bool==False:
                nick_music.play()
                nick_music_bool=True
        if setbutton==2:
            background(0)
            final=True
            topwrite = False
            wordswrite = False
            canwork=False
            setbutton=0
            temp1=0
            hold=0
            part=0
            minichoice=0
            firstmini=True
            once=0
            finalize=False
            minichoicetemp=0
            repeat=0
            brian_model=0
    if keyPressed and key==BACKSPACE and firstmini==False:
        background(0)
        canwork=False    
        once=0
        minichoicetemp=0 
        
def frogger_game():
    global canwork,ready_nick , frogger_bool, setbutton, final, topwrite, wordswrite, temp1, hold, part, once, firstmini, minichoice, repeat, minichoicetemp, finalize, nick_game_temp1
    global intro_sound, brian_model,adam_music, adam_music_bool
    intro_sound.stop()
    if once==0:
        background(0)
        text("Ready to hop the river?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        once+=1
    if keyPressed and (key=='1' or key=='2') and not firstmini:
        text(str(key), 475, 335)
        canwork=True
        setbutton= int(key)
    if keyPressed and key==ENTER and canwork and (not firstmini):
        if setbutton==1:
            frogger_bool=True
            if adam_music_bool==False:
                adam_music.play()
                adam_music_bool=True
        if setbutton==2:
            background(0)
            final=True
            topwrite = False
            wordswrite = False
            canwork=False
            setbutton=0
            temp1=0
            hold=0
            part=0
            minichoice=0
            firstmini=True
            once=0
            finalize=False
            minichoicetemp=0
            repeat=0
            brian_model=0
    if keyPressed and key==BACKSPACE and firstmini==False:
        background(0)
        canwork=False         
        once=0
        minichoicetemp=0
        
def quiz_game():
    global canwork, bundrenquiz, setbutton, final, topwrite, wordswrite, temp1, hold, part, once, firstmini, minichoice, repeat, minichoicetemp, finalize
    fill(255)
    if single_time_andrew==0:
        text("Ready for a Quiz?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
    if once==0:
        background(0)
        once+=1
    if keyPressed and (key=='1' or key=='2') and not firstmini:
        text(str(key), 475, 335)
        canwork=True
        setbutton= int(key)
    if keyPressed and key==ENTER and canwork and (not firstmini):
        if setbutton==1:
            bundrenquiz=True
        if setbutton==2:
            background(0)
            final=True
            topwrite = False
            wordswrite = False
            canwork=False
            setbutton=0
            temp1=0
            hold=0
            part=0
            minichoice=0
            firstmini=True
            once=0
            finalize=False
            minichoicetemp=0
            repeat=0
    if keyPressed and key==BACKSPACE and firstmini==False:
        background(0)
        canwork=False   

           
def minis_ingame():
    global area, frog_ingame, fish_ingame, highway_ingame, jewel_ingame, game_part, button, write, state, hold, ready_for_brian, model, juul_value, highway_value, frog_value, fish_value, single_brian, juul_once, highway_once, frog_once, fish_once, ready, keep, quiz_ingame, quiz_once, quiz_value, quiz_once_time, please_work  
    if jewel_ingame:
        fill(255)
        text("Do you want to enter Jewel's dream?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        if keyPressed and key=='1' and (not ready_for_brian):
            text('1', 475, 335)
            ready_for_brian=True
            model+=1
        elif keyPressed and key=='2' and (not ready_for_brian):
            text('2', 475, 335)
            ready_for_brian=True
            model+=2
        if keyPressed and key==ENTER and ready_for_brian:
            if model==1:
                #//ADD THE JEWEL MINIGAME HERE\\
                pass
            elif model==2 and not juul_once:
                background(0)
                game_part=0
                button =0
                write=False
                state=False
                hold=0
                juul_value=False
                single_brian=0
                juul_once=True
                jewel_ingame=False
                ready=False
                keep=0
        if keyPressed and key==BACKSPACE and ready_for_brian:
            background(0)
            model=0
            ready_for_brian=False
            
    if frog_ingame:
        fill(255)
        text("Ready to hop the river?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        if keyPressed and key=='1' and (not ready_for_brian):
            text('1', 475, 335)
            ready_for_brian=True
            model+=1
        elif keyPressed and key=='2' and (not ready_for_brian):
            text('2', 475, 335)
            ready_for_brian=True
            model+=2
        if keyPressed and key==ENTER and ready_for_brian:
            if model==1:
                #//ADD THE FROGGER MINIGAME HERE\\
                pass
            elif model==2 and not frog_once:
                background(0)
                game_part=0
                button =0
                write=False
                state=False
                hold=0
                frog_value=False
                single_brian=0
                frog_once=True
                frog_ingame=False
                ready=False
                keep=0
        if keyPressed and key==BACKSPACE and ready_for_brian:
            background(0)
            model=0
            ready_for_brian=False
            
    if fish_ingame:
        fill(255)
        text("Ya like fishing?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        if keyPressed and key=='1' and (not ready_for_brian):
            text('1', 475, 335)
            ready_for_brian=True
            model+=1
        elif keyPressed and key=='2' and (not ready_for_brian):
            text('2', 475, 335)
            ready_for_brian=True
            model+=2
        if keyPressed and key==ENTER and ready_for_brian:
            if model==1:
                #//ADD THE FISHING MINIGAME HERE\\
                pass
            elif model==2 and not fish_once:
                background(0)
                game_part=0
                button =0
                write=False
                state=False
                hold=0
                fish_value=False
                single_brian=0
                fish_once=True
                fish_ingame=False
                ready=False
                keep=0
        if keyPressed and key==BACKSPACE and ready_for_brian:
            background(0)
            model=0
            ready_for_brian=False
            
    if highway_ingame:
        fill(255)
        text("Wanna drive?", 100, 200)
        text('1. Yes', 150, 240)
        text('2. No', 150, 280)
        text('What is your choice?', 100, 335)
        if keyPressed and key=='1' and (not ready_for_brian):
            text('1', 475, 335)
            ready_for_brian=True
            model+=1
        elif keyPressed and key=='2' and (not ready_for_brian):
            text('2', 475, 335)
            ready_for_brian=True
            model+=2
        if keyPressed and key==ENTER and ready_for_brian:
            if model==1:
                #//ADD THE HIGHWAY STAR MINIGAME HERE\\
                pass
            elif model==2 and not highway_once:
                background(0)
                game_part=0
                button =0
                write=False
                state=False
                hold=0
                highway_value=False
                single_brian=0
                highway_once=True
                highway_ingame=False
                ready=False
                keep=0
        if keyPressed and key==BACKSPACE and ready_for_brian:
            background(0)
            model=0
            ready_for_brian=False
    if quiz_ingame:
        fill(255)
        if please_work == 0:
            text("Ready for a test?", 100, 200)
            text('1. Yes', 150, 240)
            text('2. No', 150, 280)
            text('What is your choice?', 100, 335)
            please_work+=1
        if keyPressed and key=='1' and (not ready_for_brian):
            text('1', 475, 335)
            ready_for_brian=True
            model+=1
        elif keyPressed and key=='2' and (not ready_for_brian):
            text('2', 475, 335)
            ready_for_brian=True
            model+=2
        if keyPressed and key==ENTER and ready_for_brian:
            if model==1:
                if quiz_once_time==0:
                    background(0)
                    frame.setSize(1150,600)
                    quiz_once_time+=1
                #ADD THE GAME FUNCTION
            elif model==2 and not quiz_once:
                background(0)
                game_part=0
                button =0
                write=False
                state=False
                hold=0
                quiz_value=False
                single_brian=0
                quiz_once=True
                quiz_ingame=False
                ready=False
                keep=0
        if keyPressed and key==BACKSPACE and ready_for_brian:
            background(0)
            model=0
            ready_for_brian=False

def aarons_game():
    global w_a,w_x,w_y,w_c,w_z,w_hitcountCASH,w_throws,w_g,w_h,w_hitcountVARDAMAN,w_r,w_u,w_hitcountdDELL,w_q,w_b,w_hitcountANSE, topwrite, wordswrite, temp1, hold, part, repeat, minichoice, minichoicetemp, finalize, firstmini, jewel_dream_sound, juul_one_sound, intro_sound
    global setbutton
    frameRate(60)
    if juul_one_sound==False:
        intro_sound.stop()
        jewel_dream_sound.play()
        juul_one_sound=True
    imageMode(CENTER)
    if millis()/1000 <= 5:
        background(0)
        fill(255)
        textSize(40)
        text("Press the left arrow key to throw the rock.", 100,200)
        text("Game starts in...." + " " + str(5 - (millis()/1000)),100,300)
    else:
        hill()
        controls()
        jewel()
        addie()
        rock()
        if w_hitcountCASH == 0:
            cash()
            if (95+w_c)<=(910 - w_x)<=(105+w_c) and 470<=(250+w_y)<=490:
                w_hitcountCASH += 1
        if w_hitcountVARDAMAN == 0:
            vardaman()
            if (45+w_h)<=(910 - w_x)<=(55+w_h) and 470<=(250+w_y)<=490:
                w_hitcountVARDAMAN += 1
        if w_hitcountdDELL == 0:
            dDell()
            if (145+w_u)<=(910 - w_x)<=(155+w_u) and 470<=(250+w_y)<=490:
                w_hitcountdDELL += 1
        if w_hitcountANSE == 0:
            anse()
            if (195+w_b)<=(910 - w_x)<=(205+w_b) and 470<=(250+w_y)<=490:
                w_hitcountANSE += 1
    
        w_t = millis()/1000
        fill(255)
        textSize(60)
        #text("Time:" + str(w_t-5), 700,100)
        text("Hit count:" + str(w_hitcountCASH+w_hitcountVARDAMAN + w_hitcountdDELL + w_hitcountANSE), 150,100)
        text("Throws:" + str(w_throws), 150,200)
        global once, Jewel, canwork, final, setbutton
        if (w_hitcountCASH + w_hitcountVARDAMAN + w_hitcountdDELL + w_hitcountANSE) == 4:
            background(0)
            fill(255,0,0)
            textSize(60)
            text("You win, Addie is all yours!!!", 100,250)
            textSize(40)
            text("You hit 4 people in" + " "+ str(w_throws) + " throws!!!",100,350)
            textAlign(CENTER)
            text('Press Space to go back', width/2, height/2+275)
            if keyPressed and key==' ':
                background(0)
                
                once=0
                Jewel=False
                canwork=False
                final=True
                setbutton=0
                
                topwrite = False
                wordswrite = False
                temp1=0
                hold=0
                part=0
                repeat=0
                minichoice=0
                w_a = 0
                w_x = 0
                w_y = 0
                w_c = 0
                w_z = 0
                w_t = 0
                w_i = 0
                w_o = 0
                w_g = 0
                w_h = 0
                w_r = 0
                w_u = 0
                w_q = 0
                w_b = 0
                w_hitcountCASH = 0
                w_hitcountVARDAMAN = 0
                w_hitcountdDELL = 0
                w_hitcountANSE = 0
                w_throws = 0
                w_temp = False
                finalize=False
                minichoicetemp=0
                firstmini=True
                if juul_one_sound==True:
                    intro_sound.play()
                    jewel_dream_sound.stop()
                    juul_one_sound=False
                setbutton=0
                
            textAlign(LEFT)
        
def hill():
    background(0,255,245)
    fill(0,255,100)
    rect(0,500,1020,650)
    triangle(350,600,1250,175,1250,650)
    rect(850,275,200,200)
    bezier(0,650,350,500,1250,-175,1250,750)
    noStroke()

def controls():
    global w_a, w_x,w_y, w_t, w_temp, w_throws
    if keyPressed:
        if key == CODED and keyCode == LEFT:
            w_a -=5
def jewel():
    global w_a,w_x, w_y , w_t, w_temp, w_throws,w_JUULimg
    fill(255,0,0)
    ellipse(900,255,10,20)
    rect(897,258,2,15)
    rect(901,258,2,15)
    image(w_JUULimg, 900, 243)
    #ellipse(900,243,7,7)
    rect(900,253,-12,2)
    pushMatrix()
    translate(900,253)
    if w_temp==True and w_y<250:
        w_t += .015
        w_x += 5
        w_y += (w_t**2)
        rotate(radians(-60))
    rect(0,0,12,2)
    popMatrix()
    
def rock():
    global w_x, w_y , w_t, w_temp, w_throws
    pushMatrix()
    if keyPressed and key==' ' and w_temp==False:
        w_temp=True
        w_throws += 1 
    if w_temp==True and w_y<250:
                 w_t +=.015
                 w_x += 5
                 w_y += (w_t**2)
    else:
        
        w_temp = False
        w_t = 0
        w_x = 0
        w_y = 0
    fill(0)
    ellipse(910 - w_x,250 + w_y,6,6)
    popMatrix()
    
def addie():
    global w_ADDIEimg
    fill(255,200,0)
    ellipse(940,258,8,17)
    rect(937,260,2,13)
    rect(941,260,2,13)
    rect(930,256,20,2)
    image(w_ADDIEimg, 940, 247)
    
def cash():
    global w_a,w_x,w_y,w_z,w_c,w_e,w_CASHimg
    fill(255,150,0)
    if w_z%2!=0:
        if w_c < 190:
            w_c +=1
        else:
            w_z+=1
    elif w_z%2==0:
        if w_c >-75:
            w_c -=1
        else:    
            w_z+=1
    ellipse(100+w_c,480,10,20)
    rect(97+w_c,487,2,13)
    rect(101+w_c,487,2,13)
    image(w_CASHimg, 100+w_c, 468)
    rect(90+w_c,478,20,2)
    
def vardaman():
    global w_a,w_x,w_y,w_g,w_h,w_e,w_VARDAMANimg
    fill(255,255,255)
    if w_g%2==0:
        if w_h < 240:
            w_h +=1
        else:
            w_g+=1
    elif w_g%2!=0:
        if w_h >-25:
            w_h -=1
        else:    
            w_g+=1
    ellipse(50+w_h,480,10,20)
    rect(47+w_h,487,2,13)
    rect(51+w_h,487,2,13)
    image(w_VARDAMANimg, 50+w_h, 468)
    rect(40+w_h,478,20,2)
    
def dDell():
    global w_a,w_x,y,w_r,w_u,w_e,w_dDELLimg
    fill(255,150,200)
    if w_r%2!=0:
        if w_u < 140:
            w_u +=1
        else:
            w_r+=1
    elif w_r%2==0:
        if w_u >-125:
            w_u -=1
        else:    
            w_r+=1
    ellipse(150+w_u,480,10,20)
    rect(147+w_u,487,2,13)
    rect(151+w_u,487,2,13)
    image(w_dDELLimg, 150+w_u, 468)
    rect(140+w_u,478,20,2)
    
def anse():
    global w_a,w_x,w_y,w_q,w_b,w_e,w_ANSEimg
    fill(0,0,0)
    if w_q%2==0:
        if w_b < 90:
            w_b +=1
        else:
            w_q+=1
    elif w_q%2!=0:
        if w_b >-175:
            w_b -=1
        else:    
            w_q+=1
    ellipse(200+w_b,480,10,20)
    rect(197+w_b,487,2,13)
    rect(201+w_b,487,2,13)
    image(w_ANSEimg, 200+w_b, 468)
    rect(190+w_b,478,20,2)

def armans_game_full(): #THE Velocity of the ball is 4.5, but it is reasonable considering how hard this game is it is good.
    
    frameRate(60)
    #background(0,0,200)
    global arman_time, whiteball, whiteballX, whiteballY, blueballX, blueballY, whitenum, blueballRadius, arman_temp_value,riverPic
    image(riverPic,0,0)
    image(riverPic,0,348)
        
    if arman_temp_value==False:
        text("Time:", 600,550)# Displays the time at the bottom right so that the user knows their score
        text(int(arman_time), 750, 550)
        if (keyPressed) and (key == CODED) and (keyCode == UP):
            blueballY -= 4.5
        if (keyPressed) and (key == CODED) and (keyCode == DOWN):
            blueballY += 4.5
        if (keyPressed) and (key == CODED) and (keyCode == LEFT):
            blueballX -= 4.5
        if (keyPressed) and (key == CODED) and (keyCode == RIGHT):
            blueballX += 4.5
        fill(0, 0, 255)
        for i in range(0, whitenum - 1):
            image(arman_img,whiteballX[i], whiteballY[i])
        image(arman_img2, blueballX, blueballY)
        
        arman_time += 0.02
        whiteball += 0.02
        if (whiteball >= 5):
            whiteball = 0
            whiteballX.append(random.randint(30, width-30 ))
            whiteballY.append(random.randrange(30, height-30))
            whitenum += 1
        fill(255)
        
        for i in range(0, whitenum - 1):
            if (blueballX - whiteballX[i])**2 + (blueballY - whiteballY[i])**2 < (blueballRadius + 15)**2:
                whitenum -= 1
                a = whiteballX.pop(i)
                b = whiteballY.pop(i)
    global arman_music, arman_music_bool, brian_model            
    if whitenum == 1:
        arman_temp_value = True

        background(0)
        fill(0, 0, 250)
        #ellipse(blueballX, blueballY, blueballRadius*1.5, blueballRadius*1.5)
        fill(255)
        textSize(100)
        textAlign(CENTER, CENTER)
        text("Time:", 450, 400)
        text(int(arman_time), 650, 400)
        text("Cooked it up and et it!", 500, 200)
        global topwrite, setbutton,wordswrite,once, temp1, hold, part, repeat, minichoice, fishing,finalize, minichoicetemp, firstmini
        textSize(40)
        text('Press Space to go back', width/2, height/2+275)
        if keyPressed and key==' ':
            background(0)
            setbutton=0
            fishing=False
            topwrite = False
            wordswrite = False
            temp1=0
            hold=0
            part=0
            repeat=0
            minichoice=0
            finalize=False
            minichoicetemp=0
            firstmini=True
            whitenum=5
            arman_time=0
            whiteball = 0
            once=0
            img_fish = whitenum
            blueballX = 400
            blueballY = 300
            blueballRadius = 20 #the smaller the ball, the harder the game. In my opinion at least
            for i in range(0, whitenum):
                whiteballX.append(random.randrange(30, width-30))
                whiteballY.append(random.randrange(30, height-30))
            arman_temp_value=False
            brian_model=0
            arman_music.stop()
            arman_music_bool=False
def coffin(xtopcorner, ytopcorner): #Addie's coffin
    noStroke()
    fill(220, 126, 0)
    rect(xtopcorner - 10, ytopcorner, 220, 100)
    triangle(xtopcorner - 10, ytopcorner, xtopcorner + 65, ytopcorner - 15, xtopcorner + 210, ytopcorner)
    triangle(xtopcorner - 10, ytopcorner + 100, xtopcorner + 65, ytopcorner + 115, xtopcorner + 210, ytopcorner + 100)
    stroke(255, 126, 0) #worn edges
    line(xtopcorner - 10, ytopcorner, xtopcorner - 10, ytopcorner + 100)
    line(xtopcorner - 10, ytopcorner, xtopcorner + 65, ytopcorner - 15)
    line(xtopcorner + 65, ytopcorner - 15, xtopcorner + 210, ytopcorner)
    line(xtopcorner + 210, ytopcorner, xtopcorner + 210, ytopcorner + 100)
    line(xtopcorner - 10, ytopcorner + 100, xtopcorner + 65, ytopcorner + 115)
    line(xtopcorner + 65, ytopcorner + 115, xtopcorner + 210, ytopcorner + 100)
    noStroke()
    fill(0)
    for i in range(xtopcorner - 5, xtopcorner + 160, 5): #holes in the coffin that are not in Addie's head
        ellipse(i, random.randrange(ytopcorner + 5, ytopcorner + 95), 5, 5)
    for i in range(xtopcorner + 190, xtopcorner + 210, 10): #holes in Addie's head
        ellipse(i, random.randrange(ytopcorner + 35, ytopcorner + 65), 5, 5)

def KnowYourBundrens():
    global xy_coordinates, Cards, selected_xy_coordinate_indexnumber, selected_xy_coordinate, n, b, c, Cards2, allowloop, time, fire, tries, Bundrensbegin, ending
    if Bundrensbegin == 0:
        xy_coordinates = [(100, 150), (350, 150), (600, 150), (850, 150), (100, 300), (350, 300), (600, 300), (850, 300), (100, 450), (350, 450), (600, 450), (850, 450)]
        Cards = [(1, "Anse", "Anse", "Anse"), (2, "But now I can get them teeth. That will be a comfort. It will.", "I reckon we can get a spade...I reckon there are Christians here.", "Eight miles of sweat  of his body washed up outen the Lord's      Earth..."), (3, "Cash", "Cash", "Cash"), (4, "8. Animal magnetism.", "It was one of those gramphones. It was as natural as a music-band.", "It wasn't on a balance. I told them     that if they wanted it to tote and ride on a balance, they would have to"), (5, "Darl", "Darl", "Darl"), (6, "...I could lie with my shirt-tail up,   [...] feeling myself without touching   myself, feeling the cool silence blowing upon my parts...", "I cannot love my      mother because I have no mother. Jewel's    mother is a horse.", "Why not leave your    cakes here? [...]     We'll  watch them."), (7, "Jewel", "Jewel", "Jewel"), (8, "It would just be me and her on a high   hill and me rolling the rocks down the  hill at their faces...", "Kill him. Kill the son of a bitch.", "One less lick and we  could be quiet."), (9, "Dewey Dell", "Dewey Dell", "Dewey Dell"), (10, "We picked on down the row, the woods getting closer and closer and the secret   shade with my sack and Lafe's sack.", "I wish I had time to  let her die. I wish I had time to wish I    had.", "Mrs. Tull's cakes...  I'm taking them to    town for her."), (11, "Vardaman", "Vardaman", "Vardaman"), (12, "My mother is a fish.", "The track went shining around the window, it red on the track.", "I can cry quiet now,   feeling and hearing  my tears.")]
        b = 24 #see one line below
        c = 0 #serve as index counters when the quotes are picked out for each character

        while b > 12: #randomizes the quotes as well as their locations on the screen
            selected_xy_coordinate_listindice = random.randrange(0, (b - 12))
            selected_xy_coordinate = xy_coordinates[selected_xy_coordinate_listindice]
            del xy_coordinates[selected_xy_coordinate_listindice]
            Cards[c] = (Cards[c][0], Cards[c][random.randrange(1, 4)], selected_xy_coordinate[0], selected_xy_coordinate[1])
            b = b - 1
            c = c + 1
        Cards2 = []
        for i in range(0, len(Cards)):
            Cards2.append(Cards[i]) #serves as memory for tracking the panels that have been matched
        n = 0 #seves as memory for the first panel selected in a pair
        allowloop = True #boolean variable that makes sure the function draw only loops for one time when the mouse is clicked
        time = millis()
        fire = []
        tries = 3 #number of mistakes the player is allowed before game over
        ending = 0
        textAlign(CENTER)
        background(0, 0, 255) #blue background
        fill(255)
        textSize(30)
        text("Do You Know Your Bundrens?", width/2, 75)
        textSize(15)
        fill(0)
        text("Click on a character's panel and match it with their corresponding quote." , 300, 25)
        textSize(30)
        fill(0, 255, 0)
        noStroke()
        rect(0, height - 20, 1150, 20) #grass
        fill(125, 125, 125)
        rect(100, 150, 200, 100) 
        rect(350, 150, 200, 100) 
        rect(600, 150, 200, 100) 
        rect(850, 150, 200, 100) 
        rect(100, 300, 200, 100) 
        rect(350, 300, 200, 100) 
        rect(600, 300, 200, 100)
        rect(850, 300, 200, 100)
        rect(100, 450, 200, 100) 
        rect(350, 450, 200, 100) 
        rect(600, 450, 200, 100) 
        rect(850, 450, 200, 100) #matching panels
        for i in range(0, len(Cards)): #loop that draws the text in the matching boxes on the screen (both quotes and names)
            if Cards[i][0] % 2 == 0:
                fill(0)
                textSize(15)
            
                if len(Cards[i][1]) > 100:
                    textSize(9)
                    text(Cards[i][1][0:40], Cards[i][2] + 100, Cards[i][3] + 30)
                    text(Cards[i][1][40:80], Cards[i][2] + 100, Cards[i][3] + 45)
                    text(Cards[i][1][80:120], Cards[i][2] + 100, Cards[i][3] + 60)
                    text(Cards[i][1][120:160], Cards[i][2] + 100, Cards[i][3] + 75)
                    text(Cards[i][1][160:200], Cards[i][2] + 100, Cards[i][3] + 75)
                    text(Cards[i][1][200:], Cards[i][2] + 100, Cards[i][3] + 75)
                elif len(Cards[i][1]) > 88 and len(Cards[i][1]) < 100:
                    text(Cards[i][1][0:22], Cards[i][2] + 100, Cards[i][3] + 30)
                    text(Cards[i][1][22:44], Cards[i][2] + 100, Cards[i][3] + 45)
                    text(Cards[i][1][44:66], Cards[i][2] + 100, Cards[i][3] + 60)
                    text(Cards[i][1][66:88], Cards[i][2] + 100, Cards[i][3] + 75)
                    text(Cards[i][1][88:100], Cards[i][2] + 100, Cards[i][3] + 90)
                elif len(Cards[i][1]) == 66:
                    textSize(10)
                    text(Cards[i][1][0:32], Cards[i][2] + 100, Cards[i][3] + 30)
                    text(Cards[i][1][32:], Cards[i][2] + 100, Cards[i][3] + 45)
                elif len(Cards[i][1]) > 66 and len(Cards[i][1]) < 89:
                    text(Cards[i][1][0:22], Cards[i][2] + 100, Cards[i][3] + 30)
                    text(Cards[i][1][22:44], Cards[i][2] + 100, Cards[i][3] + 45)
                    text(Cards[i][1][44:66], Cards[i][2] + 100, Cards[i][3] + 60)
                    text(Cards[i][1][66:], Cards[i][2] + 100, Cards[i][3] + 75)
                elif len(Cards[i][1]) > 44 and len(Cards[i][1]) < 67:
                    text(Cards[i][1][0:22], Cards[i][2] + 100, Cards[i][3] + 30)
                    text(Cards[i][1][22:44], Cards[i][2] + 100, Cards[i][3] + 45)
                    text(Cards[i][1][44:], Cards[i][2] + 100, Cards[i][3] + 60)
                elif len(Cards[i][1]) > 22 and len(Cards[i][1]) < 45:
                    text(Cards[i][1][0:22], Cards[i][2] + 100, Cards[i][3] + 30)
                    text(Cards[i][1][22:], Cards[i][2] + 100, Cards[i][3] + 45)
                elif len(Cards[i][1]) < 23:
                    text(Cards[i][1], Cards[i][2] + 100, Cards[i][3] + 50) #one line in each panel will have no more than 22 characters 
            
            elif Cards[i][0] % 2 != 0:
                fill(255)
                textSize(30) #names are drawn larger than quotes since they are less characters
                text(Cards[i][1], Cards[i][2] + 100, Cards[i][3] + 50)
            
            
            
    if Bundrensbegin == 1:
        if mousePressed == True and allowloop == True:
            for i in range(0, len(Cards)):
                if mouseX > Cards[i][2] and mouseX < Cards[i][2] + 200 and mouseY > Cards[i][3] and mouseY < Cards[i][3] + 100 and Cards2.count(Cards[i]) < 2:
                    if n == 0 and allowloop == True:
                        fill(255)
                        n = Cards[i]
                        rect(n[2], n[3] - 20, 200, 20) #white box will appear over the panel that is clicked
                        allowloop = False
                    if n != 0 and allowloop == True:
                        fill(0, 0, 255)
                        rect(n[2], n[3] - 20, 200, 20) #white box of the panel previously selected disappears
                        if n[0] % 2 == 0: #if identification number of the second selected panel is even
                            if Cards[i][0] == n[0] - 1: #if the cards match, then replace them with coffins on the screen
                                Cards2.append(Cards[i]) 
                                fill(190, 90, 0)
                                coffin(Cards[i][2], Cards[i][3])
                                Cards2.append(n)
                                coffin(n[2], n[3])
                                fill(255)
                            if Cards[i][0] != n[0] - 1 and Cards[i][0] != n[0]:
                                tries = tries - 1

                        else: #if the identification number of the second selected panel is odd
                            if Cards[i][0] == n[0] + 1: #if the cards match, then replace them with coffins on the scree
                                Cards2.append(Cards[i])
                                fill(190, 90, 0)
                                coffin(Cards[i][2], Cards[i][3])
                                Cards2.append(n)
                                coffin(n[2], n[3])
                                fill(255)
                            if Cards[i][0] != n[0] + 1 and Cards[i][0] != n[0]:
                                tries = tries - 1
                        n = 0 #allow for a new pair of panels to be clicked
                        allowloop = False
                    
    
        elif mousePressed == False:
            allowloop = True
        fill(0, 0, 255)
        rect(width - 200, 0, 200, 100)
        textSize(30)
        fill(255, 0, 0)
        text("Mistakes allowed: " + str(tries), width - 180, 55)
        if len(Cards2) == 2 * len(Cards): #if all the panels have been matched
            background(255, 0, 0)
            fill(252, 126, 0)
            if millis() - time > 100:
                fire = []
                for i in range(0, 1150, 50):
                    fire.append((i, height, i + random.randrange(5, 45), height - random.randrange(150, 600), i + random.randrange(30, 70), height))

                time = millis()
                
            for i in range(0, len(fire)): #if the player wins
                triangle(fire[i][0], fire[i][1], fire[i][2], fire[i][3], fire[i][4], fire[i][5])
            fill(255)
            textSize(30)
            text("Do You Know Your Bundrens?", width/2, 75)
            textSize(60)
            text("Now you know as much as Darl!", width/2, height/2)
        if tries == 0: #if the player loses
            Cards = []
            background(0, 0, 255)
            textMode(CENTER)
            fill(255)
            textSize(30)
            text("Do You Know Your Bundrens?", width/2, 75)
            fill(0)
            textSize(40)
            text("Game over! Looks like Shmoop failed you this time...", width/2, height/2)
        
    if Bundrensbegin == 0:
        Bundrensbegin = Bundrensbegin + 1

def cashDraw():
    noCursor()
    frameRate(30)
    global CASHframe, time, CASHgameStart, CASHcrashed, menudelay, CASHgoal, CASHvictory, CASHrobMode, topwrite,once, wordswrite, temp1, hold, part, repeat, minichoice, finalize, minichoicetemp, firstmini, highway, canwork, final, setbutton, single_time_nick   
    global CASHspeed, CASHgoal, CASHframe, CASHgameStart, CASHcrashed, CASHrobMode, CASHvictory
    global CASHbumpX, CASHbumpY, CASHsprBump
    global CASHplayerpos, CASHsprL, CASHsprR, CASHsprN, CASHplayerimg, CASHlives, CASHlifedown
    global brian_model, nick_music, nick_music_bool
    
    if not CASHcrashed:
        CASHframe += 1
        if CASHgameStart:
            time = CASHframe / 30.0
            if not CASHrobMode:
                CASHgoal = 60 - time
            else:
                CASHgoal = 120 - time
            cashBumpStep()
        else:
            time = 0
        
        cashPlayerStep()
        cashRenderStep()
        cashCrashStep()
        CASHspeedStep()
        
        if CASHgoal < 0:
            CASHvictory = True
            CASHspeed = 0.1
            cashRenderStep()
            textAlign(CENTER, BOTTOM)
            textFont(CASHfont, 36)
            fill(255)
            text("WINNER", width / 2, height / 2)
            global CASHlives 
            CASHlives = 0
    else:
        if keyPressed and key==' ':
            background(0)
            topwrite = False
            wordswrite = False
            temp1=0
            hold=0
            part=0
            repeat=0
            minichoice=0
            finalize=False
            minichoicetemp=0
            firstmini=True      
            once=0
            highway=False
            frame.setSize(1020,650)
            canwork=False
            final=True
            setbutton=0
            single_time_nick=0
            
            CASHcrashed = False
            CASHgameStart = False
            CASHframe = 0
            CASHspeed = 0
            CASHgoal = 45
            CASHrobMode = False
            CASHvictory = True

            CASHbumpX = [0, 0, 0]
            CASHbumpY = 490

            CASHplayerpos = [320, 420]

            CASHplayerimg = CASHsprN
            CASHlives = 3
            CASHlifedown = False
            brian_model=0
            nick_music.stop()
            nick_music_bool=False

    '''else:
        if (keyPressed and key == ' '):
            setup()'''


def cashRenderStep():
    imageMode(CORNER)
    image(CASHbg, 0, 0)
    image(CASHroad, 0, 0)
    imageMode(CENTER)
    image(CASHsprBump, CASHbumpX[0], CASHbumpY)
    image(CASHsprBump, CASHbumpX[1], CASHbumpY)
    image(CASHsprBump, CASHbumpX[2], CASHbumpY)
    image(CASHplayerimg, CASHplayerpos[0], CASHplayerpos[1])

    # RENDERING START PROMPT
    imageMode(CENTER)
    global CASHspeed, CASHfont
    if not CASHspeed:
        textAlign(CENTER, BOTTOM)
        textFont(CASHfont, 36)
        fill(255)
        text("Avoid the bumps or Cash will be hurt!", width / 2, 65)
        textFont(CASHfont, 24)
        text(
            "Use A/D or Left/Right Arrows to steer, Space to start", width / 2, 90)
    else:
        global CASHlives, CASHgoal
        textAlign(LEFT, TOP)
        textFont(CASHfont, 20)
        fill(255)
        text("CASH: " + str(int(CASHlives)), 5, 0)
        text("DISTANCE: " + str(int(CASHgoal)), 5, 18)

def CASHspeedStep():
    global CASHspeed, CASHframe, CASHgameStart

    if CASHspeed == 0:
        if ((keyPressed) and (key == ' ')):
            CASHspeed = 30
            CASHgameStart = True
            CASHframe = 0

def cashPlayerStep():

    global CASHplayerpos, CASHsprL, CASHsprR, CASHsprN, CASHplayerimg, CASHspeed, CASHrobMode
    distance = CASHspeed / 3

    if (keyPressed) and CASHspeed:
        if (keyPressed and (key == 'r' or key == 'R') and not CASHrobMode):
            CASHspeed *= 1.75
            global CASHbg, CASHlives, CASHbg2
            CASHbg = CASHbg2
            CASHlives = 1
            CASHrobMode = True
        if((key == 'a' or key == 'A') or (key == CODED and keyCode == LEFT)) and CASHplayerpos[0] - distance >= 100:
            CASHplayerpos[0] -= distance
        elif((key == 'd' or key == 'D') or (key == CODED and keyCode == RIGHT))and CASHplayerpos[0] + distance <= 540:
            CASHplayerpos[0] += distance
    else:
        CASHplayerimg = CASHsprN

def cashBumpStep():
    lane = [96, 208, 320, 432, 544]
    global CASHbumpX, CASHbumpY, CASHspeed

    CASHbumpY += CASHspeed / 6
    if CASHbumpY > 490:
        CASHbumpY = 260
        CASHbumpX[0] = lane[int(random.randint(0,4))]
        CASHbumpX[1] = lane[int(random.randint(0,4))]
        CASHbumpX[2] = lane[int(random.randint(0,4))]

        while (CASHbumpX[0] == CASHbumpX[1] or CASHbumpX[0] == CASHbumpX[2]) or (CASHbumpX[1] == CASHbumpX[2]):
            CASHbumpX[0] = lane[int(random.randint(0,4))]
            CASHbumpX[1] = lane[int(random.randint(0,4))]
            CASHbumpX[2] = lane[int(random.randint(0,4))]

def cashCrashStep():
    global CASHplayerpos, CASHbumpX, CASHbumpY, CASHplayerimg, CASHlives, CASHlifedown, CASHframe, CASHcrashed, once, CASHbg
    
    xcrash = 70
    ycrash = 5

    playerYcrash = CASHplayerpos[1] + 25

    # This is spaghetti code but it works ok
    if ((abs(CASHplayerpos[0] - CASHbumpX[0]) < xcrash) and (abs(playerYcrash - CASHbumpY) < ycrash)) or ((abs(CASHplayerpos[0] - CASHbumpX[1]) < xcrash) and (abs(playerYcrash - CASHbumpY) < ycrash)) or ((abs(CASHplayerpos[0] - CASHbumpX[2]) < xcrash) and (abs(playerYcrash - CASHbumpY) < ycrash)):
        CASHlifedown = True
    else:
        if CASHlifedown:
            CASHlives -= 1
        CASHlifedown = False
        
    #global topwrite, temp1, hold, part, repeat, minichoice,finalize,minichoicetemp,firstmini
    if CASHlives <= 0:
        cashRenderStep()
        textAlign(CENTER, BOTTOM)
        textFont(CASHfont, 36)
        fill(255)
        text("Cash is in pain!", width / 2, height / 2)
        text('Press Space to go back', width/2, height/2+50)
        CASHcrashed = True

        global topwrite, wordswrite, temp1, hold, part, repeat, minichoice, finalize, minichoicetemp, firstmini, highway, orig
        if keyPressed and key==' ':
            background(0)
            topwrite = False
            wordswrite = False
            temp1=0
            hold=0
            part=0
            repeat=0
            minichoice=0
            finalize=False
            minichoicetemp=0
            firstmini=True      
            once=0
            highway=False
            frame.setSize(1020,650)
            CASHrobMode=False
            CASHbg = orig

def game():
    global logPos, gameRun
    if gameRun == 0:
        for i in range(25):
            logs()
            (logPos[i][0]) -= 40*i
        for i in range(len(logPos)):
            fill(200,100,50)
            rect((logPos[i][0]),((logPos[i][1])+2),logPos[i][2], 25)
        #for i in range(11):
            #speed.append((random.randrange(1))/10)

        gameRun = 2
        
    if gameRun == 1:
        fill(0)
        rect(0,((height/5)+50),width,248)
        if keyPressed and key == " ":
            gameRun = 2
            
    for i in range(len(logPos)):
        if (p1X < (logPos[i][0] + logPos[i][2]) and (p1X + 20 > logPos [i][0])):
            if (p1Y > logPos[i][1]) and (p1Y < (logPos[i][1] + 25)) :
                gameRun = 3
            
    if p1Y <= 100:
        gameRun = 4
    if gameRun == 4:
        pass

def p1():
    global p1X, p1Y, p1Pic
    fill(255,0,0)
    #rect(p1X,p1Y,14,23)
    image(p1Pic,p1X,p1Y,17,25)
    

def logs():
    global logPos
    logPos.append([1019,((random.randrange(0,11)*29)+(height/5)),((random.randrange(2,5))*50)])
    
def logs1():
    global logPos
    logPos.append([1019,((random.randrange(0,11)*29)+(height/5)),((random.randrange(2,5))*50)])
    
def logs2():
    global logPos
    logPos.append([1019,((random.randrange(0,11)*29)+(height/5)),((random.randrange(2,5))*50)])

def river():
    global riverPic
    fill(50,50,200)
    noStroke()
    #rect(0,(height/5)-1,width,348)
    image(riverPic,0,(height/5)-1,width,348) 
      
def move():
    global p1X,p1Y,raaab
    if gameRun == 2:
        if keyPressed:
            if key == CODED and keyCode == UP:
                if p1Y <= 29:
                    pass
                else:
                    p1Y -= 29
            elif key == CODED and keyCode == DOWN:
                if p1Y >= height-29:
                    pass
                else:
                    p1Y += 29
            elif key == CODED and keyCode == LEFT:
                if p1X <= 29:
                    pass
                else:
                    p1X -= 29
            elif key == CODED and keyCode == RIGHT:   
                if p1X >= width-29:
                    pass
                else:
                    p1X += 29
            elif key == "r":
                raaab = 30

def frogger_game_full():
    global p1X, p1Y, moveUp, moveDown, moveLeft, moveRight, logMake, logPos, t, t1, t2, gameRun, logPic1, logPic2, logPic3, dirtPic, raaab
    textAlign(CENTER)
    frameRate(60)
    #background(255)
    image(dirtPic,0,0)
    game()   
    river()
    if t2 < 5:
        t2 += 1
    else:
        move()
        t2 = 0
    #for i in range(len(logPos)):
    if gameRun == 2:
        for i in range(len(logPos)):
            if raaab < 60:
                if ((logPos[i][1]) == 159) or ((logPos[i][1]) == 391) or ((logPos[i][1]) == 130) or ((logPos[i][1]) == 420): 
                    logPos[i][0] -= 2
                if ((logPos[i][1]) == 217) or ((logPos[i][1]) == 333) or ((logPos[i][1]) == 188) or ((logPos[i][1]) == 362):
                    logPos[i][0] -= 4
                if ((logPos[i][1]) == 275) or ((logPos[i][1]) == 246) or ((logPos[i][1]) == 304):
                    logPos[i][0] -= 6
            else:
                if ((logPos[i][1]) == 159) or ((logPos[i][1]) == 391) or ((logPos[i][1]) == 130) or ((logPos[i][1]) == 420):
                    logPos[i][0] -= 1
                if ((logPos[i][1]) == 217) or ((logPos[i][1]) == 333) or ((logPos[i][1]) == 188) or ((logPos[i][1]) == 362):
                    logPos[i][0] -= 2
                if ((logPos[i][1]) == 275) or ((logPos[i][1]) == 246) or ((logPos[i][1]) == 304):
                    logPos[i][0] -= 3
            #130, 159, 188, 217, 246, 275, 304, 333, 362, 391, 420
            
        if t < raaab:
            t += 1
        else:
            logs()
            logs1()
            t = 0
        
        if t1 < raaab-20:
            t1 += 1
        else:
            logs2()
            t1 = 0
    
    for i in range(len(logPos)):
        fill(200,100,50)      
        #rect((logPos[i][0]),((logPos[i][1])+2),logPos[i][2], 25)
        if logPos[i][2] == 100:
            image(logPic1,(logPos[i][0]),((logPos[i][1])+2),logPos[i][2], 25)
        elif logPos[i][2] == 150:
            image(logPic2,(logPos[i][0]),((logPos[i][1])+2),logPos[i][2], 25)
        elif logPos[i][2] == 200:
            image(logPic3,(logPos[i][0]),((logPos[i][1])+2),logPos[i][2], 25)
    
    p1()
    if gameRun == 1:
        fill(0)
        rect(0,((height/5)+50),width,248)
        fill(255)
        textSize(100)
        text("Press Space",220,(height/5)+150)
        text("To Begin",290,(height/5)+250)
    global wordswrite, temp1, topwrite, hold, part, repeat, minichoice, finalize, minichoicetemp, firstmini,once, frogger_bool
    global brian_model,adam_music, adam_music_bool

    if gameRun == 3:
        fill(0)
        rect(0,((height/5)+50),width,248)
        fill(255)
        textSize(150)
        text("Game Over!",width/2,(height/5)+230)
        textSize(40)
        text('Press Space to go back', width/2, height/2+275)
        textAlign(LEFT)
        if keyPressed and key==' ':
            background(0)
            topwrite = False
            wordswrite = False
            temp1=0
            hold=0
            part=0
            repeat=0
            minichoice=0
            finalize=False
            minichoicetemp=0
            firstmini=True      
            once=0
            frogger_bool=False
            adam_music.stop()
            brian_model=0
            p1X = (width/2)-10
            p1Y = (height/5)+352
            t = 0
            t1 = 0
            t2 = 0
            gameRun = 0
            adam_speed = []
            raaab = 60
            adam_music_bool=False
            
    if gameRun == 4:
        fill(0)
        rect(0,((height/5)+50),width,248)
        fill(255)
        textSize(150)
        text("You Win!",width/2,(height/5)+230) 
        textSize(40)
        text('Press Space to go back', width/2, height/2+275)
        textAlign(LEFT)
        if keyPressed and key==' ':
            background(0)
            topwrite = False
            wordswrite = False
            temp1=0
            hold=0
            part=0
            repeat=0
            minichoice=0
            finalize=False
            minichoicetemp=0
            firstmini=True      
            once=0
            frogger_bool=False
            adam_music.stop()
            brian_model=0
            p1X = (width/2)-10
            p1Y = (height/5)+352
            t = 0
            t1 = 0
            t2 = 0
            gameRun = 0
            adam_speed = []
            raaab = 60
            adam_music_bool=False