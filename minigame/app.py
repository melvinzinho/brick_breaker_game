import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display (customize width, height, and title)
screen_width = 800  # Change as needed
screen_height = 600  # Change as needed
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wigga Eats Water Melons")  # Customize this

# Set up the clock for 60 FPS (adjust if desired)
clock = pygame.time.Clock()

# Load assets and create variables (add your images, sounds, positions here)
player_image = pygame.image.load(
    "minigame/player_wigga.png"
).convert_alpha()
scaled_player = pygame.transform.scale(
    player_image, (300, 200))  # Optional scaling
player_mask = pygame.mask.from_surface(scaled_player)  # For collisions

water_melon_image = pygame.image.load(
    "minigame/water_melon.png"
).convert_alpha()
scaled_water_melon = pygame.transform.scale(
    water_melon_image, (200, 150)
)  # Optional scaling
water_melon_mask = pygame.mask.from_surface(
    scaled_water_melon)  # For collisions

police_image = pygame.image.load("minigame/white_police.png").convert_alpha()
scaled_police = pygame.transform.scale(
    police_image, (300, 200))  # Optional scaling
police_mask = pygame.mask.from_surface(scaled_police)  # For collisions


chicken_image = pygame.image.load("minigame/fried_chicken.png").convert_alpha()
scaled_chicken = pygame.transform.scale(
    chicken_image, (150, 100))  # Optional scaling
chicken_mask = pygame.mask.from_surface(scaled_chicken)  # For collisions


# Set up variables:
player_pos = (
    (screen_width / 2),
    (screen_height - 200),
)

water_melon_x = random.randint(0, screen_width)
water_melon_y = -screen_width
water_melon_pos = ((water_melon_x), (water_melon_y))
water_melon_boolean = True

police_pos_x = random.randint(0, screen_width)
police_pos_y = -screen_width
police_pos = ((police_pos_x), (police_pos_y))
police_boolean = True

chicken_pos_x = random.randint(0, screen_width)
chicken_pos_y = -screen_width
chicken_pos = ((chicken_pos_x), (chicken_pos_y))
chicken_boolean = True

player_speed = 8
gravity = 5
player_score = 0
reset = -300
font = pygame.font.SysFont("Arial", 48)

# Main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    water_melon_y += gravity
    police_pos_y += gravity
    chicken_pos_y += gravity

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos = (player_pos[0] - player_speed, player_pos[1])

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos = (player_pos[0] + player_speed, player_pos[1])

    if police_pos_y > screen_height:
        police_pos_y = reset
        police_pos_x = random.randint(0, screen_width)

    if water_melon_y > screen_height:
        water_melon_y = reset
        water_melon_x = random.randint(0, screen_width)

    if chicken_pos_y > screen_height:
        chicken_pos_y = reset
        chicken_pos_x = random.randint(0, screen_width)

    # Game logic (add collisions, updates, scoring here)

    offset_player_and_water_melon = (
        player_pos[0] - water_melon_x,
        player_pos[1] - water_melon_y,
    )

    offset_player_and_police = (
        player_pos[0] - police_pos_x,
        player_pos[1] - police_pos_y,
    )

    offset_player_and_chicken = (
        player_pos[0] - chicken_pos_x,
        player_pos[1] - chicken_pos_y,
    )

    # if water_melon_mask.overlap(player_mask, offset_player_and_water_melon):
    if water_melon_mask.overlap(player_mask, offset_player_and_water_melon):
        player_score += 5
        water_melon_y = reset
        water_melon_x = random.randint(0, screen_width)

    if police_mask.overlap(player_mask, offset_player_and_police):
        police_pos_y = reset
        police_pos_x = random.randint(0, screen_width)
        break

    if chicken_mask.overlap(player_mask, offset_player_and_chicken):
        player_score += 10
        chicken_pos_y = reset
        chicken_pos_x = random.randint(0, screen_width)

    # Clear the screen (customize color)
    screen.fill((0, 0, 0))  # Black background

    # Render game elements (blit images, draw shapes here)
    text_surface = font.render(f"Score: {player_score}", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (100, 50)
    screen.blit(text_surface, text_rect)

    if water_melon_boolean:
        screen.blit(scaled_water_melon, (water_melon_x, water_melon_y))

    if police_boolean:
        screen.blit(scaled_police, (police_pos_x, police_pos_y))

    if chicken_boolean:
        screen.blit(scaled_chicken, (chicken_pos_x, chicken_pos_y))

    screen.blit(scaled_player, (player_pos))

    # Update the display
    pygame.display.flip()

    # Cap FPS
    clock.tick(60)

# Clean up and quit
pygame.quit()
sys.exit()
