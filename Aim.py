import pygame
import random
import time
import math

pygame.init()
# Set the dimensions of the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
DISPLAY_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Aim Trainer")
# Game event and timing settings
SPAWN_RATE = 500
SPAWN_EVENT = pygame.USEREVENT + 1
# Margin for spawning targets and design settings
MARGIN = 40
BACKGROUND_COLOR = (3, 22, 52)  # Darker shade for better contrast
PRIMARY_COLOR = (60, 180, 245)  # Bright blue for primary circles
SECONDARY_COLOR = (245, 165, 34)  # Bright orange for contrast
# Font settings for displaying texts
FONT_STYLE = pygame.font.SysFont("consolas", 30)  # Modern font and slightly larger size
# Game life settings
HEALTH_POINTS = 5
INFO_BAR_HEIGHT = 60


class MovingTarget:
    MAX_RADIUS = 25
    EXPANSION_RATE = 0.3
    PRIMARY_COLOR = "blue"
    SECONDARY_COLOR = "yellow"

    def __init__(self, x, y):
        """ Initialize the moving target at a given position """
        self.x = x
        self.y = y
        self.radius = 0
        self.expanding = True

    def animate(self):
        """ Update the target's size dynamically """
        if self.radius + self.EXPANSION_RATE > self.MAX_RADIUS:
            self.expanding = False

        if self.expanding:
            self.radius += self.EXPANSION_RATE
        else:
            self.radius -= self.EXPANSION_RATE

    def render(self, win):
        """ Render the target with alternating colors """
        pygame.draw.circle(win, self.SECONDARY_COLOR, (self.x, self.y), self.radius)
        if self.radius > 5:
            pygame.draw.circle(win, PRIMARY_COLOR, (self.x, self.y), self.radius * 0.75)
        if self.radius > 10:
            pygame.draw.circle(win, SECONDARY_COLOR, (self.x, self.y), self.radius * 0.5)
        if self.radius > 15:
            pygame.draw.circle(win, PRIMARY_COLOR, (self.x, self.y), self.radius * 0.25)


    def hit_test(self, x, y):
        """ Check if a given point (click) is within the target's area """
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return distance <= self.radius


def render_scene(win, targets):
    """ Fill the screen and draw all targets """
    win.fill(BACKGROUND_COLOR)
    for target in targets:
        target.render(win)


def display_info(win, elapsed, hits, misses):
    """ Display game information on the screen """
    pygame.draw.rect(win, (45, 45, 45), (0, 0, SCREEN_WIDTH, INFO_BAR_HEIGHT))  # Darker bar for better readability
    time_elapsed = FONT_STYLE.render(f"Elapsed Time: {elapsed:.2f}s", True, "white")
    hit_count = FONT_STYLE.render(f"Score: {hits}", True, "white")
    miss_count = FONT_STYLE.render(f"Misses: {misses}", True, "white")

    win.blit(time_elapsed, (20, 15))
    win.blit(hit_count, (320, 15))
    win.blit(miss_count, (620, 15))

def final_screen(win, duration, hits, total_clicks):
    """ Display the final screen with game stats """
    win.fill(BACKGROUND_COLOR)
    elapsed_label = FONT_STYLE.render(f"Total Time: {duration:.2f}s", True, PRIMARY_COLOR)
    hit_label = FONT_STYLE.render(f"Total Hits: {hits}", True, PRIMARY_COLOR)
    accuracy = (hits / total_clicks * 100) if total_clicks > 0 else 0
    accuracy_label = FONT_STYLE.render(f"Accuracy: {accuracy:.1f}%", True, SECONDARY_COLOR)

    win.blit(elapsed_label, (350, 150))
    win.blit(hit_label, (350, 225))
    win.blit(accuracy_label, (350, 300))

    pygame.display.update()
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.KEYDOWN]:
                pygame.quit()
                exit()


def gameplay():
    """ Main game loop """
    running = True
    target_list = []
    clock = pygame.time.Clock()

    score = 0
    total_clicks = 0
    errors = 0
    start_time = time.time()

    pygame.time.set_timer(SPAWN_EVENT, SPAWN_RATE)

    while running:
        clock.tick(60)
        mouse_clicked = False
        mouse_position = pygame.mouse.get_pos()
        current_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == SPAWN_EVENT:
                x_pos = random.randint(MARGIN, SCREEN_WIDTH - MARGIN)
                y_pos = random.randint(MARGIN + INFO_BAR_HEIGHT, SCREEN_HEIGHT - MARGIN)
                new_target = MovingTarget(x_pos, y_pos)
                target_list.append(new_target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
                total_clicks += 1

        for target in target_list[:]:
            target.animate()
            if target.radius <= 0:
                target_list.remove(target)
                errors += 1

            if mouse_clicked and target.hit_test(*mouse_position):
                target_list.remove(target)
                score += 1

        if errors >= HEALTH_POINTS:
            final_screen(DISPLAY_WINDOW, current_time, score, total_clicks)

        render_scene(DISPLAY_WINDOW, target_list)
        display_info(DISPLAY_WINDOW, current_time, score, errors)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    gameplay()


# Copyright 2024 Mharrech Ayoub
