import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
slider_value = 5
time = 0
wave = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Update slider value
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        slider_value += 1
    if keys[pygame.K_DOWN]:
        slider_value -= 1
    slider_value = max(1, min(slider_value, 50))

    screen.fill((0, 0, 0))

    # Center the animation
    center_x, center_y = width // 2, height // 2
    pygame.draw.line(screen, (255, 255, 255), (center_x, 0), (center_x, height))

    x, y = center_x, center_y

    for i in range(slider_value):
        prevx, prevy = x, y

        n = i * 2 + 1
        radius = 75 * (4 / (n * math.pi))
        x += radius * math.cos(n * time)
        y += radius * math.sin(n * time)

        pygame.draw.ellipse(screen, (255, 100, 0), (prevx - radius, prevy - radius, 2 * radius, 2 * radius), 1)
        pygame.draw.line(screen, (255, 255, 255), (prevx, prevy), (x, y))

    wave.insert(0, y)

    pygame.draw.line(screen, (255, 255, 255), (x, y), (center_x, wave[0]), 1)
    pygame.draw.aaline(screen, (255, 255, 255), (x, y), (center_x, wave[0]))

    if len(wave) >= 2:
        pygame.draw.lines(screen, (255, 255, 255), False, [(i, wave[i]) for i in range(len(wave))])

    time += 0.05

    if len(wave) > 250:
        wave.pop()

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
