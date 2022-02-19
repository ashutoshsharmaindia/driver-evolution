from driver_evolution.species import Driver, Population
import pygame

num_drivers = 25
lifespan = 1200
mutation_rate = 0.1
starting_position = [625, 75]
walls = [
    [[650, 50], [100, 50]],
    [[100, 50], [50, 100]],
    [[50, 100], [50, 400]],
    [[50, 400], [100, 450]],
    [[100, 450], [650, 450]],
    [[650, 450], [650, 400]],
    [[650, 400], [250, 400]],
    [[250, 400], [250, 100]],
    [[250, 100], [650, 100]],
    [[650, 100], [650, 50]]
]
population = Population.from_random(num_drivers, starting_position, lifespan)

width, height = 700, 500
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Driver Evolution")


def draw():
    pass


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
