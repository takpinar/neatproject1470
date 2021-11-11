from typing import List


class Genome:
    def __init__(self, genes: List, fitness: float):
        self.genes = genes
        self.fitness = fitness


class Genes:
    def __init__(self, n_in: int, n_out: int, w: float, ino: int, active: bool):
        self.n_in = n_in
        self.n_out = n_out
        self.w = w
        self.ino = ino
        self.active = active


class Species:
    def __init__(self, genomes: List, champion: Genome):
        self.genomes = genomes
        self.champion = champion
