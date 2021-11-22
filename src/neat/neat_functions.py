from neat_structures import Genome, ConnectionGene,NodeGene, Species
from copy import deepcopy
from random import random, choice, uniform, sample
from typing import Callable


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

def mutate(g: Genome, ino: int, get_fitness: Callable):
	"""
	Function to randomly mutates the genome to alter the weights, add new connection,
	or add new node.
	:param g: genome to be mutated
	:return: mutated genome and new innovation number
	"""

	nodes = g.nodeGenes # Get list of existing nodes
	connections = g.conGenes # Get list of existing connections
	
	
	###|Weight Mutations|###
    	
	for connection in connections:
		if random < 0.75:
			randomPerturbation = uniform(-1,1)
			connection.w += randomPerturbation


    ###|Structural Mutations|###
	
	# ADD CONNECTION
	if random() < 0.75:
		newConnection = False
		while not newConnection:
			toBeConnected = sample(nodes, 2) # Get random new nodes to connect
			node1, node2 = toBeConnected[0].n_num, toBeConnected[1].n_num
			if (node1,node2) in g.directedConnects: # If existing connection, start over 
				continue
			newConnection = True

		randomWeight = random() # Get new Weight

		####TODO: figure out innovation number
		ino += 1
		newConnection = ConnectionGene(node1, node2, randomWeight, ino, active=True)
		connections.append(newConnection)
		####TODO: check different node types?

	# ADD NODE
	if random() < 0.75:
		nodeNum = len(nodes)
		newNode = NodeGene(nodeNum) # Create new node
		nodes.append(newNode) # Add NodeGene 

		connection = sample(connections, 1) # Get connection in which to insert node 
		connection.active = False # Disable old connection
		oldWeight = connection.w
		newWeight = 1
		node1, node2 = connection.n_in, connection.n_out

		ino += 1
		newConnection1 = ConnectionGene(node1, newNode, newWeight, ino, active=True) # Connect node1 and new
		ino += 1
		newConnection2 = ConnectionGene(newNode, node2, oldWeight, ino, active=True) # connect new and node2

		connections.append(newConnection1, newConnection2) # Add to connections list
	
	fitness = get_fitness(connections)
	mutatedGenome = Genome(connections, nodes, fitness, g.generation) 

	
	return mutatedGenome, ino
