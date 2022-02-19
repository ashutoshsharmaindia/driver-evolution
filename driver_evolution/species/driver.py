from random import choice

from driver_evolution.math import collision, vector

MAX_FORCE = 0.5
VEL_LIMIT = 5
SIZE = 10

# Statuses of driver
ALIVE = 0
CRASHED = 1
COMPLETED = 2


class Driver:
    def __init__(self, position, dna):
        self.position = position
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.dna = dna
        self.status = ALIVE
        self.fitness = None

    @classmethod
    def from_random(cls, position, dna_length):
        dna = [vector.rand_vec() for _ in range(dna_length)]
        return cls(position, dna)

    @classmethod
    def cross_over(cls, position, a, b):
        new_dna = []
        for i in range(len(a.dna)):
            new_dna.append(choice([a.dna[i], b.dna[i]]))
        return cls(position, new_dna)

    def apply_force(self, force):
        self.acceleration = vector.add(self.acceleration, vector.limit_mag(force, MAX_FORCE))

    def update(self):
        self.velocity = vector.add(self.velocity, self.acceleration)
        self.velocity = vector.limit_mag(self.velocity, VEL_LIMIT)
        self.position = vector.add(self.position, self.velocity)
        self.acceleration = [0, 0]

    def get_status(self, walls, checkpoint):
        if self.status == ALIVE:
            for wall in walls:
                if collision.circle_to_line(self.position, SIZE, wall[0], wall[1]):
                    self.status = CRASHED
                    break

            if collision.circle_to_circle(self.position, SIZE, checkpoint[0], checkpoint[1]):
                self.status = COMPLETED

        return self.status

    def calculate_fitness(self, checkpoint):
        if not self.fitness:
            dist = collision.calc_dist(self.position, checkpoint[0])
            if self.status == COMPLETED:
                dist *= 10
            elif self.status == CRASHED:
                dist /= 10
            self.fitness = dist
        return self.fitness
