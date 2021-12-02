from neat_structures import Genome, Gene
from neat_functions import initialization, breed, delta, mutateWeights, mutateNode, mutateConnection
from typing import List
from random import randint


def dummy_fitness():
	return 10

def runNeat(fitnessFunction, population: List, maxGen=None):

	dThresh = 3 #Delta Threshold

	generation = 0
	species = [] # a list of lists that contain genomes in the same species

	###___GENERATION LOOP____###
	while generation < maxGen or maxGen == None:
		generation += 1	



		#TODO: order and write:
		# mutations,
		# breeding
		# selecting champion





		#Sequential speciation
		newSpecies = [[] for i in range(len(species))]
		for genome in population:
			for i, spec in enumerate(species):
				representativeGenome = spec[randint(0, len(spec)-1)]
				dlt = delta(representativeGenome, genome)
				if dlt < dThresh:
					newSpecies[i].append(genome)
				else:
					continue
			newSpecies.append([genome])
		species = newSpecies

	



def main():
	#___PARAMS___#
	in_nodes = 3
	out_nodes = 1

	init_pop = initialization(in_nodes, out_nodes, dummy_fitness())
	runNeat(dummy_fitness(), init_pop)

if __name__ == '__main__':
	main()