import random

class Board(object):
	"""docstring for Board"""

	def __init__(self, arg):
		super(Board, self).__init__()
		# self.arg = arg
		self.size = arg
		self.squares = [[0] * arg for _ in range(arg)]

	def display(self):
		for row in self.squares:
			print(row)

	def start(self):
		s = random.sample(range(self.size**2), 2)
		self.squares[s[0] % 4][(s[0] - (s[0] % 4)) // 4] = 2
		self.squares[s[1] % 4][(s[1] - (s[1] % 4)) // 4] = 2
		

if __name__ == "__main__":
	b = Board(4)
	b.start()
	b.display()