import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Pong")

win = pygame.image.load("assets/win.png")

score_player_1 = 0
score_player_1_img = pygame.image.load("assets/score/0.png")
score_player_2 = 0
score_player_2_img = pygame.image.load("assets/score/0.png")



field = pygame.image.load("assets/field.png")
player_1 = pygame.image.load("assets/player1.png")
player_2 = pygame.image.load("assets/player2.png")
ball = pygame.image.load("assets/ball.png")

player_1_x = 50
player_1_y = 290
player_1_moveup = False
player_1_movedown = False


player_2_x = 1150
player_2_y = 290

ball_x = 617
ball_y = 337

ball_direction = -10
ball_direction_y = 1

def ball_movement():
    global ball_x
    global ball_y
    global ball_direction
    global ball_direction_y
    global score_player_1
    global score_player_1_img
    global score_player_2
    global score_player_2_img

    ball_x += ball_direction
    ball_y += ball_direction_y

    if ball_x < 120:
        if player_1_y < ball_y + 23:
            if player_1_y + 146 > ball_y:
                ball_direction *= -1
    if ball_x > 1100:
        if player_2_y < ball_y + 23:
            if player_2_y + 146 > ball_y:
                ball_direction *= -1

    if ball_y > 680:
        ball_direction_y *= -1
    if ball_y <= 0:
        ball_direction_y *= -1

    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_direction_y *= -1
        ball_direction *= -1
        score_player_2 += 1
        score_player_2_img = pygame.image.load("assets/score/"+str(score_player_2)+".png")
    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_direction_y *= -1
        ball_direction *= -1
        score_player_1 += 1
        score_player_1_img = pygame.image.load("assets/score/"+str(score_player_1)+".png")


def player_movement():
    global player_1_y

    if player_1_moveup:
        player_1_y -= 10
    else:
        player_1_y -= 0

    if player_1_movedown:
        player_1_y += 10
    else:
        player_1_y += 0

    if player_1_y <= 0:
        player_1_y = 0
    elif player_1_y >= 575:
        player_1_y = 575

def player_2_movement():
    global player_2_y
    player_2_y = ball_y

    if player_2_y <= 0:
        player_2_y = 0
    elif player_2_y >= 575:
        player_2_y = 575


def draw():
    if score_player_1 or score_player_2 < 3:
        window.blit(field, (0, 0))
        window.blit(player_1, (player_1_x, player_1_y))
        window.blit(player_2, (player_2_x, player_2_y))
        window.blit(score_player_1_img, (500, 50))
        window.blit(score_player_2_img, (710, 50))
        window.blit(ball, (ball_x, ball_y))
        ball_movement()
        player_movement()
        player_2_movement()
    else:
        window.blit(win, (300, 330))



loop = True

while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player_1_moveup = True
            if events.key == pygame.K_s:
                player_1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player_1_moveup = False
            if events.key == pygame.K_s:
                player_1_movedown = False

    draw()


    pygame.display.update()