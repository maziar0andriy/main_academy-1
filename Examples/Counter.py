class Counter:
	def __init__(self, to):
		if not isinstance(to, int):
			raise TypeError("That must gets only integer")
		self.__sequence = (x for x in range(1, to+1))

	def __bool__(self):
		try:
			return bool(next(self.__sequence))
		except StopIteration as e:
			return False

if __name__ == "__main__":
	# Original way
	i = 0
	while i<3:
		print("hello")
		i+=1

	# with counter
	counter = Counter(3)
	while counter:
		print("hello")
