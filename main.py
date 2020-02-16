import pygame
from pygame import gfxdraw

level = [
    '--------------------------------------------------------------------------------------------------------',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '-                                                                                                      -',
    '--------------------------------------------------------------------------------------------------------',
]

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
BRICK_WIDHT = BRICK_HEIGHT = 30
BRICK_COLOR = (0, 128, 0)
BRICK_COLOR_2 = (255, 128, 0)
FPS = 60
clock = pygame.time.Clock()
PLAYER_SIZE, PLAYER_SIZE = 40, 40
BG_SPEED = 0.5
dx = 0
PLAER_SPEED = 3
penalty = 0.0
BTN_W, BTN_H = 220, 60
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BLUE = (0, 0, 250)

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('первая игра')

player = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
# player.set_colorkey((0, 0, 0))


def face(color):
    pygame.draw.circle(player, color, (PLAYER_SIZE // 2, PLAYER_SIZE // 2), PLAYER_SIZE // 2)
    pygame.gfxdraw.aacircle(player, PLAYER_SIZE // 2, PLAYER_SIZE // 2, PLAYER_SIZE // 2, color)
    pygame.draw.circle(player, GOLD, (12, 15), 4)
    pygame.gfxdraw.aacircle(player, 12, 15, 4, GOLD)
    pygame.draw.circle(player, GOLD, (28, 15), 4)
    pygame.gfxdraw.aacircle(player, 28, 15, 4, GOLD)
    pygame.draw.arc(player, GOLD, (8, 12, 24, 20), 3.6, 6.0)


player_rect = player.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

text = pygame.font.SysFont('Arial', 22, False, False)
text_xy = ((WIN_WIDTH - text.size(f'Штрафных очков {round(penalty, 1)}')[0]) // 2, 32)

btn = pygame.Surface((BTN_W, BTN_H))
btn.fill(BLUE)
text1 = 'Играть снова?'
text1_pos = text.size(text1)

print(text1_pos)
color = BLUE
face(color)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] >= 280 and mouse_pos[0] <= 500 and mouse_pos[1] >= 315 and mouse_pos[1] <= 375:
                    print(545466)

    keys = pygame. key. get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAER_SPEED
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAER_SPEED
    if keys[pygame.K_UP]:
        player_rect.y -= PLAER_SPEED
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAER_SPEED

    screen.fill(BG_COLOR)
    if color == RED:
        color = BLUE
        face(color)

    if dx > -WIN_WIDTH * 4:
        dx -= BG_SPEED
    else:
        if player_rect.x < WIN_WIDTH - PLAYER_SIZE:
            player_rect.x += PLAER_SPEED
    dx -= BG_SPEED
    x = dx
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                # screen.blit(brick, (x, y))
                brick = pygame.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDHT, BRICK_HEIGHT])
                pygame.draw.rect(screen, BRICK_COLOR_2, [x, y, BRICK_WIDHT, BRICK_HEIGHT], 2)
                if brick. colliderect(player_rect):
                    if player_rect.x < WIN_WIDTH - PLAYER_SIZE * 2:
                        if color == BLUE:
                            color = RED
                            face(color)
                        penalty += 0.1
            x += BRICK_WIDHT
        y += BRICK_HEIGHT
        x = dx

    if player_rect.x < WIN_WIDTH - PLAYER_SIZE:
        screen.blit(player, (player_rect))
        screen.blit(
            text.render(f'Штрафных очков {round(penalty, 1)}', True, RED, (50, 50, 50)), text_xy)
    else:
        screen.blit(btn, ((WIN_WIDTH - BTN_W) // 2, WIN_HEIGHT // 2))
        btn.blit(text.render(text1, True, RED, None), ((BTN_W - text1_pos[0]) // 2, (BTN_H - text1_pos[1]) // 2))

    pygame.display.set_caption(f'FPS: {int(clock.get_fps())}')
    pygame.display.update()
    clock.tick(FPS)
