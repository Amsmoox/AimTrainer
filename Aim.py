import pygame
import random
import time
import math

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
DISPLAY_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Aim Trainer")

SPAWN_RATE = 500
SPAWN_EVENT = pygame.USEREVENT + 1

MARGIN = 40
BACKGROUND_COLOR = (3, 22, 52)  # Darker shade for better contrast
PRIMARY_COLOR = (60, 180, 245)  # Bright blue for primary circles
SECONDARY_COLOR = (245, 165, 34)  # Bright orange for contrast

FONT_STYLE = pygame.font.SysFont("consolas", 30)  # Modern font and slightly larger size

HEALTH_POINTS = 5
INFO_BAR_HEIGHT = 60


class MovingTarget:
    MAX_RADIUS = 25
    EXPANSION_RATE = 0.3
    PRIMARY_COLOR = "blue"
    SECONDARY_COLOR = "yellow"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.expanding = True

    def animate(self):
        if self.radius + self.EXPANSION_RATE > self.MAX_RADIUS:
            self.expanding = False

        if self.expanding:
            self.radius += self.EXPANSION_RATE
        else:
            self.radius -= self.EXPANSION_RATE

    def render(self, win):
        pygame.draw.circle(win, self.PRIMARY_COLOR, (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.SECONDARY_COLOR, (self.x, self.y), self.radius * 0.75)
        pygame.draw.circle(win, self.PRIMARY_COLOR, (self.x, self.y), self.radius * 0.5)
        pygame.draw.circle(win, self.SECONDARY_COLOR, (self.x, self.y), self.radius * 0.25)

    def hit_test(self, x, y):
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return distance <= self.radius


def render_scene(win, targets):
    win.fill(BACKGROUND_COLOR)
    for target in targets:
        target.render(win)


def display_info(win, elapsed, hits, misses):
    pygame.draw.rect(win, "darkgrey", (0, 0, SCREEN_WIDTH, INFO_BAR_HEIGHT))
    time_elapsed = FONT_STYLE.render(f"Elapsed Time: {elapsed:.2f}s", True, "black")
    hit_count = FONT_STYLE.render(f"Score: {hits}", True, "black")
    miss_count = FONT_STYLE.render(f"Misses: {misses}", True, "black")

    win.blit(time_elapsed, (10, 10))
    win.blit(hit_count, (300, 10))
    win.blit(miss_count, (550, 10))


def final_screen(win, duration, hits, total_clicks):
    win.fill(BACKGROUND_COLOR)
    elapsed_label = FONT_STYLE.render(f"Total Time: {duration:.2f}s", True, "white")
    hit_label = FONT_STYLE.render(f"Total Hits: {hits}", True, "white")
    accuracy = (hits / total_clicks * 100) if total_clicks > 0 else 0
    accuracy_label = FONT_STYLE.render(f"Accuracy: {accuracy:.1f}%", True, "white")

    win.blit(elapsed_label, (350, 200))
    win.blit(hit_label, (350, 250))
    win.blit(accuracy_label, (350, 300))

    pygame.display.update()
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.KEYDOWN]:
                pygame.quit()
                exit()


def gameplay():
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
