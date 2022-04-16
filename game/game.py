#!/usr/bin/python
# -*- coding: latin-1 -*-
#                      Some explanations

#  pop_axes - is a variable which creates "timer" for appearance fertilizer bag
#  in right side of screen, in every thirty axes appearance one bag

# buff from water (increase speed) ends when new water appearance on screen
import pygame

from modules import *
from sprites import *

pygame.init()

from levels import *

win = pygame.display.set_mode((500, 500))  # Specifies the expansion of the game window
pygame.display.set_caption('Tree game')  # Title

save_info = Save()
if not save_info.file['value']:
    save_info.max_score = 0
    save_info.file['value'] = True

# list of items
drops = []
woods = []
axes = []
bags = []
flowers = []
variables = []

x = 210  # main character
y = 395  # position

width = 80  # character's width
height = 70  # and height

left = False  # he looks at you
right = False  # when game starts

speed = 7  # character's speed
score = 0
score_lev = 0

boolJump = False  # he doesn't jump when game starts

jumpCount = 11  # jump coefficient
j = 19  # something like gravity when the jump is over and the character
# fell, but not completely

animCount = 0
animMenu = 0

pop_axes = 0
var = 0

clock = pygame.time.Clock()


# levels funcs
def level1():
    global score_lev
    score_lev = 0
    game()


def level2():
    global score_lev
    score_lev = 200
    game()


def level3():
    global score_lev
    score_lev = 450
    game()


def level4():
    global score_lev
    score_lev = 750
    game()


def level5():
    global score_lev
    score_lev = 1100
    game()


# func to draw choose level menu
def draw_choose_level():
    global score, score_lev, animMenu
    while True:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            draw_menu()

        if keys[pygame.K_ESCAPE]:
            score = 0
            score_lev = 0
            pygame.quit()
            quit()

        if keys[pygame.K_f]:
            game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if animMenu + 1 >= 60:
            animMenu = 0
        win.blit(an_menu[round(animMenu // 2)], (0, 0))
        animMenu += 0.2

        print_text('WOODY WOOO', 40, 30, (0, 0, 0), 30)
        print_text('CHOOSE LEVEL', 40, 75, (0, 0, 0), 30)

        button_start1 = Button(108, 52)
        button_start2 = Button(108, 52)
        button_start3 = Button(108, 52)
        button_start4 = Button(108, 52)
        button_start5 = Button(108, 52)
        button_back = Button(108, 52)

        if save_info.file['n_lev'] == 1:
            button_start1.draw(40, 130, 45, 3, '1', 30, level1)

        elif save_info.file['n_lev'] == 2:
            button_start1.draw(40, 130, 45, 3, '1', 30, level1)
            button_start2.draw(40, 195, 45, 3, '2', 30, level2)

        elif save_info.file['n_lev'] == 3:
            button_start1.draw(40, 130, 45, 3, '1', 30, level1)
            button_start2.draw(40, 195, 45, 3, '2', 30, level2)
            button_start3.draw(40, 260, 45, 3, '3', 30, level3)

        elif save_info.file['n_lev'] == 4:
            button_start1.draw(40, 130, 45, 3, '1', 30, level1)
            button_start2.draw(40, 195, 45, 3, '2', 30, level2)
            button_start3.draw(40, 260, 45, 3, '3', 30, level3)
            button_start4.draw(40, 325, 45, 3, '4', 30, level4)

        elif save_info.file['n_lev'] >= 5:
            button_start1.draw(40, 130, 45, 3, '1', 30, level1)
            button_start2.draw(40, 195, 45, 3, '2', 30, level2)
            button_start3.draw(40, 260, 45, 3, '3', 30, level3)
            button_start4.draw(40, 325, 45, 3, '4', 30, level4)
            button_start5.draw(40, 390, 45, 3, '5', 30, level5)

        button_back.draw(335, 390, 18, 3, 'Back', 30, draw_menu)

        if keys[pygame.K_BACKSPACE]:
            draw_menu()

        pygame.display.update()


def draw_menu(message='WOODY WOOO', action=None, transition=None):
    global animMenu, score, score_lev, pop_axes, x, y, axes
    if action:
        action
    while True:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            score = 0
            score_lev = 0
            pygame.quit()
            quit()

        if keys[pygame.K_f]:
            game()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if animMenu + 1 >= 60:
            animMenu = 0
        win.blit(an_menu[round(animMenu // 2)], (0, 0))
        animMenu += 0.2

        if transition == 1:
            print_text(message, 40, 40, (0, 0, 0), 30)
            button_start = Button(200, 52)
            button_start.draw(40, 120, 22, 3, 'Next level', 30, game)

        elif transition == 2:
            button_start = Button(200, 52)
            button_quit = Button(200, 52)
            button_start.draw(40, 156, 33, 3, 'Continue', 30, game)

            button_quit.draw(40, 221, 70, 3, 'Quit', 30, quit)
            print_text("CONGRATULATIONS", 40, 40, (0, 0, 0), 30)
            print_text("YOU WON", 40, 80, (0, 0, 0), 30)

        else:
            button_start = Button(218, 52)
            button_choose_level = Button(218, 52)
            button_quit = Button(218, 52)
            button_start.draw(40, 120, 77, 3, 'Play', 30, game)
            button_choose_level.draw(40, 185, 10, 3, 'Choose level', 30, draw_choose_level)
            button_quit.draw(40, 250, 77, 3, 'Quit', 30, quit)
            print_text(message, 40, 40, (0, 0, 0), 30)


def draw_m_first_second():
    while True:
        button_next = Button(150, 52)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        global animMenu, score, score_lev, pop_axes, x, y, axes
        if animMenu + 1 >= 60:
            animMenu = 0
        win.blit(an_menu[round(animMenu // 2)], (0, 0))
        animMenu += 0.2

        button_next.draw(40, 120, 43, 3, 'Play', 30, game)


def check_collision(item):
    if (y + height >= item.y + item.width >= y + 33) or y + height > item.y > y:
        if item.x <= x <= item.x + item.width:
            return True
        elif item.x <= x + width <= item.x + item.width:
            return True
        elif x < item.x < x + width:
            return True
    else:
        return False


def game_over():
    for axe in axes:
        global speed, pop_axes, score_lev
        if check_collision(axe):
            pygame.mixer.Sound.play(death)
            global score
            if score > save_info.get('max_score'):
                save_info.add('max_score', score)
            max_score = save_info.get('max_score')
            paused = True
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                pygame.mixer_music.pause()
                print_text('Press F to pay respect or Esc to exit', 48, 100, (0, 0, 0), 20)
                print_text('Your max score is ' + str(max_score), 48, 150, (0, 0, 0), 20)

                save_level(score_lev, save_info)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    score = 0

                    if score_lev < 200:
                        score_lev = 0

                    elif score_lev < 450:
                        score_lev = 200

                    elif score_lev < 750:
                        score_lev = 450

                    elif score_lev < 1100:
                        score_lev = 750

                    elif score_lev < 1500:
                        score_lev = 1100

                    elif score_lev >= 1500:
                        score_lev = 1500

                    axes.clear()
                    woods.clear()
                    drops.clear()
                    bags.clear()
                    flowers.clear()
                    drops.append(Drop(random.randint(0, 440), -79, 55, 23, random.randint(5, 10)))
                    speed = 7
                    pop_axes = 0
                    pygame.mixer_music.play(-1)
                    break

                if keys[pygame.K_ESCAPE]:
                    score = 0
                    score_lev = 0
                    pygame.quit()
                    quit()

                pygame.display.update()


animPers = 0


# It draws items and a character
def Draw_Win(an_bg, an_state, an_right, an_left):
    global animCount

    draw_BG(an_bg)

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(an_left[round(animCount // 5)], (x, y))
        animCount += 1

    elif right:
        win.blit(an_right[round(animCount // 5)], (x, y))
        animCount += 1

    else:
        win.blit(an_state, (x, y))

    for wood in woods:
        wood.draw_wood()

    for axe in axes:
        axe.draw_axe()

    for drop in drops:
        drop.draw_drop()

    for bag in bags:
        bag.draw_bag()

    for flower in flowers:
        flower.draw_flower()

    print_text('Score: ' + str(score), 380, 10, (0, 0, 0), 20)

    pygame.display.update()  # updates screen


def game():

    pygame.mixer_music.play()

    while True:

        global pop_axes, boolJump, x, y, score, score_lev, speed, jumpCount, animCount, left, right, drops, an_bg
        global bags, an_state, an_left, an_right, axes, flowers, woods

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass

        if len(drops) < 1:
            drops.append(Drop(random.randint(0, 440), -990, 55, 23, 7))
        if len(woods) < 2:
            woods.append(Wood(random.randint(0, 440), -60, 60, 23, random.randint(5, 10)))
        if len(axes) < 3:
            axes.append(Axe(random.randint(0, 440), random.randint(-150, -75), 40, 35, random.randint(5, 10)))
        if len(flowers) < 1:
            flowers.append(Flower(random.randint(0, 440), -60, 64, 43, random.randint(5, 10)))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        save_level(score_lev, save_info)

        if score_lev < 200:
            first_level(pop_axes, bags, drops, woods, axes, flowers)

            an_bg = an_bg_1
            an_state = an_state1
            an_right = an_right1
            an_left = an_left1

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 15:
                x -= speed
                left = True
                right = False

            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and ((x < 270) or (x < 490 - width) and y < 360):
                x += speed
                right = True
                left = False

            else:
                left = False
                right = False
                animCount = 0

            if keys[pygame.K_SPACE]:
                boolJump = True

            if boolJump:
                if jumpCount >= 0:
                    y -= ((jumpCount ** 2) / 2)
                    jumpCount -= 1

                elif 0 > jumpCount >= -10:
                    if y < 360 and x > 270:
                        y += (jumpCount ** 2) / 2
                        jumpCount -= 1
                    boolJump = False
                    jumpCount = 10

            if x <= 270 and y < 390:
                y += j

            if x > 270 and y < 320:
                y += j

        elif score_lev < 450:
            if score == 200 or score == 201:
                score = 0
                score_lev = 200
                drops = []
                speed = 7
                axes = []
                flowers = []
                bags = []
                woods = []
                pop_axes = 0
                x = 210
                y = 395
                draw_menu(message='LEVEL 2', action=pygame.mixer_music.pause(), transition=1)

            second_level(pop_axes, bags, drops, woods, axes, flowers)

            an_bg = an_bg_2
            an_state = an_state1
            an_right = an_right1
            an_left = an_left1

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and ((x > 150) or (x > 7 and y < 360)):
                x -= speed
                left = True
                right = False

            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < 400:
                x += speed
                right = True
                left = False

            else:
                left = False
                right = False
                animCount = 0

            if keys[pygame.K_SPACE]:
                boolJump = True

            if boolJump:
                if jumpCount >= 0:
                    y -= ((jumpCount ** 2) / 2)
                    jumpCount -= 1

                elif 0 > jumpCount >= -10:
                    if y < 360 and x > 150:
                        y += (jumpCount ** 2) / 2
                        jumpCount -= 1
                    boolJump = False
                    jumpCount = 10

            if x <= 150 and y < 320:
                y += j

            if x > 150 and y < 390:
                y += j

        elif score_lev < 750:
            if score == 250 or score == 250:
                score = 0
                score_lev = 450
                drops = []
                speed = 7
                axes = []
                flowers = []
                bags = []
                woods = []
                pop_axes = 0
                x = 210
                y = 395
                draw_menu(message="LEVEL 3", action=pygame.mixer_music.pause(), transition=1)

            third_level(pop_axes, bags, drops, woods, axes, flowers)

            an_bg = an_bg_3
            an_state = an_state3
            an_right = an_right3
            an_left = an_left3

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 15:
                x -= speed
                left = True
                right = False

            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < 490 - width:
                x += speed
                right = True
                left = False

            else:
                left = False
                right = False
                animCount = 0

            if keys[pygame.K_SPACE]:
                boolJump = True

            if boolJump:
                if jumpCount >= 0:
                    y -= ((jumpCount ** 2) / 2)
                    jumpCount -= 1

                elif 0 > jumpCount >= -10:
                    if y < 360 and x > 270:
                        y += (jumpCount ** 2) / 2
                        jumpCount -= 1
                    boolJump = False
                    jumpCount = 10

            if y < 390:
                y += j

        elif score_lev < 1100:
            if score == 300 or score == 301:
                score = 0
                score_lev = 750
                drops = []
                speed = 7
                axes = []
                flowers = []
                bags = []
                woods = []
                pop_axes = 0
                x = 210
                y = 395
                draw_menu(message="LEVEL 4", action=pygame.mixer_music.pause(), transition=1)

            fourth_level(pop_axes, bags, drops, woods, axes, flowers)

            an_bg = an_bg_4
            an_state = an_state3
            an_right = an_right3
            an_left = an_left3

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 23:
                x -= speed
                left = True
                right = False

            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and ((x < 270) or (x < 490 - width) and y < 360):
                x += speed
                right = True
                left = False

            else:
                left = False
                right = False
                animCount = 0

            if keys[pygame.K_SPACE]:
                boolJump = True

            if boolJump:
                if jumpCount >= 0:
                    y -= ((jumpCount ** 2) / 2)
                    jumpCount -= 1

                elif 0 > jumpCount >= -10:
                    if y < 360 and x > 270:
                        y += (jumpCount ** 2) / 2
                        jumpCount -= 1
                    boolJump = False
                    jumpCount = 10

            if x <= 270 and y < 390:
                y += j

            if x > 270 and y < 320:
                y += j

        elif score_lev < 1500:
            if score == 350 or score == 351:
                score = 0
                score_lev = 1100
                drops = []
                axes = []
                flowers = []
                speed = 7
                bags = []
                woods = []
                pop_axes = 0
                x = 210
                y = 395
                draw_menu(message="LEVEL 5", action=pygame.mixer_music.pause(), transition=1)

            fifth_level(pop_axes, bags, drops, woods, axes, flowers)

            an_bg = an_bg_5
            an_state = an_state3
            an_right = an_right3
            an_left = an_left3

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and ((x > 150) or (x > 7 and y < 360)):
                x -= speed
                left = True
                right = False

            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < 400:
                x += speed
                right = True
                left = False

            else:
                left = False
                right = False
                animCount = 0

            if keys[pygame.K_SPACE]:
                boolJump = True

            if boolJump:
                if jumpCount >= 0:
                    y -= ((jumpCount ** 2) / 2)
                    jumpCount -= 1

                elif 0 > jumpCount >= -10:
                    if y < 360 and x > 150:
                        y += (jumpCount ** 2) / 2
                        jumpCount -= 1
                    boolJump = False
                    jumpCount = 10

            if x <= 150 and y < 320:
                y += j

            if x > 150 and y < 390:
                y += j

        elif score_lev >= 1500:
            if score == 400 or score == 401:
                score = 402
                score_lev = 1500
                drops = []
                axes = []
                flowers = []
                speed = 7
                bags = []
                woods = []
                pop_axes = 0
                x = 210
                y = 395
                draw_menu(action=pygame.mixer_music.pause(), transition=2)

            fifth_level(pop_axes, bags, drops, woods, axes, flowers)

            an_bg = an_bg_5
            an_state = an_state3
            an_right = an_right3
            an_left = an_left3

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and ((x > 150) or (x > 7 and y < 360)):
                x -= speed
                left = True
                right = False

            elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < 400:
                x += speed
                right = True
                left = False

            else:
                left = False
                right = False
                animCount = 0

            if keys[pygame.K_SPACE]:
                boolJump = True

            if boolJump:
                if jumpCount >= 0:
                    y -= ((jumpCount ** 2) / 2)
                    jumpCount -= 1

                elif 0 > jumpCount >= -10:
                    if y < 360 and x > 150:
                        y += (jumpCount ** 2) / 2
                        jumpCount -= 1
                    boolJump = False
                    jumpCount = 10

            if x <= 150 and y < 320:
                y += j

            if x > 150 and y < 390:
                y += j

        Draw_Win(an_bg, an_state, an_right, an_left)

        if keys[pygame.K_p]:
            pause()

        for wood in woods:

            if check_collision(wood):
                woods.pop(woods.index(wood))
                score += 1
                score_lev += 1

        for flower in flowers:

            if check_collision(flower):
                flowers.pop(flowers.index(flower))
                score += 2
                score_lev += 2

        for drop in drops:
            if check_collision(drop):
                drops = []
                speed = 10

        for drop in drops:
            if -60 < drop.y < 500:
                speed = 7

            if drop.speed == 0:
                drop.speed = 7
            if drop.y == -990 or drop.y == -79:
                drops.pop(drops.index(drop))
        game_over()
        pygame.display.update()
