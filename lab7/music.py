import pygame
import os

pygame.init()

# Музыкальная папка
music_folder = "/Users/rgalbekovaaltynai/Documents/GitHub/sem2/lab7/musics"
playlist = [os.path.join(music_folder, song) for song in os.listdir(music_folder) if song.endswith(".mp3")]

# Настройка экрана
screen_width, screen_height = 602, 604
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ninety One")
clock = pygame.time.Clock()

# Фон и кнопки
assets_path = "/Users/rgalbekovaaltynai/Documents/GitHub/sem2/lab7/music-elements"
background = pygame.image.load(os.path.join(assets_path, "background.png"))
playb = pygame.image.load(os.path.join(assets_path, "play.png"))
pausb = pygame.image.load(os.path.join(assets_path, "pause.png"))
nextb = pygame.image.load(os.path.join(assets_path, "next.png"))
prevb = pygame.image.load(os.path.join(assets_path, "back.png"))

# Размеры кнопок
button_size = (70, 70)
playb = pygame.transform.scale(playb, button_size)
pausb = pygame.transform.scale(pausb, button_size)
nextb = pygame.transform.scale(nextb, button_size)
prevb = pygame.transform.scale(prevb, (75, 75))

# Панель для кнопок
panel_width, panel_height = 500, 150
panel_x = (screen_width - panel_width) // 2
panel_y = screen_height - panel_height - 20
bg = pygame.Surface((panel_width, panel_height))
bg.fill((255, 255, 255))

# Шрифт для текста
font2 = pygame.font.SysFont(None, 24)

# Центрирование кнопок
button_y = panel_y + 50
play_x = panel_x + (panel_width // 2) - 35
pause_x = play_x
next_x = play_x + 100
prev_x = play_x - 100

# Запуск музыки
index = 0
aplay = False
pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(1)
aplay = True 

# Основной цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    # Отрисовка элементов
    screen.blit(background, (0, 0))
    screen.blit(bg, (panel_x, panel_y))
    
    # Название песни
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    text_x = panel_x + (panel_width - text2.get_width()) // 2
    screen.blit(text2, (text_x, panel_y + 15))

    # Отрисовка кнопок
    screen.blit(prevb, (prev_x, button_y))
    screen.blit(nextb, (next_x, button_y))
    screen.blit(pausb if aplay else playb, (play_x, button_y))

    clock.tick(24)
    pygame.display.update()