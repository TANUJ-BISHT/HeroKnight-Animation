import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('TANUJ YO')
game_icon = pygame.image.load('player/HeroKnight/game_icon.png').convert_alpha()
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
run = True

#ground
ground = pygame.image.load('player/HeroKnight/ground.png').convert_alpha()
ground = pygame.transform.scale(ground,(1280,720))
ground_rect = ground.get_rect(topleft = (0,500))

#player
player = pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_0.png').convert_alpha()
player = pygame.transform.scale2x(player)
player_rect = player.get_rect(bottomleft = (500,400))
player_mask = pygame.mask.from_surface(player)

#player change size function
def change_size(frame_list):
    mt = []
    for frames in frame_list:
        mt.append(pygame.transform.scale2x(frames))
    return mt


player_idle = []
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_0.png').convert_alpha())
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_1.png').convert_alpha())
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_2.png').convert_alpha())
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_3.png').convert_alpha())
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_4.png').convert_alpha())
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_5.png').convert_alpha())
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_6.png').convert_alpha())
player_idle.append(pygame.image.load('player/HeroKnight/Idle/HeroKnight_Idle_7.png').convert_alpha())

player_run = []
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_0.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_1.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_2.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_3.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_4.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_5.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_6.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_7.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_8.png').convert_alpha())
player_run.append(pygame.image.load('player/HeroKnight/Run/HeroKnight_run_9.png').convert_alpha())

player_jump = []
player_jump.append(pygame.image.load('player/HeroKnight/Jump/HeroKnight_jump_0.png').convert_alpha())
player_jump.append(pygame.image.load('player/HeroKnight/Jump/HeroKnight_jump_1.png').convert_alpha())
player_jump.append(pygame.image.load('player/HeroKnight/Jump/HeroKnight_jump_2.png').convert_alpha())

current_frame = 0
player_jump = change_size(player_jump)
player_run = change_size(player_run)
player_idle = change_size(player_idle)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('sky blue')
    screen.blit(ground,ground_rect)

    player_rect.y += 5
    if player_rect.y >= 400:
        player_rect.y = 400

    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += 3
        current_frame += 0.2
        if current_frame > 9 :
            current_frame = 0
        screen.blit(player_run[int(current_frame)],player_rect)
    elif keys[pygame.K_LEFT]:
        player_rect.x -= 3
        current_frame += 0.2
        if current_frame > 9 :
            current_frame = 0
        screen.blit((pygame.transform.flip(player_run[int(current_frame)],True,False)),player_rect)
    elif keys[pygame.K_SPACE]:   
        player_rect.y -= 10
        current_frame += 0.2
        if current_frame > 2 :
            current_frame = 0
        screen.blit(player_jump[int(current_frame)],player_rect)        
    else:
        current_frame += 0.2
        if current_frame > 7 :
            current_frame = 0
        screen.blit(player_idle[int(current_frame)],player_rect)

    pygame.display.update()
    clock.tick(75)