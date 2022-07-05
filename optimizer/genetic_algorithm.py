class GeneticAlgorithm:
	def __init__(self, setting):
		self.population = None
		self.population_size = setting.population_size
		self.current_generation = 0
		self.maximum_generation = setting.maximum_generation
		
		self.solution = None
	
	def initialize(self):
		return []
	
	def calculate_fitness(self, individual):
		return 0
	
	def select(self, population):
		return []
	
	def crossover(self, population):
		return []
	
	def mutate(self, population):
		return []
	
	def check_terminate_condition(self, population):
		return False
	
	def extract_solution(self):
		self.solution = None
		return self.solution
	
	def get_termination_cause(self):
		pass
	
	def run(self):
		self.population = self.initialize()
		
		for i in range(0, self.maximum_generation):
			self.current_generation = i
			
			# calculate fitness for all
			fitness_list = []
			for individual in self.population:
				current_fitness = self.calculate_fitness(individual)
				fitness_list.append((current_fitness, individual))
			
			# selection phase
			selected_population = self.select(self.population)
			
			# crossover phase
			crossed_population = self.crossover(selected_population)
			
			# mutate phase
			mutated_population = self.mutate(crossed_population)
			
			# done
			self.population = mutated_population
			
			if self.check_terminate_condition(self.population):
				break
		
		return self.solution
