from driver_evolution.species import Population
from driver_evolution.species import SIZE, ALIVE, COMPLETED
from driver_evolution.math import vector
import pygame

num_drivers = 100
lifespan = 1800
mutation_rate = 0.004
starting_position = [140, 360]
walls = [
    # walls
    [[100, 260], [980, 260]],
    [[100, 460], [980, 460]],
    [[100, 260], [100, 460]],
    [[980, 260], [980, 460]],
    # obstacles
    [[420, 260], [420, 360]],
    [[620, 360], [620, 460]]
]
checkpoint = [[940, 360], 10]
population = Population.from_random(num_drivers, starting_position, lifespan)
amount_alive = 0
amount_completed = 0
frame_count = 0
generation_num = 1

pygame.init()
pygame.font.init()

width, height = 1080, 720
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Driver Evolution")

font = pygame.font.SysFont("Monospace", 20)

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]


def draw_driver(driver):
    center = driver.position
    pygame.draw.circle(display, WHITE, center, SIZE)
    dir_vec = vector.mult(vector.from_ang_mag(vector.ang(driver.velocity), SIZE), -1)
    pygame.draw.line(display, BLACK, center, vector.sub(center, dir_vec), 3)


def draw_text(text, color, position):
    text_surface = font.render(text, True, color)
    display.blit(text_surface, position)


def draw():
    pygame.draw.rect(display, BLACK, [0, 0, width, height])

    draw_text(f"Generation {generation_num}", WHITE, (15, 15))
    # draw_text(f"{(amount_completed // num_drivers)}% completed", WHITE, (15, 50))

    for wall in walls:
        p1, p2 = wall
        pygame.draw.line(display, WHITE, p1, p2, 2)

    pygame.draw.circle(display, RED, checkpoint[0], SIZE)

    for driver in population.drivers:
        draw_driver(driver)

    pygame.display.update()


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for driver in population.drivers:
        status = driver.get_status(walls, checkpoint)
        if status == ALIVE:
            driver.apply_force(driver.dna[frame_count])
            driver.update()
            amount_alive += 1
        elif status == COMPLETED:
            amount_completed += 1

    if amount_alive != 0 and frame_count < lifespan:
        frame_count += 1
    else:
        population.breed_next_gen(starting_position, checkpoint, mutation_rate)
        generation_num += 1
        amount_completed = 0
        frame_count = 0

    amount_alive = 0
    draw()
