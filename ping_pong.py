
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

paddle_width, paddle_height = 20, 100
ball_size = 20

player1 = pygame.Rect(30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

ball_speed_x, ball_speed_y = 4, 4
player_speed = 5

score1 = 0
score2 = 0

font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    if ball.right >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
