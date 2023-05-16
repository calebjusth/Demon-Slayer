import pygame
import random
import sys

# initialize pygame
pygame.init()

# music
pygame.mixer.init()
hit_sound = pygame.mixer.Sound('audio/game-explosion.wav')


# initialize music module
pygame.mixer.music.load('audio/war.mp3') #music goes here
pygame.mixer.music.play(-1)

# set up the game window
screen_width = 860
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fall flame")

# set up the player sprite
player_img = pygame.image.load("img/player.png")
player_width = 90
player_height = 90
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_img = pygame.transform.scale(player_img, (player_height, player_width))


# set up the bullet sprite
bullet_img = pygame.image.load("img/bullet.png")
bullet_width = 50
bullet_height = 50
bullet_speed = 10
bullet_img = pygame.transform.scale(bullet_img, (bullet_height, bullet_width))


# set up the enemy sprite
enemy_img = pygame.image.load("img/enemy.png")
enemy_width = 90
enemy_height = 90
enemy_speed = 5
enemy_img = pygame.transform.scale(enemy_img, (enemy_height, enemy_width))
# set up the score and font
score = 0
font = pygame.font.Font(None, 36)

# set up the clock
clock = pygame.time.Clock()

# defining
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = -enemy_height

# set up the game loop
game_running = True

while game_running:
    # handle events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # create a new bullet sprite when spacebar is pressed
                bullet_x = player_x + player_width / 2 - bullet_width / 2
                bullet_y = player_y - bullet_height
                bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)


    # move the player sprite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    elif keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += 5

    # move the bullet sprite
    if 'bullet_rect' in locals():
        bullet_y -= bullet_speed
        bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)

    # move the enemy sprite
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = -enemy_height

    # check for collision with bullet sprite
    if 'bullet_rect' in locals() and bullet_rect.colliderect(enemy_rect):
        score += 1
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = -enemy_height
        del bullet_rect
        hit_sound.play()
    # check for collision with player sprite
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if player_rect.colliderect(enemy_rect):
        game_running = False

    # draw the sprites and score
    screen.fill((255, 255, 255))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    if 'bullet_rect' in locals():
        screen.blit(bullet_img, (bullet_x, bullet_y))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # update the display
    pygame.display.flip()

    # set the game speed
    clock.tick(60)

# quit pygame
pygame.mixer.quit()
pygame.quit()