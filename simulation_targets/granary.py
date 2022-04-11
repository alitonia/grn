from simulation_targets.history import History


class Granary:
	def __init__(self, environment):
		self._temperature = environment.temperature
		self._humidity = environment.humidity
	
	@property
	def temperature(self):
		return self._temperature
	
	@property
	def humidity(self):
		return self._humidity
	
	@temperature.setter
	# assuming small granary, temperature changes immediately
	def temperature(self, temperature):
		self._temperature = temperature
	
	@humidity.setter
	# assuming small granary, humidity changes immediately
	def humidity(self, humidity):
		self._humidity = humidity


class SmallGranary(Granary):
	pass


class BigGranary(Granary):
	def __init__(self, environment):
		super().__init__(environment)
		self.temperature_history = History()
		self.humidity_history = History()
