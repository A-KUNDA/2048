import random

def bubbleleft(ls):
	still = False
	while not still:
		still = True
		for i in range(len(ls) - 1):
			if ls[i] == 0 and ls[i+1] != 0:
				ls[i], ls[i+1] = ls[i+1], ls[i]
				still = False

def collapseleft(ls):
	for i in range(len(ls)-1):
		if ls[i] == ls[i+1]:
			ls[i] = 2*ls[i]
			for j in range(i+1, len(ls)-1):
				ls[j] = ls[j+1]
			ls[len(ls) - 1] = 0


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
	
	def move_left(self):
		for row in self.squares:
			bubbleleft(row)
			collapseleft(row)

if __name__ == "__main__":
	b = Board(4)
	b.start()
	b.display()
	b.move_left()
	print("\n")
	b.display()