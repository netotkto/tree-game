import random
import shelve

from sounds import *
from sprites import *

animBG = 0
animFlower = 0
animAxe = 0
animWood = 0
animDrop = 0
animGrow = 0

win = pygame.display.set_mode((500, 500))  # Задается расширение окна игры

x = 210  # позиция главного
y = 395  # персонажа

width = 80  # его ширина
height = 70  # и высота


# Загружаются используемые спрайты
def choice_animation_axe():
    return random.choice(an_axe)


def choice_animation_wood():
    return random.choice(an_wood)


# OOП (классы предметов)
class Wood():
    def __init__(self, x, y, width, height, speed):
        global animWood
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.an = choice_animation_wood()

    def draw_wood(self):
        global animWood
        if animWood + 1 >= 28:
            animWood = 0
        win.blit(self.an[animWood // 7], (self.x, self.y))  # Умный алгоритм
        animWood += 1


class Axe():
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.an = choice_animation_axe()

    def draw_axe(self):
        global animAxe
        if animAxe + 1 >= 30:
            animAxe = 0
        win.blit(self.an[round(animAxe // 5)], (self.x, self.y))  # Умный алгоритм
        animAxe += 0.3


class Drop():
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def draw_drop(self):
        global animDrop
        if animDrop + 1 >= 28:
            animDrop = 0
        win.blit(an_drop[animDrop // 7], (self.x, self.y))  # Умный алгоритм
        animDrop += 1


class Grow_Up():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_bag(self):
        global animGrow
        if animGrow + 1 >= 30:
            animGrow = 0
        win.blit(an_bag[animGrow // 15], (self.x, self.y))  # Умный алгоритм
        animGrow += 1


class Flower():
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def draw_flower(self):
        global animFlower
        if animFlower + 1 >= 18:
            animFlower = 0
        win.blit(an_flower[round(animFlower // 6)], (self.x, self.y))  # Умный алгоритм
        animFlower += 0.18


def draw_BG(an_bg):
    global animBG
    if animBG + 1 >= 32:
        animBG = 0
    win.blit(an_bg[round(animBG // 2)], (0, 0))
    animBG += 0.3


class Button():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active_color = (158, 194, 200)
        self.inactive_color = (178, 219, 225)

    def draw(self, x, y, xt, yt, message, font_size, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(win, self.active_color, (x, y, self.width, self.height))
            print_text(message, x + xt, y + yt, (0, 0, 0), font_size)
            if click[0] == 1:
                pygame.mixer.Sound.play(click_button)
                pygame.time.delay(200)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    action()
        else:
            pygame.draw.rect(win, self.inactive_color, (x, y, self.width, self.height))
            print_text(message, x + xt, y + yt, (0, 0, 0), font_size)


class Save():
    def __init__(self):
        self.file = shelve.open('information')
        self.file['value'] = False

    def add(self, name, value):
        self.file[name] = value

    def get(self, name):
        try:
            return self.file[name]
        except KeyError:
            print(0)

    def __del__(self):
        self.file.close()


def print_text(message, x, y, font_color, font_size, font_type='fonts/font.ttf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    win.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.mixer_music.pause()
        print_text('Pause! Press Enter to play', 38, 100, (0, 0, 0), 30)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pygame.mixer_music.play(-1)
            break

        pygame.display.update()


def save_level(value, save_info):
    if value < 200:

        if save_info.file['n_lev'] < 2:
            save_info.add('n_lev', 1)

        elif value < 450:

            if save_info.file['n_lev'] < 3:
                save_info.add('n_lev', 2)

        elif value < 750:

            if save_info.file['n_lev'] < 4:
                save_info.add('n_lev', 3)

        elif value < 1100:

            if save_info.file['n_lev'] < 5:
                save_info.add('n_lev', 4)

        elif value < 1500:

            if save_info.file['n_lev'] < 6:
                save_info.add('n_lev', 5)
