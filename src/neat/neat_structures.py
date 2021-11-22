from typing import List, Set
from enum import Enum


class Genome:
    def __init__(self, connections: List, nodes: List, fitness: float, generation: int = 0):
        self.conGenes = connections # List of ConnectionGenes
        self.nodeGenes = nodes # List of NodeGenes
        self.fitness = fitness
        self.generation = generation
        self.inos = set([g.ino for g in connections])
        self.ino_dic = {g.ino: g for g in connections}
        self.directedConnects = set((g.n_in, g.n_out) for g in connections)

    def __gt__(self, other):
        return self.fitness >= other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __eq__(self, other):
        return self.fitness == other.fitness


class ConnectionGene:
    def __init__(self, n_in: int, n_out: int, w: float, ino: int, active: bool):
        self.n_in = n_in
        self.n_out = n_out
        self.w = w
        self.ino = ino
        self.active = active

    def __str__(self):
        if self.active:
            active_stat = 'active'
        else:
            active_stat = 'disabled'
        return f'Connection between {self.n_in} to {self.n_out} has weight {self.w} and innovation number {self.ino}' \
               f'and is {active_stat}.'


class NodeGene:
    def __init__(self, n_num : int ):
        self.nodes = n_num
        #TODO: Make node types ('sensor', 'hidden', 'output')



class Species:
    def __init__(self, genomes: List, champion: Genome):
        self.genomes = genomes
        self.champion = champion
