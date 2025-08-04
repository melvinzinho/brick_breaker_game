import pygame
import sys
from classes import Player

# Initialize Pygame
pygame.init()

# Set up the display (customize width, height, and title)
screen_width = 800  # Change as needed
screen_height = 600  # Change as needed
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker")  # Customize this

# Set up the clock for 60 FPS (adjust if desired)
clock = pygame.time.Clock()

# Load assets and create variables (add your images, sounds, positions here)
player_image = pygame.image.load(
    "brick_breaker/assets/white_paddle.png"
).convert_alpha()
scaled_player = pygame.transform.scale_by(player_image, 4)  # Optional scaling
player_mask = pygame.mask.from_surface(scaled_player)  # For collisions

ball_image = pygame.image.load("brick_breaker/assets/metal_ball.png").convert_alpha()
scaled_ball = pygame.transform.scale_by(ball_image, 2)  # Optional scaling
ball_mask = pygame.mask.from_surface(scaled_ball)  # For collisions

brick_image = pygame.image.load(
    "brick_breaker/assets/full_metal_brick.png"
).convert_alpha()
scaled_brick = pygame.transform.scale_by(brick_image, 2)  # Optional scaling
brick_mask = pygame.mask.from_surface(scaled_brick)  # For collisions


# Example: Load sound:
# jump_sound = pygame.mixer.Sound("path/to/jump.wav")

# Set up variables:
brick_pos = (400, 0)
player_pos = (
    (screen_width // 2) - 80,
    (screen_height - 50),
)  # Starting position (x, y)
ball_pos = ((screen_width / 2), (screen_height / 2))
# score = 0  # Game score
player_speed = 5  # Movement speed
ball_gravity = 5
ball_bounce = 0


# Main game loop
running = True
while running:
    print(ball_pos)
    # Handle events (add more if needed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add custom events (e.g., key presses, mouse) here

    # Handle input (e.g., keys, mouse; add your code here)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos = (player_pos[0] - player_speed, player_pos[1])

        if ball_mask.overlap(player_mask, offset_player_and_ball):
            ball_bounce = -2

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos = (player_pos[0] + player_speed, player_pos[1])

        if ball_mask.overlap(player_mask, offset_player_and_ball):
            ball_bounce = 2

    # Game logic (add collisions, updates, scoring here)
    ball_pos = ((ball_pos[0] + ball_bounce), ball_pos[1] + ball_gravity)
    offset_player_and_ball = (player_pos[0] - ball_pos[0], player_pos[1] - ball_pos[1])

    offset_ball_and_brick = (
        ball_pos[0] - brick_pos[0],
        ball_pos[1] - brick_pos[1],
    )

    if ball_pos[1] < 0:
        ball_gravity += 5

    if ball_pos[0] < 0:
        ball_bounce = 2
    if ball_pos[0] > (screen_width - 30):
        ball_bounce = -2

    if ball_mask.overlap(player_mask, offset_player_and_ball):
        ball_gravity -= 5

    if ball_mask.overlap(brick_mask, offset_ball_and_brick):
        ball_gravity += 5

    # Clear the screen (customize color)
    screen.fill((0, 0, 0))  # Black background

    # Render game elements (blit images, draw shapes here)
    screen.blit(scaled_player, player_pos)
    screen.blit(scaled_ball, (ball_pos))
    screen.blit(scaled_brick, (brick_pos))

    # Update the display
    pygame.display.flip()

    # Cap FPS
    clock.tick(60)

# Clean up and quit
pygame.quit()
sys.exit()
