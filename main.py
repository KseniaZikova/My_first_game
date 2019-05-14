import pygame


pygame.init()

display_width = 1000
display_height = 410

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Academ_Panter_Game')

icon = pygame.image.load('image_pa/icon.png')
pygame.display.set_icon(icon)

butt_music = pygame.mixer.Sound('music/button.wav')
pygame.mixer.music.load('music/background1.mp3')
pygame.mixer.music.set_volume(0.3)
oi_music = pygame.mixer.Sound('music/Bdish.wav')

pre_image = [pygame.image.load('image_pa/p02.png'),
             pygame.image.load('image_pa/p01.png'),
             pygame.image.load('image_pa/p02.png')]

stone_img = [pygame.image.load('image_pa/Stone0.png'),
             pygame.image.load('image_pa/Stone1.png'),
             pygame.image.load('image_pa/Stone0.png'),
             pygame.image.load('image_pa/Stone1.png')]

cloud_img = [pygame.image.load('image_pa/Cloud0.png'),
             pygame.image.load('image_pa/Cloud1.png'),
             pygame.image.load('image_pa/Cloud0.png'),
             pygame.image.load('image_pa/Cloud1.png')]

hero_img = [pygame.image.load('hero/1.png'),
            pygame.image.load('hero/2.png'),
            pygame.image.load('hero/3.png'),
            pygame.image.load('hero/4.png'),
            pygame.image.load('hero/5.png'),
            pygame.image.load('hero/6.png')]


img_counter = 0


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.activ_color = (255, 255, 255)


    def draw(self, x, y, txt, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.activ_color, (x, y, self.width, self.height))
            if click[0] == 1:
                pygame.mixer.Sound.play(butt_music)
                pygame.time.delay(300)
                if action is not None:
                    action()

        else:
            pygame.draw.rect(display, self.activ_color, (x, y, self.width, self.height))

            print_txt(txt=txt, x=x + 10, y=y + 10, font_size=font_size)




class Pregrada:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed


    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
        else:
            self.x = display_width - 50

    @staticmethod
    def draw_array(array):
        for pre in array:
            pre.move()

    def create_preg_arr(self):
        img = pre_image[0]
        width = 64
        height = 210
        self.append(Pregrada(display_width + 20, height, width, img, 4))

        img = pre_image[1]
        width = 60
        height = 222
        self.append(Pregrada(display_width + 250, height, width, img, 3.9))

        img = pre_image[2]
        width = 64
        height = 210
        self.append(Pregrada(display_width + 600, height, width, img, 4))



class Cloud_stone:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move_sab(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
        else:
            self.x = display_width - 50

    @staticmethod
    def draw_array_stone(array):
        for pre in array:
            pre.move_sab()

    def create_cloud_stone_arr(self):
        img = stone_img[0]
        width = 10
        height = 370
        self.append(Cloud_stone(display_width + 20, height, width, img, 3))

        img = stone_img[1]
        width = 10
        height = 390
        self.append(Cloud_stone(display_width + 200, height, width, img, 3))

        img = stone_img[2]
        width = 10
        height = 340
        self.append(Cloud_stone(display_width + 500, height, width, img, 3))

        img = stone_img[3]
        width = 10
        height = 370
        self.append(Cloud_stone(display_width + 700, height, width, img, 3))

        img = cloud_img[0]
        width = 10
        height = 30
        self.append(Cloud_stone(display_width + 20, height, width, img, 2))

        img = cloud_img[1]
        width = 10
        height = 70
        self.append(Cloud_stone(display_width + 300, height, width, img, 2))
        img = cloud_img[2]
        width = 10
        height = 50
        self.append(Cloud_stone(display_width + 600, height, width, img, 2))

        img = cloud_img[3]
        width = 10
        height = 100
        self.append(Cloud_stone(display_width + 800, height, width, img, 2))


panter_width = 10
panter_height = 90
panter_x = display_width // 3
panter_y = display_height - panter_height - 100

pr_1_width = 20
pr_1_height = 80
pr_1_x = display_width - 50
pr_1_y = display_height - pr_1_height - 100

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30

score_jump = 0
pregrad_sc = 0


def main():
    global make_jump

    pygame.mixer.music.play(-1)

    game = True
    preg_arr = []
    obj_arr = []
    Pregrada.create_preg_arr(preg_arr)
    Cloud_stone.create_cloud_stone_arr(obj_arr)
    lend = pygame.image.load('image_pa/back0.jpg')

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True
        if make_jump:
            jump()
        if keys[pygame.K_z]:
            mini_stop()

        scores_math(preg_arr)


        display.blit(lend, (0, 0))

        print_txt('Score: ' + str(score_jump), 70, 10)

        Pregrada.draw_array(preg_arr)
        Cloud_stone.draw_array_stone(obj_arr)

        draw_hero()

        if check_coll(preg_arr):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(oi_music)
            game = False

        pygame.display.update()
        clock.tick(80)

    return stop()


def jump():
    global panter_y, jump_counter, make_jump
    if jump_counter >= -30:
        if jump_counter == -28:
            pygame.mixer.Sound.play(oi_music)

        panter_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def draw_hero():
    global img_counter
    if img_counter == 30:
        img_counter = 0

    display.blit(hero_img[img_counter // 5], (panter_x, panter_y))
    img_counter += 1


def print_txt(txt, x, y, font_color=(0, 0, 0), font_type='font/PingPong.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(txt, True, font_color)
    display.blit(text, (x, y))


def mini_stop():
    pause = True
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_txt('Press Enter to continue', 340, 100)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pause = False

        pygame.display.update()
        clock.tick(20)
    pygame.mixer.music.unpause()


def check_coll(bars):
    for bar in bars:
        if panter_y + panter_height >= bar.y:
            if bar.x <= panter_x <= bar.x + bar.width:
                return True
            elif bar.x <= panter_x + panter_width <= bar.x + bar.width:
                return True
    return False


def stop():
    stopped = True

    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_txt('Game over', 440, 100)
        print_txt('Press Enter to play again', 350, 150)
        print_txt('Esc to exit', 430, 180)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        clock.tick(20)



def scores_math(bars):
    global score_jump, pregrad_sc

    if not pregrad_sc:
        for bar in bars:
            if bar.x <= panter_x + panter_width / 2 <= bar.x + bar.width:
                if panter_y + panter_height - 5 <= bar.y:
                    pregrad_sc = True
                    break
    else:
        if jump_counter == -30:
            score_jump += 1
            pregrad_sc = False


def menu():

    menu_back = pygame.image.load('image_pa/menu.jpg')
    pygame.mixer.music.play()

    start = Button(120, 50)
    name = Button(0, 0)
    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(menu_back, (0, 0))
        start.draw(460, 90, 'Start', start_game, 40)
        name.draw(290, 23, 'Academ_Panter Game', start_game, 50)
        pygame.display.update()
        clock.tick(60)


def start_game():
    global score_jump, make_jump, jump_counter, panter_y
    while main():
        score_jump = 0
        make_jump = False
        jump_counter = 30
        panter_y = display_height - panter_height - 100

menu()
pygame.quit()
quit()