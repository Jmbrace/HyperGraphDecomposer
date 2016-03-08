class HyperEdge:

	def __init__(self, numOfVertices, size):
		self.numOfVertices = numOfVertices
		self.size = size
		self.vertices = []
		self.used = false

	def addVertex(self, vertex):
		self.vertices.append(vertex)