from dataclasses import dataclass
from random import randint, choice
@dataclass(order=True)
class agent:
    name: str
    genes: list
    iteration: int = 0
    fitness: int = 0
    def shuffle_genes(self, severity):
        for i in range(int(severity * float(len(self.genes)) * 2)):
            self.genes[randint(0, len(self.genes)) - 1] = bool(randint(0,1))
    def sex(self, partner):
        kid = agent(self.name, self.genes, self.iteration + 1)
        for i in range(5):
            num = randint(0, len(kid.genes) - 1)
            kid.genes[num] = partner.genes[num]
        return kid
def main(iterations, population, names, agents_per_gen, determine_fitness, mutation_chance):
    agents = []
    for _ in range(population):
        temp = agent(choice(names), [True for i in range(10)])
        temp.shuffle_genes(10)
        temp.fitness = determine_fitness(temp)
        agents.append(temp)
    fittest = sorted(agents, key=lambda x: x.fitness, reverse=True)
    for i in range(iterations):
        children = []
        for i in fittest[:agents_per_gen]:
            for _ in range(population // agents_per_gen):
                child = i.sex(choice(fittest[:agents_per_gen]))
                child.fitness = determine_fitness(child)
                children.append(child)
        agents = children
        fittest = sorted(agents, key=lambda x: x.fitness, reverse=True)
    return fittest
if __name__ == '__main__':
    def determine_fitness(self):
        return self.genes.count(True)

    print(main(100, 100, ["bert", "julia", "karin"], 10, determine_fitness, 0.01))