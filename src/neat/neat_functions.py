from neat.neat_structures import Genome, Gene, Species
from copy import deepcopy
from random import random, choice
from typing import Callable


def initialization(n_inputs: int, n_outputs: int, gene: Gene, genome: Genome, find_fitness: callable, pop_size=150):
    ino = 0
    population_genomes = [[] for _ in range(pop_size)]

    # Make each genome gene-by-gene with random weights
    for i in range(n_inputs):
        for j in range(n_outputs):
            for k in range(pop_size):
                new_gene = gene(n_in=1,
                            n_out=j,
                            w=uniform(-1, 1),
                            ino=ino,
                            active=True
                            )
                population_genomes[k].append(new_gene)
            ino += 1

    population = []
    for gen in population_genomes:
        fitness = find_fitness(gen)
        population.append(Genome(gen, fitness, generation=0))

    return population


def breed(g1: Genome, g2: Genome, get_fitness: Callable, generation: int) -> Genome:
    """
    :param g1: Genome of the first parent
    :param g2: Genome of the second parent
    :param get_fitness: Genome of the second parent
    :param generation: Current generation
    :return: Genome of the child
    """
    if g1 > g2:
        better_parent = g1
        other_parent = g2
    else:
        better_parent = g2
        other_parent = g1
    genome_dic = deepcopy(better_parent.ino_dic)
    for ino in genome_dic:
        if ino in other_parent.inos:
            if not better_parent.ino_dic[ino].active or not other_parent.ino_dic[ino].active:
                if random() < .75:
                    genome_dic[ino].active = False
                else:
                    genome_dic[ino].active = True
            genome_dic[ino].w = choice([better_parent.ino_dic[ino].w, other_parent.ino_dic[ino].w])

    genome = list(genome_dic.values())

    fitness = get_fitness(genome)

    child = Genome(genome, fitness, generation)

    return child
