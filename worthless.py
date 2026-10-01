import pygame
import random
import math

pygame.init()

W,H = 900, 600
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Worthless Game")

clock = pygame.time.Clock()

stars = []

for _ in range(700):
    angle = random.uniform(0, 2 * math.pi)
    depth = random.uniform(1,1000)
    
    stars.append([angle, depth])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,5))

    cx, cy = W//2, H//2

    for star in stars:
        angle, depth = star
        depth -= 12

        if depth <= 1:
            depth = 1000
            angle = random.uniform(0, 2 * math.pi)
        star[0] = angle
        star[1] = depth

        scale = 500 / depth
        x = cx + math.cos(angle) * scale * 2
        y = cy + math.sin(angle) * scale

        size = max(1, int(4 -depth/300))

        if 0 <= x < W and 0 <= y < H:
            pygame.draw.circle(screen, (0,255,180), (int(x), int(y)), size)

    for r in range(90, 5, -8):
        pygame.draw.circle(
            screen,
            (0,20+r // 3,30+r // 2),
            (cx, cy),
            r,
            2
        )
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
