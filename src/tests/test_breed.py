from neat.neat_structures import Genome, Gene
from neat.neat_functions import breed
from typing import List


def get_fitness(genome: List):
    a = genome
    return 12


gene_0_0 = Gene(
    n_in=0,
    n_out=2,
    w=.3,
    ino=0,
    active=True
)

gene_0_1 = Gene(
    n_in=1,
    n_out=2,
    w=.12,
    ino=1,
    active=False
)

genome_0_high = Genome([gene_0_0, gene_0_1], 27)
genome_0_low = Genome([gene_0_0, gene_0_1], 5)

gene_1_0 = Gene(
    n_in=0,
    n_out=2,
    w=.7,
    ino=0,
    active=True
)

genome_1 = Genome([gene_1_0], 8)


def test_breed_size():
    child = breed(genome_0_low, genome_1, get_fitness=get_fitness)
    assert len(child.genes) == 1


def test_breed_size2():
    child = breed(genome_0_high, genome_1, get_fitness=get_fitness)
    assert len(child.genes) == 2


def test_breed_weights():
    child = breed(genome_0_high, genome_1, get_fitness=get_fitness)
    assert child.genes[0].w == .3 or child.genes[0].w == .7


def test_breed_weights2():
    child = breed(genome_0_high, genome_1, get_fitness=get_fitness)
    assert child.genes[1].w == .12


def test_breed_fitness():
    child = breed(genome_0_high, genome_1, get_fitness=get_fitness)
    assert child.fitness == 12

