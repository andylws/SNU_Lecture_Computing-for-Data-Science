from P1 import Country  # Do Not Modify


class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        total_population = 0
        for country in self.countries:
            total_population = total_population + country.population
        return total_population
