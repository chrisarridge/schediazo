
class Path:
	def __init__(self, transform=None):
		self._commands = ''

	def move_to(self, x, y):
		self._commands += ' M {} {}'.format(x,y)

	def close_path(self):
		self._commands += ' Z'

	def line_to(self, x, y):
		self._commands += ' L {} {}'.format(x,y)

	def curve_to(self, x1, y1, x2, y2, x3, y3):
		self._commands += ' C {} {} {} {} {} {}'.format(x1, y1, x2, y2, x3, y3)

	@property
	def d(self):
		return self._commands
