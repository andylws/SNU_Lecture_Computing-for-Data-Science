class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        if self.area > other.area:
            return True
        else:
            return False

    def population_density(self):
        return self.population / self.area
