import pygame, random, openpyxl

pygame.init()
WIDTH, HEIGHT = 360, 600
COR = (156, 195, 151)
# -------------------------
DOG1_SIZE = 100
DOG2_SIZE = 80
POOP_SIZE = 85
POOP_SPEED = 10
SCORE_POOP_SIZE = 50
# -------------------------
CAT1_SIZE = 115
CAT2_SIZE = 80
BATHTUB_SIZE = 120
BATHTUB_SPEED = 10
SCORE_BATHTUB_SIZE = 50
# -------------------------
GATOR1_SIZE = 115
GATOR2_SIZE = 80
ANVIL_SIZE = 80
ANVIL_SPEED = 10
SCORE_ANVIL_SIZE = 50
# -------------------------
DINIS_SIZE = 90
PICO_SIZE = 100
PICO_SPEED = 10
SCORE_PICO_SIZE = 50
BONUS_SIZE1 = 120
BONUS_SIZE2 = 100
# -------------------------
dog1_img = pygame.image.load("dogpixel.png")
dog1_img = pygame.transform.scale(dog1_img, (DOG1_SIZE, DOG1_SIZE))
dog1_mask = pygame.mask.from_surface(dog1_img)
dog2_img = pygame.image.load("dogpixel.png")
dog2_img = pygame.transform.scale(dog2_img, (DOG2_SIZE, DOG2_SIZE))
dog2_mask = pygame.mask.from_surface(dog2_img)
poop_img = pygame.image.load("pooppixel.png")
poop_img = pygame.transform.scale(poop_img, (POOP_SIZE, POOP_SIZE))
poop_mask = pygame.mask.from_surface(poop_img)
score_poop_img = pygame.image.load("pooppixel.png")
score_poop_img = pygame.transform.scale(score_poop_img, (SCORE_PICO_SIZE, SCORE_PICO_SIZE))
# -------------------------------------------------------------------------------------------------
cat1_img = pygame.image.load("catpixel.png")
cat1_img = pygame.transform.scale(cat1_img, (CAT1_SIZE, CAT1_SIZE))
cat1_mask = pygame.mask.from_surface(cat1_img)
cat2_img = pygame.image.load("catpixel.png")
cat2_img = pygame.transform.scale(cat2_img, (CAT2_SIZE, CAT2_SIZE))
cat2_mask = pygame.mask.from_surface(cat2_img)
btt_img = pygame.image.load("bathtubpixel.png")
btt_img = pygame.transform.scale(btt_img, (BATHTUB_SIZE, BATHTUB_SIZE))
btt_mask = pygame.mask.from_surface(btt_img)
score_btt_img = pygame.image.load("bathtubpixel.png")
score_btt_img = pygame.transform.scale(score_btt_img, (SCORE_BATHTUB_SIZE, SCORE_BATHTUB_SIZE))
# -------------------------------------------------------------------------------------------------
dinis_img = pygame.image.load("headshotdinis.png")
dinis_img = pygame.transform.scale(dinis_img, (DINIS_SIZE, DINIS_SIZE))
dinis_mask = pygame.mask.from_surface(dinis_img)
pico_img = pygame.image.load("headshotpico.png")
pico_img = pygame.transform.scale(pico_img, (PICO_SIZE, PICO_SIZE))
pico_mask = pygame.mask.from_surface(pico_img)
score_pico_img = pygame.image.load("headshotpico.png")
score_pico_img = pygame.transform.scale(score_pico_img, (SCORE_PICO_SIZE, SCORE_PICO_SIZE))
# -------------------------------------------------------------------------------------------------
gator1_img = pygame.image.load("gatorpixel.png")
gator1_img = pygame.transform.scale(gator1_img, (GATOR1_SIZE, GATOR1_SIZE))
gator1_mask = pygame.mask.from_surface(gator1_img)
gator2_img = pygame.image.load("gatorpixel.png")
gator2_img = pygame.transform.scale(gator2_img, (GATOR2_SIZE, GATOR2_SIZE))
gator2_mask = pygame.mask.from_surface(gator2_img)
anvil_img = pygame.image.load("anvilpixel.png")
anvil_img = pygame.transform.scale(anvil_img, (ANVIL_SIZE, ANVIL_SIZE))
anvil_mask = pygame.mask.from_surface(anvil_img)
score_anvil_img = pygame.image.load("anvilpixel.png")
score_anvil_img = pygame.transform.scale(score_anvil_img, (SCORE_ANVIL_SIZE, SCORE_ANVIL_SIZE))
# -------------------------------------------------------------------------------------------------
bonus_img = pygame.image.load("bonus.png")
bonus_img = pygame.transform.scale(bonus_img, (BONUS_SIZE1, BONUS_SIZE2))
bonus_mask = pygame.mask.from_surface(bonus_img)
# -------------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(dog1_img)
pygame.display.set_caption("Animal Dodge Game")
screen.fill(COR)
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
game_running = True
game_over = False
user_name = ""
# -------------------------------------------------------------------------------------------------
def pontuação_excel(user_name, game_type, score):
    if user_name == "":
        user_name = "Anónimo"
    try:
        workbook = openpyxl.load_workbook('Pontuações ADG.xlsx')
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
    livro = workbook.active
    row_number = 2
    while livro.cell(row=row_number, column=1).value is not None:
        row_number += 1
    livro.cell(row=row_number, column=1, value=user_name)
    livro.cell(row=row_number, column=2, value=game_type)
    livro.cell(row=row_number, column=3, value=score)
    workbook.save("Pontuações ADG.xlsx")
# -------------------------------------------------------------------------------------------------
def ir_menu():
    global game_running, game_over, user_name, user_name_box, user_name_intro, user_name_name, event
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    if len(user_name) < 10:
                        user_name += event.unicode
        screen.fill(COR)
        user_name_intro = font.render("Nome do Jogador", True, (0,0,0))
        screen.blit(user_name_intro, (80,40))
        user_name_box = pygame.draw.rect(screen, (225,225,225), (38,70,285,46))
        user_name_name = font.render(user_name, True, (0,0,0))
        screen.blit(user_name_name, (user_name_box.x+5,user_name_box.y+12))
        pygame.draw.rect(screen, (156, 195, 151), (38,180,120,120))
        screen.blit(dog1_img, (50,190))
        pygame.draw.rect(screen, (156, 195, 151), (197,180,120,120))
        screen.blit(cat1_img, (200,182))
        pygame.draw.rect(screen, (156, 195, 151), (38,380,120,120))
        screen.blit(gator1_img, (40,380))
        pygame.draw.rect(screen, (156, 195, 151), (197,380,120,120))
        screen.blit(bonus_img, (199,390))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 38 < x < 38 + 120 and 180 < y < 180 + 120:
                game_over = False
                play_dog()
            elif 197 < x < 197 + 120 and 180 < y < 180 + 120:
                game_over = False
                play_cat()
            elif 38 < x < 38 + 120 and 380 < y < 380 + 120:
                game_over = False
                play_gator()
            if 197 < x < 197 + 120 and 380 < y < 380 + 120:
                game_over = False
                play_bonus()
        pygame.display.update()
# -------------------------------------------------------------------------------------------------
def play_dog():
    global DOG2_SIZE, POOP_SIZE, POOP_SPEED, SCORE_POOP_SIZE, dog_x, dog_y, poop_x, poop_y, score, event
    def play_again_dog():
        global DOG2_SIZE, POOP_SIZE, POOP_SPEED, SCORE_POOP_SIZE, dog_x, dog_y, poop_x, poop_y, score, event
        DOG2_SIZE = 80
        POOP_SIZE = 90
        POOP_SPEED = 10
        SCORE_POOP_SIZE = 50
        dog_x = WIDTH // 2 - DOG2_SIZE // 2
        dog_y = HEIGHT - DOG2_SIZE - 10
        poop_x = random.randint(0, WIDTH - POOP_SIZE)
        poop_y = -POOP_SIZE
        score = 0
    play_again_dog()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    COR_DOG = (87,169,242)
    game_running = True
    game_over = False
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dog_x > 0:
            dog_x -= 5
        if keys[pygame.K_RIGHT] and dog_x < WIDTH - DOG2_SIZE:
            dog_x += 5
        poop_y += POOP_SPEED
        if poop_y > HEIGHT:
            poop_y = -POOP_SIZE
            poop_x = random.randint(0, WIDTH - POOP_SIZE)
            POOP_SPEED += 0.3
            score += 1
        offset = (poop_x - dog_x, poop_y - dog_y)
        collision = dog2_mask.overlap(poop_mask, offset)
        if collision:
            print("\n\033[91mGAME OVER!\033[0m \033[1mScore:\033[0m", score)
            pontuação_excel(user_name, "Cão", score)
            game_over = True
        screen.fill(COR_DOG)
        screen.blit(dog2_img, (dog_x, dog_y))
        screen.blit(poop_img, (poop_x, poop_y))
        screen.blit(score_poop_img, (20,20))
        font = pygame.font.Font(None, 45)
        score_text = font.render(": " +str(score), True, (0, 0, 0))
        screen.blit(score_text, (70, 35))
        menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
        font = pygame.font.Font(None, 25)
        text = font.render("MENU", True, (0,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                ir_menu()
        screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        if game_over:
            pygame.draw.circle(screen, (226,49,52), (180,300), 75)
            font = pygame.font.Font(None, 45)
            text = font.render("RETRY", True, (225,225,225))
            text_circle = text.get_rect(center=(180, 300))
            screen.blit(text, text_circle)
            menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
            font = pygame.font.Font(None, 25)
            text = font.render("MENU", True, (0,0,0))
            screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        pygame.display.flip()
        clock.tick(60)
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_over = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 130 < x < 130 + 100 and 250 < y < 250 + 100:
                        game_over = False
                        play_again_dog()
                    if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                        ir_menu()
# -------------------------------------------------------------------------------------------------
def play_cat():
    global CAT2_SIZE, BATHTUB_SIZE, BATHTUB_SPEED, SCORE_BATHTUB_SIZE, cat_x, cat_y, btt_x, btt_y, score, event
    def play_again_cat():
        global CAT2_SIZE, BATHTUB_SIZE, BATHTUB_SPEED, SCORE_BATHTUB_SIZE, cat_x, cat_y, btt_x, btt_y, score, event
        CAT2_SIZE = 80
        BATHTUB_SIZE = 90
        BATHTUB_SPEED = 10
        SCORE_BATHTUB_SIZE = 50
        cat_x = WIDTH // 2 - CAT2_SIZE // 2
        cat_y = HEIGHT - CAT2_SIZE - 10
        btt_x = random.randint(0, WIDTH - BATHTUB_SIZE)
        btt_y = -BATHTUB_SIZE
        score = 0
    play_again_cat()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    COR_CAT = (87,169,242)
    game_running = True
    game_over = False
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and cat_x > 0:
            cat_x -= 5
        if keys[pygame.K_RIGHT] and cat_x < WIDTH - CAT2_SIZE:
            cat_x += 5
        btt_y += BATHTUB_SPEED
        if btt_y > HEIGHT:
            btt_y = -BATHTUB_SIZE
            btt_x = random.randint(0, WIDTH - BATHTUB_SIZE)
            BATHTUB_SPEED += 0.3
            score += 1
        offset = (btt_x - cat_x, btt_y - cat_y)
        collision = cat2_mask.overlap(btt_mask, offset)
        if collision:
            print("\n\033[91mGAME OVER!\033[0m \033[1mScore:\033[0m", score)
            pontuação_excel(user_name, "Gato", score)
            game_over = True
        screen.fill(COR_CAT)
        screen.blit(cat2_img, (cat_x, cat_y))
        screen.blit(btt_img, (btt_x, btt_y))
        screen.blit(score_btt_img, (20,20))
        font = pygame.font.Font(None, 45)
        score_text = font.render(": " +str(score), True, (0, 0, 0))
        screen.blit(score_text, (70, 35))
        menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
        font = pygame.font.Font(None, 25)
        text = font.render("MENU", True, (0,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                ir_menu()
        screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        if game_over:
            pygame.draw.circle(screen, (226,49,52), (180,300), 75)
            font = pygame.font.Font(None, 45)
            text = font.render("RETRY", True, (225,225,225))
            text_circle = text.get_rect(center=(180, 300))
            screen.blit(text, text_circle)
            menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
            font = pygame.font.Font(None, 25)
            text = font.render("MENU", True, (0,0,0))
            screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        pygame.display.flip()
        clock.tick(60)
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_over = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 130 < x < 130 + 100 and 250 < y < 250 + 100:
                        game_over = False
                        play_again_cat()
                    if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                        ir_menu()
# -------------------------------------------------------------------------------------------------
def play_gator():
    global GATOR2_SIZE, ANVIL_SIZE, ANVIL_SPEED, SCORE_ANVIL_SIZE, gator_x, gator_y, anvil_x, anvil_y, score, event
    def play_again_gator():
        global GATOR2_SIZE, ANVIL_SIZE, ANVIL_SPEED, SCORE_ANVIL_SIZE, gator_x, gator_y, anvil_x, anvil_y, score, event
        GATOR2_SIZE = 80
        ANVIL_SIZE = 80
        ANVIL_SPEED = 10
        SCORE_ANVIL_SIZE = 50
        gator_x = WIDTH // 2 - GATOR2_SIZE // 2
        gator_y = HEIGHT - GATOR2_SIZE - 10
        anvil_x = random.randint(0, WIDTH - ANVIL_SIZE)
        anvil_y = -ANVIL_SIZE
        score = 0
    play_again_gator()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    COR_GATOR = (87,169,242)
    game_running = True
    game_over = False
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and gator_x > 0:
            gator_x -= 5
        if keys[pygame.K_RIGHT] and gator_x < WIDTH - GATOR2_SIZE:
            gator_x += 5
        anvil_y += ANVIL_SPEED
        if anvil_y > HEIGHT:
            anvil_y = -ANVIL_SIZE
            anvil_x = random.randint(0, WIDTH - ANVIL_SIZE)
            ANVIL_SPEED += 0.3
            score += 1
        offset = (anvil_x - gator_x, anvil_y - gator_y)
        collision = gator2_mask.overlap(anvil_mask, offset)
        if collision:
            print("\n\033[91mGAME OVER!\033[0m \033[1mScore:\033[0m", score)
            pontuação_excel(user_name, "Crocodilo", score)
            game_over = True
        screen.fill(COR_GATOR)
        screen.blit(gator2_img, (gator_x, gator_y))
        screen.blit(anvil_img, (anvil_x, anvil_y))
        screen.blit(score_anvil_img, (20,20))
        font = pygame.font.Font(None, 45)
        score_text = font.render(": " +str(score), True, (0, 0, 0))
        screen.blit(score_text, (70, 35))
        menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
        font = pygame.font.Font(None, 25)
        text = font.render("MENU", True, (0,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                ir_menu()
        screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        if game_over:
            pygame.draw.circle(screen, (226,49,52), (180,300), 75)
            font = pygame.font.Font(None, 45)
            text = font.render("RETRY", True, (225,225,225))
            text_circle = text.get_rect(center=(180, 300))
            screen.blit(text, text_circle)
            menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
            font = pygame.font.Font(None, 25)
            text = font.render("MENU", True, (0,0,0))
            screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        pygame.display.flip()
        clock.tick(60)
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_over = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 130 < x < 130 + 100 and 250 < y < 250 + 100:
                        game_over = False
                        play_again_gator()
                    if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                        ir_menu()
# -------------------------------------------------------------------------------------------------
def play_bonus():
    global DINIS_SIZE, PICO_SIZE, PICO_SPEED, SCORE_PICO_SIZE, dinis_x, dinis_y, pico_x, pico_y, score, event
    def play_again_bonus():
        global DINIS_SIZE, PICO_SIZE, PICO_SPEED, SCORE_PICO_SIZE, dinis_x, dinis_y, pico_x, pico_y, score, event
        DINIS_SIZE = 90
        PICO_SIZE = 90
        PICO_SPEED = 10
        SCORE_PICO_SIZE = 50
        dinis_x = WIDTH // 2 - DINIS_SIZE // 2
        dinis_y = HEIGHT - DINIS_SIZE - 10
        pico_x = random.randint(0, WIDTH - PICO_SIZE)
        pico_y = -PICO_SIZE
        score = 0
    play_again_bonus()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    COR_BONUS = (210,58,224)
    game_running = True
    game_over = False
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dinis_x > 0:
            dinis_x -= 5
        if keys[pygame.K_RIGHT] and dinis_x < WIDTH - DINIS_SIZE:
            dinis_x += 5
        pico_y += PICO_SPEED
        if pico_y > HEIGHT:
            pico_y = -PICO_SIZE
            pico_x = random.randint(0, WIDTH - PICO_SIZE)
            PICO_SPEED += 0.3
            score += 1
        offset = (pico_x - dinis_x, pico_y - dinis_y)
        collision = dinis_mask.overlap(pico_mask, offset)
        if collision:
            print("\n\033[91mGAME OVER!\033[0m \033[1mScore:\033[0m", score)
            pontuação_excel(user_name, "Bónus", score)
            game_over = True
        screen.fill(COR_BONUS)
        screen.blit(dinis_img, (dinis_x, dinis_y))
        screen.blit(pico_img, (pico_x, pico_y))
        screen.blit(score_pico_img, (20,20))
        font = pygame.font.Font(None, 45)
        score_text = font.render(": " +str(score), True, (0, 0, 0))
        screen.blit(score_text, (70, 35))
        menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
        font = pygame.font.Font(None, 25)
        text = font.render("MENU", True, (0,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                ir_menu()
        screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        if game_over:
            pygame.draw.circle(screen, (226,49,52), (180,300), 75)
            font = pygame.font.Font(None, 45)
            text = font.render("RETRY", True, (225,225,225))
            text_circle = text.get_rect(center=(180, 300))
            screen.blit(text, text_circle)
            menu_rect = pygame.draw.rect(screen, (225, 225, 225), (240,35,100,30))
            font = pygame.font.Font(None, 25)
            text = font.render("MENU", True, (0,0,0))
            screen.blit(text, (menu_rect.x+25, menu_rect.y+7))
        pygame.display.flip()
        clock.tick(60)
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_over = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 130 < x < 130 + 100 and 250 < y < 250 + 100:
                        game_over = False
                        play_again_bonus()
                    if 240 < x < 240 + 100 and 35 < y < 35 + 30:
                        ir_menu()
# -------------------------------------------------------------------------------------------------
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_name = user_name[:-1]
            else:
                if len(user_name) < 10:
                    user_name += event.unicode
    screen.fill(COR)
    user_name_intro = font.render("Nome do Jogador", True, (0,0,0))
    screen.blit(user_name_intro, (80,40))
    user_name_box = pygame.draw.rect(screen, (225,225,225), (38,70,285,46))
    user_name_name = font.render(user_name, True, (0,0,0))
    screen.blit(user_name_name, (user_name_box.x+5,user_name_box.y+12))
    pygame.draw.rect(screen, (156, 195, 151), (38,180,120,120))
    screen.blit(dog1_img, (50,190))
    pygame.draw.rect(screen, (156, 195, 151), (197,180,120,120))
    screen.blit(cat1_img, (200,182))
    pygame.draw.rect(screen, (156, 195, 151), (38,380,120,120))
    screen.blit(gator1_img, (40,380))
    pygame.draw.rect(screen, (156, 195, 151), (197,380,120,120))
    screen.blit(bonus_img, (199,390))
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if 38 < x < 38 + 120 and 180 < y < 180 + 120:
            game_over = False
            play_dog()
        elif 197 < x < 197 + 120 and 180 < y < 180 + 120:
            game_over = False
            play_cat()
        elif 38 < x < 38 + 120 and 380 < y < 380 + 120:
            game_over = False
            play_gator()
        if 197 < x < 197 + 120 and 380 < y < 380 + 120:
            game_over = False
            play_bonus()
    if game_running == True:
        pygame.display.update()
pygame.quit()