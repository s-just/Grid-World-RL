import pygame
import time
import gridworld

clock = pygame.time.Clock()
FPS = 4 

pygame.init()

screen = pygame.display.set_mode((200, 250))
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
    draw_obstacle((1,3))
    draw_obstacle((2,3))
    draw_obstacle((3,0))
    draw_obstacle((3,2))
    draw_goal((4,4))
    draw_agent(agent_pos)

def draw_episode(episode_num):
    pygame.draw.rect(screen, (0, 0, 0), (0, 200, 200, 50))
    font = pygame.font.Font(None, 24)
    
    text = font.render(f"Episode: {episode_num}", True, (255, 255, 255)) # create a text surface
    text_rect = text.get_rect(center=(100, 225)) # position the text
    screen.blit(text, text_rect) # draw the text onto the screen

    text2 = font.render(f"Press 'z' to go next.", True, (255, 255, 255)) # create a text surface
    text_rect2 = text2.get_rect(center=(100, 240)) # position the text
    screen.blit(text2, text_rect2) # draw the text onto the screen

draw_grid((0,0))

#example_mem = [[(0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)], [(4, 4)], [(4, 4)], [(4, 2), (4, 3), (4, 4)], [(3, 2), (3, 3), (3, 4), (4, 4)]]

move_delay = 1

curr_ep = 0
draw_episode(curr_ep)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        if event.type == pygame.KEYDOWN:
            # If the z key is pressed, move agent to goal
            if event.key == pygame.K_z:
                # Play next episode
                if curr_ep < len(gridworld.mem):
                    for pos in gridworld.mem[curr_ep]:
                        # Redraw the grid and agent at the new position
                        draw_grid(pos)
                        pygame.display.update()
                        clock.tick(FPS)
                    # Increment the episode index
                    curr_ep += 1
                    draw_episode(curr_ep)
                else:
                    break
                
    # Update display
    pygame.display.update()
