import random

from optimizer.genetic_algorithm import GeneticAlgorithm
from simulation_targets.controller import SingleParameterController


class SingleControllerGA(GeneticAlgorithm):
	def __init__(self, setting):
		super().__init__(setting)
		self.fitness_calculation_loop = 200
	
	# uniform random distribution
	# 3 parameter for P, I, D respectively
	def initialize(self):
		new_population = []
		for i in range(self.population_size):
			new_population.append((
				random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
			))
		return new_population
	
	def calculate_fitness(self, individual):
		P, I, D = individual
		feedback = 0
		c = SingleParameterController(0, P, I, D)
		
		for i in range(1, self.fitness_calculation_loop):
			c.update(feedback)
			feedback = c.feedback
			if i > 9:
				c.PID.SetPoint = 1
		
