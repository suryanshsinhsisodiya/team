import pygame
pygame.init()
win_width = 1100
win_height = 800
root = pygame.display.set_mode((win_width, win_height))


def display():
    root.fill('#222222')
    pygame.draw.rect(root, '#ffffff', player1, border_radius=12)
    pygame.draw.rect(root, '#ffffff', player2, border_radius=12)
    pygame.draw.rect(root, '#ffffff', ball, border_radius=10)
    pygame.display.update()


def main():
    global player1, player2, ball
    FPS = 60
    clock = pygame.time.Clock()
    block_width = 12
    block_height = 125
    ball_radius = 20
    ball_velocity_x = 7
    ball_velocity_y = 7
    player1 = pygame.Rect(10, 10, block_width, block_height)
    player2 = pygame.Rect(win_width - 22, 10, block_width, block_height)
    ball = pygame.Rect(win_width / 2 - 10, win_height /
                       2 - 10, ball_radius, ball_radius)
    while True:
        clock.tick(FPS)
        ball.x += ball_velocity_x
        ball.y += ball_velocity_y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.y > 10:
            player1.y -= 7
        if keys[pygame.K_s] and player1.y < win_height - player1.height:
            player1.y += 7
        if keys[pygame.K_UP] and player2.y > 10:
            player2.y -= 7
        if keys[pygame.K_DOWN] and player2.y < win_height - player2.height:
            player2.y += 7

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if ball.y <= 0 or ball.y >= win_height - ball.height:
            ball_velocity_y *= -1
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_velocity_x *= -1
        display()


main()
