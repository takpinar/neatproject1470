from neat_structures import Genome, ConnectionGene, NodeGene, Species
from random import random, sample, uniform
from typing import Callable

def mutate(g: Genome, ino: int, get_fitness: Callable):
	"""
	Function to randomly mutates the genome to alter the weights, add new connection,
	or add new node.
	:param g: genome to be mutated
	:return: mutated genome
	"""

	nodes = g.nodeGenes
	connections = g.conGenes
	
	#TODO:

	###	_________________ ###
	###|Weight Mutations |###
	###	_________________ ###
	
	for connection in connections:
		if random < 0.75:
			randomPerturbation = uniform(-1,1)
			connection.w += randomPerturbation

	###	_____________________ ###
	###|Structural Mutations |###
	###	_____________________ ###

	# ADD CONNECTION
	if random() < 0.75:
		newConnection = False
		while not newConnection:
			toBeConnected = sample(nodes, 2) # Get random new nodes to connect
			node1, node2 = toBeConnected[0], toBeConnected[1]
			if (node1,node2) in g.directedConnects: # Start over if existing connection
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

		connections.append(newConnection1, newConnection2)
	
	fitness = get_fitness(connections)
	newGenome = Genome(connections, nodes, fitness, g.generation) 

	
	return newGenome