import pygame

# Initialize Pygame
pygame.init()

# Create the display surface object of specific dimensions (500, 500)
win = pygame.display.set_mode((500, 500))

# Set the Pygame window name
pygame.display.set_caption("Moving rectangle")

# Object current coordinates
x = 200
y = 200

# Dimensions of the object
width = 20
height = 20

# Velocity / speed of movement
vel = 10

# Flag to check if the key has been pressed
key_pressed = False

# Indicates Pygame is running
run = True

# Infinite loop
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # Check for a key press event
            if event.key == pygame.K_SPACE:
                key_pressed = True

    if key_pressed:
        # Move the rectangle continuously in the positive y-direction
        y += vel

        # If the rectangle goes off the bottom of the window, reset its position
        if y > 500:
            y = 0 - height

    # Store keys pressed
    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    # Move right
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    win.fill((0, 0, 0))
    print(x, y)
    # Drawing object on screen, which is a rectangle here
    pygame.draw.rect(win, (255, 200, 0), (x, y, width, height))

    # Refresh the window
    pygame.display.update()

# Close the Pygame window
pygame.quit()