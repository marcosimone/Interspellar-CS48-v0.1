import socket
import sys
import threading
import pickle
from array import array
import pygame
from pygame.locals import *
from bullet import *
from player import Player
from dank_wiz import DankWizard
from dark_wiz import DarkWizard
from soundboard import soundboard

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
fpsClock = pygame.time.Clock()
font = pygame.font.Font('WhiteRabbit.ttf', 24)
icon = pygame.image.load("images/icon.png").convert_alpha()
sounds = soundboard()
y = 0
x = 0
gothreadgo = True
server_ip=""
server_port=0
shiftLookup={'1':'!', '2':'@', '3':'#', '4':'$', '5':'%', '6':'^', '7':'&', '8':'*', '9':'(', '0':')', ',':'<', '.':'>', '/':'?', ';':':', '\'':'"', '`':'~', '-':'_', '=':'+', '\\':'|'}
#background stuff
splash=pygame.image.load("images/liquid_toaster.png").convert()
click_continue=pygame.image.load("images/continue.png").convert()
logo = pygame.image.load("images/logo.png").convert_alpha()
stars = pygame.image.load("images/stars.png").convert_alpha()
stars2 = stars
hills = pygame.image.load("images/hills.png").convert_alpha()
lobby_back = pygame.image.load("images/lobby_background.png").convert_alpha()
clouds = pygame.image.load("images/lobby_clouds.png").convert_alpha()
mist = pygame.image.load("images/lobby_mist.png").convert_alpha()
mountains = pygame.image.load("images/lobby_mountains.png").convert_alpha()
level = []
#buttons
back_hover = pygame.image.load("images/buttons/back_hover.png").convert_alpha()
back_idle = pygame.image.load("images/buttons/back.png").convert_alpha()

bullets = []

#networking
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

toDraw_background = []
toDraw_bullets = []
toDraw_players = []

def main():

    pygame.mixer.music.load("sound/Lines_of_Code.wav")
    pygame.display.set_icon(icon)
    loading=True
    click=False
    alpha=0
    alpha2=12
    while loading:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                loading = False
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                #if click:
                loading = False
        splash.set_alpha(alpha%2)
        toDraw_background.append((splash, (500,150)))
        click_continue.set_alpha(alpha2)
        if click:
            toDraw_background.append((click_continue, (500, 460)))
        blit()
        alpha+=1
        if alpha >= 510:
            alpha=510
            click=True
            alpha2+=1
        
        pygame.display.update()
        pygame.display.set_caption("Loading Interspellar")
        fpsClock.tick(60)
    main_menu()

def main_menu():
    buttons_idle = [pygame.image.load("images/buttons/play.png").convert_alpha(),
                    pygame.image.load("images/buttons/options.png").convert_alpha(),
                                   pygame.image.load("images/buttons/credits.png").convert_alpha()]

    buttons_hover = [pygame.image.load("images/buttons/play_hover.png").convert_alpha(),
                     pygame.image.load("images/buttons/options_hover.png").convert_alpha(),
                                    pygame.image.load("images/buttons/credits_hover.png").convert_alpha()]

    buttons = [buttons_idle[0], buttons_idle[1], buttons_idle[2]]

    global y
    toDraw_background.append((stars, (0, y)))
    toDraw_background.append((stars, (0, y-720)))
    toDraw_background.append((hills, (0, 720-hills.get_height())))
    toDraw_background.append((logo, (254, 131)))

    for index, butt in enumerate(buttons):
        toDraw_background.append((butt, (500, 300+(100*index))))
    blit()
    #pygame.mixer.music.play(-1)
    while 1:

        for index, butt in enumerate(buttons):
            if Rect(500, 300+(100*index), butt.get_width(),
                    butt.get_height()).collidepoint(pygame.mouse.get_pos()):
                buttons[index] = buttons_hover[index]
            else:
                buttons[index] = buttons_idle[index]

        toDraw_background.append((stars, (0, y/2)))
        toDraw_background.append((stars, (0, y/2-720)))
        toDraw_background.append((hills, (0, 720-hills.get_height())))
        toDraw_background.append((logo, (254, 131)))
        for index, butt in enumerate(buttons):
            toDraw_background.append((butt, (500, 300+(100*index))))
        y += 1
        if y == 1440:
            y = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            elif event.type == MOUSEBUTTONUP and event.button == 1:
                for index, butt in enumerate(buttons):
                    if Rect(500, 300+(100*index), butt.get_width(),
                            butt.get_height()).collidepoint(event.pos):
                        sounds.click.play()
                        menu_choices[index]()

        blit()
        pygame.display.update()
        pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
        fpsClock.tick(60)

def blit():
    global level
    for pic in toDraw_background:
        if pic is not None:
            screen.blit(pic[0], pic[1])

    for plat in level:
        pygame.draw.rect(screen, Color("grey"), plat)

    for pic in toDraw_bullets:
        if pic is not None:
            screen.blit(pic[0], pic[1])
    for pic in toDraw_players:
        if pic is not None:
            screen.blit(pic[0], pic[1])
    del toDraw_background[:]
    del toDraw_bullets[:]

def join_server():
    global y
    #Box = (surface, text)
    join_idle = pygame.image.load("images/buttons/join.png").convert_alpha()
    join_hover = pygame.image.load("images/buttons/join_hover.png").convert_alpha()
    join = join_idle
    joinPos = ((screen.get_width() - join.get_width())/2, 500)

    screen.blit(stars, (0, y))
    screen.blit(stars, (0, y-720))
    screen.blit(hills, (0, 720-hills.get_height()))

    ipBox = [pygame.Surface((300, 40)), "127.0.0.1"] #DEBUG
    ipBox[0].fill(Color(255, 255, 255)) 
    portBox = [pygame.Surface((150, 40)), "4637"] #DEBUG
    
    portBox[0].fill(Color(196, 196, 196))
    ipPos = ((screen.get_width()-ipBox[0].get_width())/2,
             (screen.get_height()-ipBox[0].get_height())/2-80)
    portPos = ((screen.get_width()-ipBox[0].get_width())/2,
               (screen.get_height()-portBox[0].get_height())/2-20)

    screen.blit(ipBox[0], ipPos)
    screen.blit(portBox[0], portPos)
    back = back_idle
    screen.blit(join, ((screen.get_width()-join.get_width())/2, 500))
    screen.blit(back, (100, 575))
    focus = ipBox

    while 1:

        ipText = font.render(ipBox[1], True, Color(0, 0, 0))
        portText = font.render(portBox[1], True, Color(0, 0, 0))
        screen.blit(stars, (0, y/2))
        screen.blit(stars, (0, y/2-720))
        screen.blit(hills, (0, 720-hills.get_height()))
        screen.blit(ipBox[0], ipPos)
        screen.blit(ipText, (ipPos[0]+10, ipPos[1]+ipText.get_height()/2))
        screen.blit(portBox[0], (portPos))
        screen.blit(portText, (portPos[0]+10, portPos[1]+portText.get_height()/2))
        screen.blit(join, joinPos)
        screen.blit(back, (100, 575))

        if Rect(100, 575, back.get_width(), back.get_height()).collidepoint(pygame.mouse.get_pos()):
            back = back_hover
        else:
            back = back_idle

        if Rect(joinPos, (join.get_width(), join.get_height())
               ).collidepoint(pygame.mouse.get_pos()):
            join = join_hover
        else:
            join = join_idle

        y += 1
        if y == 1440:
            y = 0

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if Rect(ipPos, (ipBox[0].get_width(), ipBox[0].get_height())
                       ).collidepoint(event.pos):
                    focus = ipBox
                    ipBox[0].fill(Color(255, 255, 255))
                    portBox[0].fill(Color(196, 196, 196))
                elif Rect(portPos, (portBox[0].get_width(), portBox[0].get_height())
                         ).collidepoint(event.pos):
                    focus = portBox
                    ipBox[0].fill(Color(196, 196, 196))
                    portBox[0].fill(Color(255, 255, 255))
                elif Rect(joinPos, (back.get_width(), back.get_height())).collidepoint(event.pos):
                    sounds.click.play()
                    try_join(ipBox, portBox)
                elif Rect(100, 575, back.get_width(), back.get_height()).collidepoint(event.pos):
                    sounds.click.play()
                    return
            elif event.type == KEYDOWN:
                if(event.key >= 48 and event.key <= 57) or event.key == 46:
                    focus[1] += str(chr(event.key))
                elif event.key >= 256 and event.key <= 266:
                    if event.key == 266:
                        focus[1] += str(chr(46))
                    else:
                        focus[1] += str(chr(event.key-208))
                elif event.key == 8:
                    focus[1] = focus[1][:-1]
                elif event.key == 13 or event.key == 271:
                    sounds.click.play()
                    try_join(ipBox, portBox)
                elif event.key == 9:
                    if focus == ipBox:
                        focus = portBox
                        ipBox[0].fill(Color(196, 196, 196))
                        portBox[0].fill(Color(255, 255, 255))
                    else:
                        focus = ipBox
                        ipBox[0].fill(Color(255, 255, 255))
                        portBox[0].fill(Color(196, 196, 196))

            elif event.type == QUIT:
                sys.exit()

        pygame.display.update()
        pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
        fpsClock.tick(60)

def try_join(ipBox, portBox):
    try:
        global server_ip
        server_ip=ipBox[1]
        global server_port
        server_port=int(portBox[1])
        socket.inet_aton(server_ip)
        int(server_port)
        sock.sendto(pickle.dumps(("j")), (server_ip, server_port))
        sock.settimeout(3.0)
        data, addr = sock.recvfrom(1024)
        lobby_players = pickle.loads(data)
        print 'joining %s:%s' % (server_ip, server_port)
        lobby(lobby_players)

    except socket.timeout:
        print 'server could not be found'
    except socket.error:
        print 'invalid ip'
    except ValueError:
        print 'invalid port'

def lobby(players):
    global x
    game_start=[False]
    chat=[]
    font = pygame.font.SysFont('lucidaconsole', 16)
    chat_full=pygame.Surface((524, 0))
    chat_render=chat_full
    t = threading.Thread(target=lobby_thread, args=(players, chat, game_start))
    t.daemon = True
    t.start()
    team="default"
    global wizard
    wizard = "0"
    name="unnamed"
    chat_box = [pygame.Surface((524, 25)), ""]
    chat_box[0].fill(Color(255, 255, 255)) 
    name_box = [pygame.Surface((200, 30)), name] 
    name_box[0].fill(Color(196, 196, 196))
    name_label=pygame.image.load("images/buttons/name.png").convert_alpha()
    chatPos = ((screen.get_width()-chat_box[0].get_width())/2,(screen.get_height()-chat_box[0].get_height()-10))
    namePos = ((screen.get_width()-name_box[0].get_width())/2,10)
    screen.blit(chat_box[0], chatPos)
    screen.blit(name_box[0], namePos)
    focus = chat_box
    #team_1_top = [pygame.image.load("images/team_1_top_1_re.png").convert_alpha(), pygame.image.load("images/team_1_top_2_re.png").convert_alpha(),pygame.image.load("images/team_1_top_3_re.png").convert_alpha(), pygame.image.load("images/team_1_top_4_re.png").convert_alpha()]
    #team_2_top = [pygame.image.load("images/team_2_top_1_re.png").convert_alpha(), pygame.image.load("images/team_2_top_2_re.png").convert_alpha(),pygame.image.load("images/team_2_top_3_re.png").convert_alpha(), pygame.image.load("images/team_2_top_4_re.png").convert_alpha()]
    team_1_mid = pygame.image.load("images/team_1_mid.png").convert_alpha()
    team_2_mid = pygame.image.load("images/team_2_mid.png").convert_alpha()
    team_1_top = pygame.image.load("images/team_1_top_re.png").convert_alpha()#####
    team_2_top = pygame.image.load("images/team_2_top_re.png").convert_alpha()#####
    team_1_bot = pygame.image.load("images/team_1_bot_re.png").convert_alpha()
    team_2_bot = pygame.image.load("images/team_2_bot_re.png").convert_alpha()
    arrow = [pygame.transform.flip(pygame.image.load("images/buttons/lobby_char.png").convert_alpha(), True, False), 
             pygame.image.load("images/buttons/lobby_char.png").convert_alpha()]
    arrow_hover = [pygame.transform.flip(pygame.image.load("images/buttons/lobby_char_hover.png").convert_alpha(), True, False),
                   pygame.image.load("images/buttons/lobby_char_hover.png").convert_alpha()]
    info_panel=[pygame.image.load("images/buttons/info_panel_dank.png").convert_alpha(),
                pygame.image.load("images/buttons/info_panel_dark.png").convert_alpha(),
                pygame.image.load("images/buttons/info_panel_healer.png").convert_alpha(),
                pygame.image.load("images/buttons/info_panel_gravity.png").convert_alpha()]
    team_char_select=[]
    set=pygame.image.load("images/buttons/set_button.png").convert_alpha()
    start=pygame.image.load("images/buttons/start.png").convert_alpha()
    panel=pygame.image.load("images/buttons/char_panel.png").convert_alpha()
    ready = pygame.image.load("images/ready.png").convert_alpha()
    for i in range(0,4):
        team_char_select.append(arrow[0])
        team_char_select.append(arrow[1])
    idle_anim=[]
    for i in range(4):
        names=["dankwiz/", "wiz_atk_", "darkwiz/", "dark_idle_", "healer/","healer_idle_", "dankwiz/", "wiz_atk_"]
        for j in range(5):
            anim_string = "images/animations/" + names[2*i] + names[2*i+1] + str(j+1) + ".png"
            idle_anim.append(pygame.transform.scale(pygame.image.load(anim_string).convert_alpha(), (64, 64)))
    idle_anim_frame=[0,0,0,0]
    info=-1
    chat_label=font.render(' chat ', True, Color("#749DCF"), Color(0, 0, 0))
    while 1:
        
        font = pygame.font.SysFont('lucidaconsole', 16)
        chatText = font.render(chat_box[1], True, Color(0, 0, 0))
        nameText = font.render(name_box[1], True, Color(0, 0, 0))
        if game_start[0]:
            play()
            return
        if len(chat)!=0:
            text=chat.pop()
            text='%s: %s' % (players[text[0][0]][1], text[1])
            size=font.size(text)
            if size[0]+3 > 524:
                linenum=size[0]/542+1
                split_length=int(len(text)/((size[0]+.0)/(524+.0)))
                text_split=[text[i:i+split_length] for i in range(0, len(text), split_length)]
                msg=pygame.Surface((524, size[1]*linenum))
                for index,sub in enumerate(text_split):
                    msg.blit(font.render(sub, True, Color(255, 255, 255)), (0, index*size[1]))
            else:
                linenum=1
                msg=font.render(text, True, Color(255, 255, 255))
            
            old_render=chat_full
            old_render.set_alpha(255)
            
            chat_full=pygame.Surface((524, old_render.get_height()+msg.get_height()))
            chat_full.fill(Color(0, 0, 0))
            chat_full.set_alpha(180)
            chat_full.blit(old_render, (0,0))
            chat_full.blit(msg, (3, old_render.get_height()))
            
            if chat_full.get_height() > 190:
                chat_render=chat_full.subsurface(pygame.Rect((0, chat_full.get_height()-204),(524, 204)))
            else:
                chat_render=chat_full

        screen.blit(lobby_back, (0, 720-lobby_back.get_height()))
        screen.blit(mist, (x/4,0))
        screen.blit(mist, (x/4-1280,-50))
        screen.blit(mountains, (0,0))
        screen.blit(clouds, (x%1280, 0))
        screen.blit(clouds, (x%1280-1280, 0))
        
        screen.blit(chat_box[0], chatPos)
        screen.blit(chatText, (chatPos[0]+10, chatPos[1]+chatText.get_height()/2))
        screen.blit(name_box[0], (namePos))
        screen.blit(nameText, (namePos[0]+10, namePos[1]+nameText.get_height()/2))
        #screen.blit(team_1_top[int((x/4)%4)], (20,0))
        #screen.blit(team_2_top[int((x/4)%4)], (800,0))
        screen.blit(team_1_top, (20,20))
        screen.blit(team_2_top, (800,20))
        screen.blit(start, (1000, 600    ))
        
        #(port, name, sprite, team)
        font=pygame.font.Font('WhiteRabbit.ttf', 24)
        player_list_1=[]
        player_list_2=[]
        for player in players:
            if players[player][3]=='0':
                player_entry=team_1_mid.copy()
                player_entry.blit(idle_anim[5*int(players[player][2])], (8, 8))
                player_name=font.render(players[player][1], True, Color(0, 0, 0))
                player_entry.blit(player_name, (64+8+5, player_entry.get_height()/2-font.size(players[player][1])[1]/2))
                ##check if ready
                player_list_1.append(player_entry)
                
            elif players[player][3]=='1':
                player_entry=team_2_mid.copy()
                player_entry.blit(idle_anim[5*int(players[player][2])], (8, 8))
                player_name=font.render(players[player][1], True, Color(0, 0, 0))
                player_entry.blit(player_name, (64+8+5, player_entry.get_height()/2-font.size(players[player][1])[1]/2))
                ##check if ready
                player_list_2.append(player_entry)
        for i in range(0, len(player_list_1)):
            screen.blit(player_list_1[i], (20, team_1_mid.get_height()*i+team_1_top.get_height()+20))
        for i in range(0, len(player_list_2)):
            screen.blit(player_list_2[i], (800, team_2_mid.get_height()*i+team_2_top.get_height()+20))
        screen.blit(team_2_bot, (800,team_2_top.get_height()+20+team_2_mid.get_height()*len(player_list_2)))
        screen.blit(team_1_bot, (20,team_1_top.get_height()+20+team_1_mid.get_height()*len(player_list_1)))
        screen.blit(name_label, (namePos[0]-name_label.get_width()-5, namePos[1]))
        screen.blit(set, (namePos[0]+name_box[0].get_width()+5, namePos[1]))
        
        screen.blit(chat_render, (screen.get_width()/2-262, screen.get_height()-chat_render.get_height()-35))
        screen.blit(chat_label, (screen.get_width()/2-262, screen.get_height()-chat_render.get_height()-35-chat_label.get_height()))
        screen.blit(ready, (640+chat_render.get_width()/2+(1280-(640+chat_render.get_width()/2))/2-ready.get_width()/2,600))
        x+=.5
        if x > 1280*4:
            x = 0;
        
        for index,box in enumerate(team_char_select):
            if Rect(640-40 - ((index+1)%2) * 45 + index%2*80, 175+(75*(index/2)), box.get_width(), box.get_height()).collidepoint(pygame.mouse.get_pos()):
                team_char_select[index]=arrow_hover[index%2]           
            else:
                team_char_select[index]=arrow[index%2]
            screen.blit(box, (640-40 - ((index+1)%2) * 45 + index%2*80, 175+(75*(index/2))))
            
        for i in range(0,4):
            if Rect(640-32, 175+75*i, 64, 64).collidepoint(pygame.mouse.get_pos()):
                info=i
                idle_anim_frame[i]+=.1
                if idle_anim_frame[i]>=25:
                    idle_anim_frame[i]=0
   
            screen.blit(panel, (640-35, 175+(75*(i))))
            screen.blit(idle_anim[i*5+int(idle_anim_frame[i])%5], (640-32, 175+(75*(i))))
        if info!=-1:
            screen.blit(info_panel[info], (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]-10))    
            info=-1
            
        for event in pygame.event.get():
        
            if event.type == MOUSEBUTTONUP and event.button == 1:
                for index,box in enumerate(team_char_select):
                    if Rect(640-40 - ((index+1)%2) * 45 + index%2*80, 175+(75*(index/2)), box.get_width(), box.get_height()).collidepoint(event.pos):
                        team = str(index%2)
                        wizard = str(index/2)
                        sock.sendto(pickle.dumps(("u", name, wizard, team)), (server_ip, server_port))
                        sounds.click.play()
                        #print "wizard:%s\nteam:%s\n" % (wizard, team)
                if Rect(chatPos, (chat_box[0].get_width(), chat_box[0].get_height())
                       ).collidepoint(event.pos):
                    focus = chat_box
                    chat_box[0].fill(Color(255, 255, 255))
                    name_box[0].fill(Color(196, 196, 196))
                elif Rect(namePos, (name_box[0].get_width(), name_box[0].get_height())
                         ).collidepoint(event.pos):
                    focus = name_box
                    chat_box[0].fill(Color(196, 196, 196))
                    name_box[0].fill(Color(255, 255, 255))
                elif Rect((namePos[0]+name_box[0].get_width()+5, namePos[1]), (set.get_width(), set.get_height())
                         ).collidepoint(event.pos):
                    sock.sendto(pickle.dumps(("u", name_box[1], wizard, team)),(server_ip, server_port))
                    name=name_box[1]

                    sounds.click.play()
                elif Rect((640+chat_render.get_width()/2+(1280-(640+chat_render.get_width()/2))/2-ready.get_width()/2,600), (ready.get_width(),ready.get_height())).collidepoint(event.pos):
                         sounds.click.play()
                         sock.sendto(pickle.dumps(("*")),(server_ip, server_port))
            elif event.type == KEYDOWN:
                
                if pygame.key.get_pressed()[304]:
                    if (event.key>=39 and event.key<=61) or (event.key>=91 and event.key<=96):
                        focus[1]+=shiftLookup[str(chr(event.key))]
                    elif event.key>=97 and event.key<=122:
                        focus[1]+=str(chr(event.key-32))
                elif(event.key >= 32 and event.key <= 126) or event.key == 46:
                    focus[1] += str(chr(event.key))
                elif event.key >= 256 and event.key <= 266:
                    if event.key == 266:
                        focus[1] += str(chr(46))
                    else:
                        focus[1] += str(chr(event.key-208))
                elif event.key == 8:
                    focus[1] = focus[1][:-1]
                elif event.key == 13 or event.key == 271:
                    sounds.click.play()
                    if focus==chat_box:
                        sock.sendto(pickle.dumps(("c", focus[1])), (server_ip, server_port))
                        focus[1]=''
                    else:
                        sock.sendto(pickle.dumps(("u", focus[1], wizard, team)),(server_ip, server_port))
                        name=focus[1]
                elif event.key == 9:
                    if focus == chat_box:
                        focus = name_box
                        chat_box[0].fill(Color(196, 196, 196))
                        name_box[0].fill(Color(255, 255, 255))
                    else:
                        focus = chat_box
                        chat_box[0].fill(Color(255, 255, 255))
                        name_box[0].fill(Color(196, 196, 196))
            elif event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
        fpsClock.tick(60)


def lobby_thread(players, chat, start):
    sock.settimeout(None)
    sock.sendto(pickle.dumps("t"), (server_ip, server_port))
    
    while True:
        data, addr = sock.recvfrom(1024)
        data=pickle.loads(data)
        src=data[1]
        cmd=data[0]
        
        if cmd[0] == "c":
            chat.append((src, cmd[1]))
       
        elif cmd[0] == "u":
            players[src[0]] = (src[1], cmd[1], cmd[2], cmd[3])
        elif cmd[0] == "j":
            players[src[0]] = (addr[1], addr[0], "default", "default")
            print '%s joined' % (src[0])
            print players
        elif cmd[0] == "q":
            del clients[src[0]]
        elif cmd[0] == "*":
            start[0]=True
    

def play():
    global level
    global wizard
    level=[Rect((100,575),(300,70)), Rect((300,175),(300,70)), Rect((200,375),(100,20)), Rect((800,200),(100,500)), Rect((1100,200),(100,500))]
    player=DankWizard(screen, sounds, level, (640, 650))
    if wizard == '0':
        player=DankWizard(screen, sounds, level, (640, 650)) 
    elif wizard == '1':
        player=DarkWizard(screen, sounds, level, (640, 650)) 
    elif wizard == '2':
        player=Healer(screen, sounds, level, (640, 650)) 
    elif wizard == '3':
        player=DankWizard(screen, sounds, level, (640, 650))
    toDraw_players.append(player.draw())
    gothreadgo=True
    t = threading.Thread(target=update_foes)
    t.daemon = True
    t.start()
    global y
    back=back_idle
    while 1:
        toDraw_background.append((stars, (0,y/2)))
        toDraw_background.append((stars, (0,y/2-720)))
        toDraw_background.append((hills, (0,720-hills.get_height())))
        toDraw_background.append((back, (100, 575)))

        y +=1
        if y==1440:
            y=0

        if Rect(100,575,back.get_width(), back.get_height()).collidepoint(pygame.mouse.get_pos()):
            back=back_hover
        else:
            back=back_idle

        for event in pygame.event.get():

            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONUP and event.button==1:
                if Rect(100,575,back.get_width(), back.get_height()).collidepoint(event.pos):
                    sounds.click.play()
                    del toDraw_players[:]
                    gothreadgo=False
                    level=[]
                    return
            if event.type==MOUSEBUTTONDOWN and event.button==3:
                bull=Bullet(screen, sounds, level, event.pos, player.getPos())
                bullets.append(bull)
                sock.sendto(pickle.dumps("b" + bull.toString()),(server_ip, server_port))


        for bullet in enumerate(bullets):
            if bullet[1].isDead():
                sounds.explode.play()
                del bullets[bullet[0]]
            else:
                bullet[1].update()
                toDraw_bullets.append(bullet[1].draw())
        input = [pygame.key.get_pressed()[119]==1,pygame.key.get_pressed()[97]==1,pygame.key.get_pressed()[115]==1,pygame.key.get_pressed()[100]==1]
        player.update(input, bullets)
        sock.sendto(pickle.dumps(player.getPos()),(server_ip, server_port))
        toDraw_players[0]=player.draw()
        blit()
        pygame.display.update()
        pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
        fpsClock.tick(60)

def update_foes():
    other_players={}
    sock.sendto(pickle.dumps((("b"),(Bullet(screen, sounds, level, (-1,-1), (-1,-1))).toString())),
                             (server_ip, server_port))
    while True:
        data, addr = sock.recvfrom(1024)
        data=pickle.loads(data)
        #print data
        if  data[0].equals("s"):
            print 0
        elif data[0].equals("b"):
            bull=enemyBullet(screen, sounds, level, data[1])
            bullets.append(bull)
        else:
            if not other_players.has_key(data[0]):
                other_players[data[0]]=Player(screen, sounds, level, (640, 650))
                toDraw_players.append(other_players[data[0]])
            other_players[data[0]].setPos(data[1])
            count=0
            for key in other_players:
                toDraw_players[1+count]=other_players[key].draw()

                count +=1

def options():
    walker = [pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_1.png").convert_alpha()),
              pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_2.png").convert_alpha()),
              pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_3.png").convert_alpha()),
              pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_4.png").convert_alpha())]
    global y
    x = 0
    back = back_idle
    while 1:
        screen.blit(stars, (0, y/2))
        screen.blit(stars, (0, y/2-720))
        screen.blit(hills, (0, 720-hills.get_height()))
        screen.blit(back, (100, 575))
        x += 1
        if x >= 1280+64:
            screen.blit(pygame.transform.flip(walker[(x/9)%4], True, False), ((x-1280-64-64), 650))
            if x == 2*(1280+64):
                x = 0
        else:
            screen.blit(walker[(x/9)%4], (1280-x, 650))
        y += 1
        if y == 1440:
            y = 0

        if Rect(100, 575, back.get_width(), back.get_height()).collidepoint(pygame.mouse.get_pos()):
            back = back_hover
        else:
            back = back_idle

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if Rect(100, 575, back.get_width(), back.get_height()).collidepoint(event.pos):
                    sounds.click.play()
                    return
        pygame.display.update()
        pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
        fpsClock.tick(60)

def credits():
    return

menu_choices = [join_server, options, credits]

if __name__ == "__main__":
    main()
