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

    def get_population_weights(self, checkpoint):
        return [d.calculate_fitness(checkpoint) for d in self.drivers]

    def breed_next_gen(self, position, checkpoint, mutation_rate):
        new_gen = []
        while len(new_gen) < len(self.drivers):
            partners = choices(self.drivers, self.get_population_weights(checkpoint), k=2)
            new_driver = Driver.cross_over(position, *partners)

            for i in range(len(new_driver.dna)):
                if random() < mutation_rate:
                    new_driver.dna[i] = vector.rand_vec()

            new_gen.append(new_driver)
        self.drivers = new_gen
