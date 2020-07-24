

import pygame
import random

pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 300
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#background image
bgimg = pygame.image.load("bg.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("SnakesByKrishna")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snkList, snake_size):
    for x,y in snkList:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((23, 50, 10))
        text_screen("Welcome to ", black, 20, 200)
        text_screen("Snakes", black, 20, 240)
        text_screen("Press Space ", black, 20, 280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameLoop()
        pygame.display.update()

# Game Loop
def gameLoop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snkList = []
    snkLength = 1
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 20
    fps = 60

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game over!", red, 50, 200)
            text_screen("press enter to", red, 20, 300)
            text_screen("Continue", red, 50, 350)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snkLength += 5

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snkList.append(head)

            if len(snkList) > snkLength:
                del snkList[0]

            if head in snkList[:-1]:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                game_over = True

            if snake_x<0 or snake_x>screen_height or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                game_over= True

            plot_snake(gameWindow, black, snkList, snake_size)
            text_screen("Score: " + str(score), (55,75,50), 5, 5)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

