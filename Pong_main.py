################################
# Name: Barry Cimring
# Date: 15/5/2019
# Description: The game of pong
################################

import pygame
import time
import math as m
from random import randint

pygame.init()

WIDTH = 1000
HEIGHT = 750

game_window = pygame.display.set_mode((WIDTH,HEIGHT))

GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (200,0,255)
LIGHTRED = (255,200,200)
LIGHTBLUE = (200,200,255)

paddle_1_length = 100
paddle_2_length = 100

paddle_y1 = 325
paddle_y2 = 325
paddle_x1 = 30
paddle_x2 = 960
paddle_speed = 5

ball_x = 500
ball_y = 375
ballR = 35

ball_speed_x = 6
ball_speed_y = 6
random_direction = [-1,1]
ball_speed_x *= random_direction[randint(0,1)]
ball_speed_y *= random_direction[randint(0,1)]



distance_top_paddle_1 = m.sqrt((paddle_x1-ball_x)**2 + (paddle_y1-ball_y)**2)
distance_top_paddle_2 = m.sqrt((paddle_x2-ball_x)**2 + (paddle_y2-ball_y)**2)
distance_bottom_paddle_1 = m.sqrt((paddle_x1-ball_x)**2 + (paddle_y1-ball_y+100)**2)
distance_bottom_paddle_2 = m.sqrt((paddle_x2-ball_x)**2 + (paddle_y2-ball_y+100)**2)

score_1 = 0
score_2 = 0
scoreFont = pygame.font.SysFont("Cambria", 50)

play_1_player = "1 Player"
play_2_player = "2 Players"
playFont = pygame.font.SysFont("Cambria",100)
playerOne = "Player 1"
playerTwo = "Player 2"

introMessage = "Hi there! Welcome to the realm of Pong. We take rules seriously here, so listen up:"
rule1_text = "1. If a ball is not hit back, the other player gets a point."
rule2_text = '2. Player 1 uses keys "W", "S", player 2 uses arrow keys.'
rule3_text = "3. First player to 7 points wins!"

introFont = pygame.font.SysFont("Arial Black",40)
ruleFont = pygame.font.SysFont("Arial Black",30)

#-----------------------------------FUNCTIONS--------------------------------------------#
def intro_screen():
    game_window.fill(BLACK)
    pygame.draw.rect(game_window,GREEN,(50,550,400,150))
    pygame.draw.rect(game_window,GREEN,(550,550,400,150))
    
    button_1 = playFont.render(play_1_player,1,BLACK)
    button_2 = playFont.render(play_2_player,1,BLACK)
    intro = introFont.render(introMessage[:39],1,LIGHTRED)
    rules = introFont.render(introMessage[40:92],1,LIGHTRED)
    rule_1 = ruleFont.render(rule1_text,1,LIGHTBLUE)
    rule_2 = ruleFont.render(rule2_text,1,LIGHTBLUE)
    rule_3 = ruleFont.render(rule3_text,1,LIGHTBLUE)

    game_window.blit(intro,(40,50))
    game_window.blit(rules,(40,110))
    game_window.blit(rule_1,(40,200))
    game_window.blit(rule_2,(40,300))
    game_window.blit(rule_3,(40,400))
    game_window.blit(button_1,(70,565))
    game_window.blit(button_2,(560,565))
    
    pygame.display.update()

def difficulty_screen():
    game_window.fill(BLACK)
    pygame.draw.rect(game_window,GREEN,(50,50,900,215))
    pygame.draw.rect(game_window,YELLOW,(50,270,900,215))
    pygame.draw.rect(game_window,RED,(50,490,900,215))
    E = "Easy"
    M = "Medium"
    H = "Hard"
    emh_font = pygame.font.SysFont("Times New Roman",180,True)
    easy = emh_font.render(E,1,BLACK)
    medium = emh_font.render(M,1,BLACK)
    hard = emh_font.render(H,1,BLACK)
    game_window.blit(easy,(300,50))
    game_window.blit(medium,(180,265))
    game_window.blit(hard,(280,480))
    pygame.display.update()

    
def win_screen1():
    game_window.fill(BLACK)
    winText = "Player 1 Wins!"
    winFont = pygame.font.SysFont("Cambria", 105)
    message = winFont.render(winText,1,WHITE)
    game_window.blit(message,(170,300))
    pygame.display.update()
    pygame.time.delay(2000)
    
def win_screen2():
    game_window.fill(BLACK)
    winText = "Player 2 Wins!"
    winFont = pygame.font.SysFont("Cambria", 105)
    message = winFont.render(winText,1,WHITE)
    game_window.blit(message,(170,300))
    pygame.display.update()
    pygame.time.delay(2000)

def computer_win():
    game_window.fill(BLACK)
    winText = "Computer Wins!"
    winFont = pygame.font.SysFont("Cambria", 105)
    message = winFont.render(winText,1,WHITE)
    game_window.blit(message,(170,300))
    pygame.display.update()
    pygame.time.delay(2000)

def redrawGameField():
    game_window.fill(PURPLE)
    pygame.draw.rect(game_window,BLACK,(10,10,485,730),0)
    pygame.draw.rect(game_window,BLACK,(505,10,485,730),0)

    pygame.draw.rect(game_window,WHITE,(paddle_x1,paddle_y1,10,paddle_1_length),0)
    pygame.draw.rect(game_window,WHITE,(paddle_x2,paddle_y2,10,paddle_2_length),0)

    gameBoard1 = scoreFont.render(str(score_1),1,WHITE)
    gameBoard2 = scoreFont.render(str(score_2),1,WHITE)
    player_1 = scoreFont.render(playerOne,1,WHITE)
    player_2 = scoreFont.render(playerTwo,1,WHITE)
    
    game_window.blit(gameBoard1,(430,340))
    game_window.blit(gameBoard2,(530,340))
    game_window.blit(player_1,(50,50))
    game_window.blit(player_2,(770,50))

    pygame.draw.circle(game_window,PURPLE,(500,375),100,5)
    pygame.draw.circle(game_window,GREEN,(ball_x,ball_y),ballR,0)

    pygame.display.update()

def bounceBall(distance_top_paddle_1,distance_top_paddle_2,distance_bottom_paddle_1,distance_bottom_paddle_2,ball_speed_x,ball_speed_y,direction_paddle_1,direction_paddle_2):
    if (distance_top_paddle_1 < 122) and (distance_bottom_paddle_1 <122) and (0 < (ball_x-paddle_x1) < 35):
        if direction_paddle_1 > 0:
            if ball_speed_y < 0:
                ball_speed_x *= -1
                ball_speed_y *= -1
            else:
                ball_speed_x *= -1
        elif direction_paddle_1 < 0:
            if ball_speed_y > 0:
                ball_speed_x *= -1
                ball_speed_y *= -1
            else:
                ball_speed_x *= -1
        else:
            ball_speed_x *= -1
            
    if (distance_top_paddle_2 < 122) and (distance_bottom_paddle_2 <122) and (0 < (paddle_x2-ball_x) < 35):
        if direction_paddle_2 > 0:
            if ball_speed_y < 0:
                ball_speed_x *= -1
                ball_speed_y *= -1
            else:
                ball_speed_x *= -1
        elif direction_paddle_2 < 0:
            if ball_speed_y > 0:
                ball_speed_x *= -1
                ball_speed_y *= -1
            else:
                ball_speed_x *= -1
        else:
            ball_speed_x *= -1
    if ball_y - ballR <= 0:
        ball_speed_y *= -1
    if ball_y +ballR >= 750:
        ball_speed_y *= -1
    return ball_speed_x,ball_speed_y


def keyPressedTwoPlayer(paddle_y1,paddle_y2,paddle_speed):
    keys = pygame.key.get_pressed()     # get_pressed() method generates a True/False list                                # for the status of all keys
    if keys[pygame.K_UP]:               # if up arrow has been pressed
        if 0 <= paddle_y2:
            paddle_y2 = paddle_y2 - paddle_speed     # move the ball up
        else:
            paddle_y2 = paddle_y2 + paddle_speed*2
            
    if keys[pygame.K_DOWN]:             # if down arrow has been pressed
        if paddle_y2 <=650:
            paddle_y2 = paddle_y2 + paddle_speed       # move the ball down
        else:
            paddle_y2 = paddle_y2 - paddle_speed*2
            
    if keys[pygame.K_w]:               # if up arrow has been pressed
        if 0 <= paddle_y1:
            paddle_y1 = paddle_y1 - paddle_speed     # move the ball up
        else:
            paddle_y1 = paddle_y1 + paddle_speed*2
            
    if keys[pygame.K_s]:             # if down arrow has been pressed
        if paddle_y1 <=650:
            paddle_y1 = paddle_y1 + paddle_speed       # move the ball down
        else:
            paddle_y1 = paddle_y1 - paddle_speed*2
            
    return paddle_y1,paddle_y2

def keyPressedOnePlayer(paddle_y1,paddle_speed):
    keys = pygame.key.get_pressed()     # get_pressed() method generates a True/False list                                # for the status of all keys
    if keys[pygame.K_w]:               # if up arrow has been pressed
        if 0 <= paddle_y1:
            paddle_y1 = paddle_y1 - paddle_speed     # move the ball up
        else:
            paddle_y1 = paddle_y1 + paddle_speed*2
            
    if keys[pygame.K_s]:             # if down arrow has been pressed
        if paddle_y1 <=650:
            paddle_y1 = paddle_y1 + paddle_speed       # move the ball down
        else:
            paddle_y1 = paddle_y1 - paddle_speed*2
            
    return paddle_y1

def CPU_move(ball_x,ball_y,ballR,ball_speed_x,ball_speed_y,paddle_y2):
    if ball_speed_x > 0:
        if ball_speed_y > 0:
            if paddle_y2 <650:
                if abs((ball_y + ball_speed_y)-(paddle_y2+paddle_speed+50)) < abs((ball_y + ball_speed_y)-(paddle_y2-paddle_speed+50)):
                    paddle_y2 += paddle_speed
            else:
                paddle_y2 -= 3
                
        if ball_speed_y < 0:
            if paddle_y2 > 0 :
                if abs((ball_y + ball_speed_y)-(paddle_y2-paddle_speed+50)) < abs((ball_y + ball_speed_y)-(paddle_y2+paddle_speed+50)):
                    paddle_y2 -= paddle_speed
            else:
                paddle_y2 += 3
    return paddle_y2

def moveBall(ball_x,ball_y,ball_speed_x,ball_speed_y):
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    return ball_x,ball_y

def castNewBallTwoPlayer(score):
    if score == True:
        ball_x = 250
        ball_y = 375
        ball_speed_x = randint(6,8)
        ball_speed_y = randint(6,8)
        ball_speed_y *= random_direction[randint(0,1)]
    elif score == False:
        ball_x = 750
        ball_y = 375
        ball_speed_x = randint(-8,-6)
        ball_speed_y = randint(6,8)
        ball_speed_y *= random_direction[randint(0,1)]
        
    return ball_x,ball_y, ball_speed_x, ball_speed_y
    
def castNewBallOnePlayer(score):
    if score == True:
        ball_x = 250
        ball_y = 375
        ball_speed_x = randint(6,10)
        ball_speed_y = randint(6,7)
        ball_speed_y *= random_direction[randint(0,1)]
    elif score == False:
        ball_x = 750
        ball_y = 375
        ball_speed_x = randint(-6,-4)
        ball_speed_y = randint(6,7)
        ball_speed_y *= random_direction[randint(0,1)]
    paddle_y2 = 325

    return ball_x,ball_y, ball_speed_x, ball_speed_y,paddle_y2


#---------------------------------------MAIN-------------------------------------------#
introScreen = False
while not introScreen:
    intro_screen()
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (550 < mouse_x < 950) and (550 < mouse_y <700 ):
                two_players = True
                introScreen = True
            elif (50 < mouse_x < 450) and (550 < mouse_y <700 ):
                two_players = False
                introScreen = True
                
if two_players == False:
    difficult = False
    playerTwo = "Computer"
    while not difficult:
        difficulty_screen()
        mouse_x,mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (50 < mouse_x <950) and (50 < mouse_y < 265):
                    difficulty = 1
                    difficult = True
                if (50 < mouse_x <950) and (265 < mouse_y < 480):
                    difficulty = 2
                    difficult = True
                if (50 < mouse_x <950) and (480 < mouse_y < 695):
                    difficulty = 3
                    difficult = True
        
            

#------------------------------------------------------------TWO PLAYERS----------------------------------------------------#

redrawGameField()
pygame.time.delay(1000)
exit_flag = False
if two_players == True:
    while not exit_flag:
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:   # If user clicked close
                exit_flag = True
        
        #Move paddles
        #----------------------------------------------------------------------------------------------------------#
        previous_paddle_y1 = paddle_y1
        previous_paddle_y2 = paddle_y2
        
        (paddle_y1,paddle_y2) = keyPressedTwoPlayer(paddle_y1,paddle_y2,paddle_speed)

        direction_paddle_1 = paddle_y1 - previous_paddle_y1
        direction_paddle_2 = paddle_y2 - previous_paddle_y2
        #----------------------------------------------------------------------------------------------------------#

        #Bounce and move ball
        #----------------------------------------------------------------------------------------------------------#
        (ball_speed_x,ball_speed_y) = bounceBall(distance_top_paddle_1,     distance_top_paddle_2,     distance_bottom_paddle_1,     distance_bottom_paddle_2,   ball_speed_x,   ball_speed_y,  direction_paddle_1,  direction_paddle_2)
        
        (ball_x,ball_y) = moveBall(ball_x,ball_y,ball_speed_x,ball_speed_y)
        #----------------------------------------------------------------------------------------------------------#
            
        
        #Distance from paddles
        #----------------------------------------------------------------------------------------------------------#
        distance_top_paddle_1 = m.sqrt((paddle_x1-ball_x+10)**2 + (paddle_y1-ball_y)**2)
        distance_top_paddle_2 = m.sqrt((paddle_x2-ball_x+10)**2 + (paddle_y2-ball_y)**2)
        distance_bottom_paddle_1 = m.sqrt((paddle_x1-ball_x)**2 + (paddle_y1-ball_y+100)**2)
        distance_bottom_paddle_2 = m.sqrt((paddle_x2-ball_x)**2 + (paddle_y2-ball_y+100)**2)
        #----------------------------------------------------------------------------------------------------------#
        redrawGameField()

        
        #New Ball
        #----------------------------------------------------------------------------------------------------------#
        if (ball_x + ballR) < 0:
            score_2 += 1
            (ball_x,ball_y,ball_speed_x,ball_speed_y) = castNewBallTwoPlayer(False)
            redrawGameField()
            pygame.time.delay(1000)
        if (ball_x - ballR) > 1000:
            score_1 += 1
            (ball_x,ball_y,ball_speed_x,ball_speed_y) = castNewBallTwoPlayer(True)
            redrawGameField()
            pygame.time.delay(1000)
        if score_1 == 7:
            win = True
            exit_flag = True
        if score_2 == 7:
            win = False
            exit_flag = True
        #----------------------------------------------------------------------------------------------------------#
        pygame.time.delay(8)

    if win == True:
        win_screen1()

    if win == False:
        win_screen2()

        
#------------------------------------------------------------ONE PLAYER----------------------------------------------------#
paddle_speed_player = 0
paddle_speed_computer = 0
if two_players == False:
    if difficulty == 1:
        delay = 8
        paddle_speed_player = 6
        paddle_speed_CPU = 4
        
    if difficulty == 2:
        delay = 7
        paddle_speed_player = 6
        paddle_speed_CPU = 5
        
    if difficulty == 3:
        delay = 6
        paddle_speed_player = 5
        paddle_speed_CPU = 6
    
if two_players == False:
    while not exit_flag:
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:   # If user clicked close
                exit_flag = True
                
        #Move paddles
        #----------------------------------------------------------------------------------------------------------#
        previous_paddle_y1 = paddle_y1
        previous_paddle_y2 = paddle_y2
        
        (paddle_y1) = keyPressedOnePlayer(paddle_y1,paddle_speed_player)
        (paddle_y2) = CPU_move(ball_x,ball_y,ballR,ball_speed_x,ball_speed_y,paddle_y2)

        direction_paddle_1 = paddle_y1 - previous_paddle_y1
        direction_paddle_2 = paddle_y2 - previous_paddle_y2
        #----------------------------------------------------------------------------------------------------------#

        
        #Bounce and move ball
        #----------------------------------------------------------------------------------------------------------#
        (ball_speed_x,ball_speed_y) = bounceBall(distance_top_paddle_1,     distance_top_paddle_2,     distance_bottom_paddle_1,     distance_bottom_paddle_2,   ball_speed_x,   ball_speed_y,  direction_paddle_1,  direction_paddle_2)
        
        (ball_x,ball_y) = moveBall(ball_x,ball_y,ball_speed_x,ball_speed_y)
        #----------------------------------------------------------------------------------------------------------#


        #Distance from paddles
        #----------------------------------------------------------------------------------------------------------#
        distance_top_paddle_1 = m.sqrt((paddle_x1-ball_x+10)**2 + (paddle_y1-ball_y)**2)
        distance_top_paddle_2 = m.sqrt((paddle_x2-ball_x+10)**2 + (paddle_y2-ball_y)**2)
        distance_bottom_paddle_1 = m.sqrt((paddle_x1-ball_x)**2 + (paddle_y1-ball_y+100)**2)
        distance_bottom_paddle_2 = m.sqrt((paddle_x2-ball_x)**2 + (paddle_y2-ball_y+100)**2)
        #----------------------------------------------------------------------------------------------------------#
        redrawGameField()

        
        #New Ball
        #----------------------------------------------------------------------------------------------------------#
        if (ball_x + ballR) < 0:
            score_2 += 1
            (ball_x,ball_y,ball_speed_x,ball_speed_y,paddle_y2) = castNewBallOnePlayer(False)
            redrawGameField()
            pygame.time.delay(1000)
        if (ball_x - ballR) > 1000:
            score_1 += 1
            (ball_x,ball_y,ball_speed_x,ball_speed_y,paddle_y2) = castNewBallOnePlayer(True)
            redrawGameField()
            pygame.time.delay(1000)
        if score_1 == 7:
            win = True
            exit_flag = True
        if score_2 == 7:
            win = False
            exit_flag = True
        #----------------------------------------------------------------------------------------------------------#
        pygame.time.delay(delay)
        
    if win == True:
        win_screen1()

    if win == False:
        computer_win()

pygame.quit()
