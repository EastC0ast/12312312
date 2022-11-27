import pygame
import pygame_widgets
from pygame_widgets.button import Button

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('My Hommie Uses Clicker')
    clock = pygame.time.Clock()
    size = width, height = 650, 800
    center_of_window = width // 2, height // 2
    top_of_window = width // 2, 35
    bot_of_window = width // 2, 800
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    score = 0


    def but():
        global ingame
        ingame = False
        print('Clicked!')


    button = Button(
        screen,
        550,
        10,
        90,
        45,

        text='Магазин',
        fontSize=30,
        margin=20,
        radius=5,
        onClick=lambda: but()
    )
    screen_rect = screen.get_rect()
    font = pygame.font.match_font('Mont')
    mont64, mont32 = pygame.font.Font(font, 64), pygame.font.Font(font, 32)
    target_img, target2_img, target3_img = pygame.image.load('1st.png'), pygame.image.load(
        '2nd.png'), pygame.image.load('3rd.png')
    background_image = pygame.image.load('background_img.png')
    lvl_img, lvl2_img = pygame.image.load('lvl.png'), pygame.image.load('1lvl.png')
    lvl_img, lvl2_img = pygame.transform.scale(lvl_img, (250, 283)), pygame.transform.scale(lvl2_img, (250, 283))
    lvl_img_rect = lvl_img.get_rect()
    running = True
    FPS = 60
    level = 0
    ingame = True
    while running:
        screen.blit(background_image, (0, 0))
        if level == 0 or level == 2:
            screen.blit(lvl_img, (0, 40))
            if level == 0:
                screen.blit(target_img, (80, 235))
            else:
                screen.blit(target3_img, (80, 235))
        elif level == 1:
            screen.blit(lvl2_img, (0, 40))
            screen.blit(target2_img, (80, 235))
        text = mont64.render(f'Кол-во очков {score}', True, (255, 255, 255))
        place = text.get_rect(center=top_of_window)
        screen.blit(text, place)
        events = pygame.event.get()
        pygame_widgets.update(events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ingame:
                if screen_rect.collidepoint(event.pos):
                    if level == 0:
                        score += 1
                    elif level == 1:
                        score += 2
                    elif level == 2:
                        score += 4
                    elif level == 3:
                        score += 8
                    elif level == 4:
                        score += 16
                    elif level == 5:
                        score += 32
                if lvl_img_rect.collidepoint(event.pos):
                    if score >= 100:
                        if level == 0:
                            level += 1
                            score -= 100
                        if score >= 500:
                            if level == 1:
                                level += 1
                                score -= 500
                            if score >= 1000:
                                if level == 2:
                                    level += 0
                                    score -= 1000
        clock.tick(FPS)
        pygame.display.update()
