class Vehicle(object):

	def __init__(self, position = (0,0)):
		self.position = position
		self.velocity = (0,0)

	def accelerate(self, intensity = 5):
		self.velocity[0] = self.velocity[0] * intensity
		self.velocity[1] = self.velocity[1] * intensity

	def turn(self, direction):
		self.velocity[0] += direction[0]
		self.velociry[1] += direction[1]

