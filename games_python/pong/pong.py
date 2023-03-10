import pygame
import os
pygame.init()
win_width = 1100
win_height = 700
root = pygame.display.set_mode((win_width, win_height))
try:
    os.chdir('games_python\\pong')
except:
    pass
theme = 'dark'
fg = '#cccccc'
bg = '#222222'


font = pygame.font.Font('assets\\pong_font.ttf', 64)


def display():
    root.fill(bg)
    pygame.draw.rect(root, fg, player1, border_radius=3)
    pygame.draw.rect(root, fg, player2, border_radius=3)
    pygame.draw.rect(root, fg, ball, border_radius=10)
    pygame.draw.rect(root, fg, seperator)
    root.blit(pygame.image.load(
        'assets\\{}_theme.png'.format(theme)), (15, 15))
    headfontrender = font.render(scoretext, True, fg)
    headtext_x = (1100 - headfontrender.get_size()[0])//2
    root.blit(headfontrender, (headtext_x, 8))
    pygame.display.update()


def reset_score():
    global p1_score, p2_score
    p1_score = 0
    p2_score = 0


def main():
    global player1, player2, ball, fg, bg, themerect, seperator, p1_score, p2_score, theme, scoretext
    FPS = 60
    clock = pygame.time.Clock()
    block_width = 12
    block_height = 140
    ball_radius = 20
    MAX_VEL = 7
    velocity_increment_frame = 0
    ball_velocity_x = MAX_VEL
    ball_velocity_y = 0
    player1 = pygame.Rect(10, 320, block_width, block_height)
    player2 = pygame.Rect(win_width - 22, 320, block_width, block_height)
    ball = pygame.Rect(win_width / 2 - 10, win_height /
                       2 + 25, ball_radius, ball_radius)
    seperator = pygame.Rect(0, 98, win_width, 2)
    gameover = False
    while not gameover:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        velocity_increment_frame += 1
        if velocity_increment_frame == 1000:
            MAX_VEL += 1
            velocity_increment_frame = 0
        scoretext = f'{p1_score} - {p2_score}'

        if ball.x <= 0:
            p2_score += 1
            main()
        if ball.x >= win_width - ball.width:
            p1_score += 1
            main()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.y > 110:
            player1.y -= 7
        if keys[pygame.K_s] and player1.y < win_height - player1.height - 10:
            player1.y += 7
        if keys[pygame.K_UP] and player2.y > 110:
            player2.y -= 7
        if keys[pygame.K_DOWN] and player2.y < win_height - player2.height - 10:
            player2.y += 7

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and 19 < mouse[0] < 83 and 19 < mouse[1] < 83:
                if theme == 'light':
                    theme, bg, fg = 'dark', '#222222', '#cccccc'
                elif theme == 'dark':
                    theme, bg, fg = 'light', '#cccccc', '#222222'
        ball.x += ball_velocity_x
        ball.y += ball_velocity_y

        if ball.y <= 100:
            ball.y += 10
            ball_velocity_y *= -1
        if ball.y >= win_height - ball.height:
            ball.y = win_height - ball.height
            ball_velocity_y *= -1
        if ball.colliderect(player1):
            ball_velocity_x *= -1
            middle_y = player1.y + player1.height / 2
            difference_in_y = middle_y - ball.y
            reduction_factor = (block_height / 2) / MAX_VEL
            velocity_y = difference_in_y / reduction_factor
            ball_velocity_y = -velocity_y
        if ball.colliderect(player2):
            ball_velocity_x *= -1
            middle_y = player2.y + player2.height / 2
            difference_in_y = middle_y - ball.y
            reduction_factor = (block_height / 2) / MAX_VEL
            velocity_y = difference_in_y / reduction_factor
            ball_velocity_y = -velocity_y

        if (19 < mouse[0] < 83 and 19 < mouse[1] < 83):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        display()
        if p1_score == 5:
            postgame('Player 1')
        if p2_score == 5:
            postgame('Player 2')


def postgame(winner):
    print(winner)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


reset_score()
main()
