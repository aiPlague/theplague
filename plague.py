import random

class Plague:
    def __init__(self, name, transmissibility, lethality):
        self.name = name
        self.transmissibility = transmissibility  # Probability of transmission (0.0 to 1.0)
        self.lethality = lethality  # Probability of death if infected (0.0 to 1.0)

    def mutate(self):
        # Slightly alter transmissibility and lethality during mutation
        self.transmissibility = max(0, min(1, self.transmissibility + random.uniform(-0.1, 0.1)))
        self.lethality = max(0, min(1, self.lethality + random.uniform(-0.05, 0.05)))
        return self

    def __str__(self):
        return f"{self.name} [Transmissibility: {self.transmissibility:.2f}, Lethality: {self.lethality:.2f}]"


class Population:
    def __init__(self, size, virus, initial_infected=10):
        self.size = size
        self.virus = virus
        self.healthy = size - initial_infected
        self.infected = initial_infected
        self.dead = 0

    def step(self):
        # Spread infection
        new_infections = 0
        for _ in range(self.infected):
            if random.random() < self.virus.transmissibility:
                if self.healthy > 0:
                    new_infections += 1
                    self.healthy -= 1

        # Handle deaths
        deaths = 0
        for _ in range(self.infected):
            if random.random() < self.virus.lethality:
                deaths += 1
                self.infected -= 1

        self.dead += deaths
        self.infected += new_infections

        # Virus mutates at each step
        self.virus.mutate()

        return {
            "healthy": self.healthy,
            "infected": self.infected,
            "dead": self.dead,
            "virus": str(self.virus)
        }

    def __str__(self):
        return f"Healthy: {self.healthy}, Infected: {self.infected}, Dead: {self.dead}"


# Initialize simulation
virus = Virus(name="NeoFlu", transmissibility=0.3, lethality=0.05)
population = Population(size=1000, virus=virus)

# Run the simulation for 50 steps
for day in range(1, 51):
    stats = population.step()
    print(f"Day {day}:")
    print(f"Healthy: {stats['healthy']}, Infected: {stats['infected']}, Dead: {stats['dead']}")
    print(f"Virus: {stats['virus']}\n")
