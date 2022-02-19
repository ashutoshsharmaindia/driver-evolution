from driver_evolution import vector
from random import choice

MAX_FORCE = 0.5
VEL_LIMIT = 5
SIZE = 10


class Driver:
    def __init__(self, position, dna):
        self.position = position
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.dna = dna

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

    def get_status(self):
        # TODO: check for collisions with walls and final checkpoint to see if successful
        pass
