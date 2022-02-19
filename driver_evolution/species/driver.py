from driver_evolution import vector

MAX_FORCE = 0.5
VEL_LIMIT = 5


class Driver:
    def __init__(self, size, position, dna):
        self.size = size
        self.position = position
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.dna = dna

    @classmethod
    def from_random(cls):
        pass

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
