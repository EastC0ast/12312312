import sqlite3

import pygame


class Game:

    def __init__(self):
        self.con = sqlite3.connect("data.sqlite")
        cur = self.con.cursor()
        sqlite_select_query = """SELECT * from data"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()

        self.game_exit = False
        self.COSTS = [25, 123, 828, 650, 5000]

        self.main_hero = pygame.image.load("img/hero.png")

        self.cursor = pygame.image.load("img/cursor.png")
        self.bed = pygame.image.load("img/bed.png")
        self.chem = pygame.image.load("img/chem.png")
        self.levelup = pygame.image.load("img/lvlup.png")
        self.endlogo = pygame.image.load("img/end.png")

        self.bgs = [
            pygame.image.load("img/background.png"),
            pygame.image.load("img/background1.png"),
            pygame.image.load("img/background2.png"),
        ]
        self.heroes = [
            pygame.image.load("img/hero.png"),
            pygame.image.load("img/hero1.png"),
            pygame.image.load("img/hero2.png"),
        ]

        self.blink_hero = [
            pygame.image.load("img/hero.png"),
            pygame.image.load("img/hero_1.png"),
        ]

        self.blink_hero1 = [
            pygame.image.load("img/hero1.png"),
            pygame.image.load("img/hero1_1.png"),
        ]

        self.score = records[0][0]
        self.level = records[0][1]

        self.cursors = records[0][3]
        self.beds = records[0][2]
        self.chems = records[0][4]

        self.counter = records[0][5]
        self.player_anim_count = 0

        self.prev_count_cursor = records[0][6]
        self.prev_count_bed = records[0][7]
        self.prev_count_chem = records[0][8]
        cur.close()
        self.game_display = pygame.display.set_mode((800, 500))
        pygame.mixer.init(44100, -16, 2, 2048)
        self.bg_sound = pygame.mixer.Sound('sound/Sugar-Lime.mp3')
        pygame.display.set_caption('Little-Clicker v2.0')

    def update(self):
        cur = self.con.cursor()
        try:
            sqlite_update_query = """UPDATE data SET score = ?, lvl = ?, cursors = ?, beds = ?, chems = ?, counter = 
            ?, prev_count_cursor = ?, prev_count_bed = ?, prev_count_chem = ? """
            column_values = (self.score, self.level, self.cursors, self.beds, self.chems, self.counter,
                             self.prev_count_cursor, self.prev_count_bed, self.prev_count_chem)
            cur.execute(sqlite_update_query, column_values)
            self.con.commit()
        except:
            print('error')
            self.con.rollback()
        cur.close()

    def process_mouse(self, event):
        from menu import Menu
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.main_hero.get_rect().move((10, 50)).collidepoint(pos):
                self.score += 1
                self.player_anim_count += 1
                if self.player_anim_count == 2:
                    self.player_anim_count = 0
            elif self.cursor.get_rect().move((600, 40)).collidepoint(pos):
                if self.score >= self.COSTS[0]:
                    if self.cursors < 1242:
                        self.score -= self.COSTS[0]
                        self.cursors += 1
                        self.COSTS[0] += 8
            elif self.bed.get_rect().move((600, 70)).collidepoint(pos):
                if self.score >= self.COSTS[1]:
                    if self.beds < 1242:
                        self.score -= self.COSTS[1]
                        self.beds += 1
                        self.COSTS[1] += 13
            elif self.chem.get_rect().move((600, 110)).collidepoint(pos):
                if self.score >= self.COSTS[2]:
                    if self.chems < 1242:
                        self.score -= self.COSTS[2]
                        self.chems += 1
                        self.COSTS[2] += 190
            elif self.level <= 1:
                if self.levelup.get_rect().move((600, 150)).collidepoint(pos):
                    if self.score >= self.COSTS[3]:
                        if self.level < 1242:
                            self.score -= self.COSTS[3]
                            self.level += 1
                            self.COSTS[3] += 800
            elif self.endlogo.get_rect().move((600, 150)).collidepoint(pos):
                if self.score >= self.COSTS[4]:
                    if self.level < 1242:
                        self.score -= self.COSTS[4]
                        self.score, self.level, self.cursors, self.beds, self.chems, \
                        self.counter, self.prev_count_chem, self.prev_count_bed, self.prev_count_cursor = (0 for _ in
                                                                                                           range(9))
                        self.bg_sound.stop()
                        self.update()
                        menu = Menu('Play Again')
                        menu.start_menu()
        elif event.type == pygame.KEYDOWN and event.type != pygame.KEYUP:
            if event.key == pygame.K_9:
                self.score += 1000

    def draw_text(self, fontsize, text, coord):
        font = pygame.font.match_font('Mont')
        font = pygame.font.Font(font, fontsize)
        text_image = font.render(text, True, (255, 255, 255))
        self.game_display.blit(text_image, coord)

    def draw_texts(self):

        self.draw_text(45, "Points: " + str(self.score), (70, 0))

        self.draw_text(45, "Market:", (640, 0))
        self.draw_text(37, "Cursor " + str(self.COSTS[0]) + " p.", (640, 40))
        self.draw_text(37, "Bed " + str(self.COSTS[1]) + " p.", (640, 80))
        self.draw_text(37, "Chem " + str(self.COSTS[2]) + " p.", (640, 120))
        if self.level <= 1:
            self.draw_text(37, "LvlUp " + str(self.COSTS[3]) + " p.", (640, 160))
        if self.level > 1:
            self.draw_text(37, "EndGame " + str(self.COSTS[4]) + " p.", (600, 160))
        self.draw_text(37, str(self.cursors) + " PPS", (50, 326))
        self.draw_text(37, str(self.beds * 5) + " PPS", (58, 380))
        self.draw_text(37, str(self.chems * 10) + " PPS", (58, 435))
        self.draw_text(37, str(self.level) + "th Level", (640, 400))

    def draw_shop(self):
        self.game_display.blit(self.cursor, (600, 40))
        self.game_display.blit(self.bed, (600, 70))
        self.game_display.blit(self.chem, (600, 110))
        if self.level <= 1:
            self.game_display.blit(self.levelup, (600, 150))
        if self.level > 1:
            self.game_display.blit(self.endlogo, (570, 155))

    def draw_improvements(self):
        self.game_display.blit(self.cursor, (16, 326))
        self.game_display.blit(self.bed, (12, 368))
        self.game_display.blit(self.chem, (12, 432))

    def change_hero(self):
        if self.level == 0:
            self.game_display.blit(self.blink_hero[self.player_anim_count], (8, 62))
        elif self.level == 1:
            self.game_display.blit(self.blink_hero1[self.player_anim_count], (8, 62))
        elif self.level == 2:
            self.game_display.blit(self.heroes[self.level], (8, 62))

    def game_loop(self):
        self.game_exit = False
        self.bg_sound.play()
        clock = pygame.time.Clock()
        while not self.game_exit:
            for event in pygame.event.get():
                self.process_mouse(event)
                if event.type == pygame.QUIT:
                    exit()

            self.game_display.blit(self.bgs[self.level], (0, 0))

            self.change_hero()
            self.draw_shop()
            self.draw_improvements()
            self.draw_texts()

            self.counter += 1

            if self.counter >= 1000:
                self.counter = 0
                self.prev_count_cursor = 0
                self.prev_count_bed = 0
                self.prev_count_chem = 0
            if self.counter >= self.prev_count_cursor + 150:
                self.score += self.cursors
                self.prev_count_cursor = self.counter
            if self.counter >= self.prev_count_bed + 70:
                self.score += self.beds
                self.prev_count_bed = self.counter
            if self.counter >= self.prev_count_chem + 40:
                self.score += self.chems
                self.prev_count_chem = self.counter
            self.update()
            pygame.display.update()
            clock.tick(60)

    def draw_text(self, fontsize, text, coord):
        font = pygame.font.match_font('Mont')
        font = pygame.font.Font(font, fontsize)
        text_image = font.render(text, True, (255, 255, 255))
        self.game_display.blit(text_image, coord)

    def draw_texts(self):

        self.draw_text(45, "Points: " + str(self.score), (70, 0))

        self.draw_text(45, "Market:", (640, 0))
        self.draw_text(37, "Cursor " + str(self.COSTS[0]) + " p.", (640, 40))
        self.draw_text(37, "Bed " + str(self.COSTS[1]) + " p.", (640, 80))
        self.draw_text(37, "Chem " + str(self.COSTS[2]) + " p.", (640, 120))
        if self.level <= 1:
            self.draw_text(37, "LvlUp " + str(self.COSTS[3]) + " p.", (640, 160))
        if self.level > 1:
            self.draw_text(37, "EndGame " + str(self.COSTS[4]) + " p.", (600, 160))
        self.draw_text(37, str(self.cursors) + " PPS", (50, 326))
        self.draw_text(37, str(self.beds * 5) + " PPS", (58, 380))
        self.draw_text(37, str(self.chems * 10) + " PPS", (58, 435))
        self.draw_text(37, str(self.level) + "th Level", (640, 400))

    def draw_shop(self):
        self.game_display.blit(self.cursor, (600, 40))
        self.game_display.blit(self.bed, (600, 70))
        self.game_display.blit(self.chem, (600, 110))
        if self.level <= 1:
            self.game_display.blit(self.levelup, (600, 150))
        if self.level > 1:
            self.game_display.blit(self.endlogo, (570, 155))

    def draw_improvements(self):
        self.game_display.blit(self.cursor, (16, 326))
        self.game_display.blit(self.bed, (12, 368))
        self.game_display.blit(self.chem, (12, 432))

    def change_hero(self):
        if self.level == 0:
            self.game_display.blit(self.blink_hero[self.player_anim_count], (8, 62))
        elif self.level == 1:
            self.game_display.blit(self.blink_hero1[self.player_anim_count], (8, 62))
        elif self.level == 2:
            self.game_display.blit(self.heroes[self.level], (8, 62))

    def game_loop(self):
        self.game_exit = False
        self.bg_sound.play()
        clock = pygame.time.Clock()
        while not self.game_exit:
            for event in pygame.event.get():
                self.process_mouse(event)
                if event.type == pygame.QUIT:
                    exit()

            self.game_display.blit(self.bgs[self.level], (0, 0))

            self.change_hero()
            self.draw_shop()
            self.draw_improvements()
            self.draw_texts()


            self.counter += 1

            if self.counter >= 1000:
                self.counter = 0
                self.prev_count_cursor = 0
                self.prev_count_bed = 0
                self.prev_count_chem = 0
            if self.counter >= self.prev_count_cursor + 150:
                self.score += self.cursors
                self.prev_count_cursor = self.counter
            if self.counter >= self.prev_count_bed + 70:
                self.score += self.beds
                self.prev_count_bed = self.counter
            if self.counter >= self.prev_count_chem + 40:
                self.score += self.chems
                self.prev_count_chem = self.counter
            self.update()
            pygame.display.update()
            clock.tick(60)
