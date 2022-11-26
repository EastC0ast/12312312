import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('My Hommie Uses Clicker')
    clock = pygame.time.Clock()
    size = width, height = 650, 800
    center_of_window = width // 2, height // 2 # центр экрана
    top_of_window = width // 2, 35 # верх экрана
    bot_of_window = width // 2, 800  # верх экрана
    screen = pygame.display.set_mode(size) # создание окна
    screen_rect = screen.get_rect()
    font = pygame.font.match_font('Mont') # шрифт
    mont64 = pygame.font.Font(font, 64) # шрифт 64
    mont32 = pygame.font.Font(font, 32) # шрифт 32
    target_img = pygame.image.load('1st.png')
    background_image = pygame.image.load('background_img.png')
    running = True
    FPS = 60
    score = 000000

    while running:
        screen.blit(background_image, (0, 0))
        screen.blit(target_img, (80, 235))
        text = mont64.render(f'Кол-во очков {score}', True, (255, 255, 255))
        place = text.get_rect(center = top_of_window)
        screen.blit(text, place)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if screen_rect.collidepoint(event.pos):
                    score += 1


        clock.tick(FPS)
