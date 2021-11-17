from neat.neat_structures import Genome, Gene, Species
from copy import deepcopy
from random import random, choice
from typing import Callable


def breed(g1: Genome, g2: Genome, get_fitness: Callable) -> Genome:
    """
    :param g1: Genome of the first parent
    :param g2: Genome of the second parent
    :param get_fitness: Genome of the second parent
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

    child = Genome(genome, fitness)

    return child
