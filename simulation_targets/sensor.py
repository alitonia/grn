class _Sensor:
	def __init__(self, measure_target, error_margin=0):
		self.measure_target = measure_target
		self.error_margin = error_margin


class TemperatureSensor(_Sensor):
	def get_temperature(self):
		return self.measure_target.temperature


class HumiditySensor(_Sensor):
	def get_humidity(self):
		return self.measure_target.humidity
