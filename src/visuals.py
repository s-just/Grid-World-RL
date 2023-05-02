import pygame
import time

pygame.init()

screen = pygame.display.set_mode((200, 200))
padding = 2

def draw_obstacle(pos):
    pygame.draw.rect(screen, (128, 0, 0), (pos[0] * 40 + 10, pos[1] * 40 + 10, 20-padding, 20-padding))

def draw_agent(pos):
   pygame.draw.circle(screen, (0, 0, 128), ((pos[0]*40)+20,(pos[1]*40)+20), 10)
   
def draw_goal(pos):
    pygame.draw.rect(screen, (0, 128, 0), (pos[0] * 40 + 10, pos[1] * 40 + 10, 20-padding, 20-padding))

def draw_grid(agent_pos):
    # Create a 5x5 grid of rectangles
    for i in range(5):
      for j in range(5):
        pygame.draw.rect(screen, (128, 128, 128), (i * 40, j * 40, 40-padding, 40-padding))

    # Draw the obstacles and goals, then place the agent
    draw_obstacle((1,1))
    draw_obstacle((3,1))
    draw_obstacle((3,2))
    draw_obstacle((0,3))
    draw_obstacle((2,3))
    draw_goal((4,4))
    draw_agent(agent_pos)

draw_grid((0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        if event.type == pygame.KEYDOWN:
            # If the z key is pressed, move agent to goal
            if event.key == pygame.K_z:
                draw_grid((4,4))
                
    # Update display
    pygame.display.update()
