from driver_evolution.species.driver import Driver
from driver_evolution import vector
from random import random, choices

class Population:
    def __init__(self, drivers):
        self.drivers = drivers

    @classmethod
    def from_random(cls, num, position, dna_length):
        drivers = [Driver.from_random(position, dna_length) for _ in range(num)]
        return cls(drivers)

    def make_next_generation(self, mutation):
