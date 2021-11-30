from neat.neat_structures import Genome, Gene, Species
from copy import deepcopy
from random import random, choice, uniform
from typing import Callable, List


def initialization(n_inputs: int, n_outputs: int, get_fitness: Callable, pop_size: int = 150):
    ino = 0
    population_genomes = [[] for _ in range(pop_size)]

    # Make each genome gene-by-gene with random weights
    for i in range(n_inputs):
        for j in range(n_outputs):
            for k in range(pop_size):
                new_gene = Gene(n_in=i,
                                n_out=j,
                                w=uniform(-1, 1),
                                ino=ino,
                                active=True
                                )
                population_genomes[k].append(new_gene)
            ino += 1

    population = []
    for gen in population_genomes:
        fitness = get_fitness(gen)
        population.append(Genome(gen, fitness, generation=0))

    return population


def breed(g1: Genome, g2: Genome,  generation: int) -> List:
    """
    :param g1: Genome of the first parent
    :param g2: Genome of the second parent
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

    return genome


def delta(genome1: Genome, genome2: Genome, c1: float = 1.0, c2: float = 1.0, c3: float = .4):
    """
    :param c1: Excess coefficient
    :param c2: Disjoint coefficient
    :param c3: Matching coefficient
    :param genome1: First genome
    :param genome2: Second genome
    :return: Compatibility distance between genomes
    """
    genes1 = genome1.genes
    genes2 = genome2.genes
    n = max(len(genes1), len(genes2))

    # counts
    excess = 0
    disjoint = 0
    matching = 0

    # total difference between matching genes
    total_diff = 0

    # find excess and disjoint count
    i = 0
    j = 0
    while i < len(genes1) or j < len(genes2):
        if i >= len(genes1):
            excess += (len(genes2) - j)
            break
        elif j >= len(genes2):
            excess += (len(genes1) - i)
            break

        gene1 = genes1[i]
        gene2 = genes2[j]

        if gene1.ino == gene2.ino:
            # calculate diff
            diff = abs(gene1.w - gene2.w)
            total_diff += diff
            matching += 1
            i += 1
            j += 1
        elif gene1.ino < gene2.ino:
            disjoint += 1
            i += 1
        else:
            disjoint += 1
            j += 1

    # sanity check
    assert matching != 0

    delta = c1 * (excess / n) + c2 * (disjoint / n) + c3 * (total_diff / matching)

    return delta
