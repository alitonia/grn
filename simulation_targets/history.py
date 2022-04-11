class History:
	def __init__(self, limit=3):
		if limit <= 0:
			raise Exception(f'Invalid limit: {limit} <= 0')
		self._records = []
		self._limit = limit
	
	@property
	def record(self):
		return self._records
	
	def add_record(self, v):
		if len(self._records) == self._limit:
			self._records.pop(0)
		self._records.append(v)
