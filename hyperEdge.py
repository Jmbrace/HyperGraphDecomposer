import copy

class HyperEdge:

	def __init__(self, size, vertexList, used = False):
		self.size = size
		self.vertices = vertexList
		self.used = used

	def __str__(self):
		edge = "{"
		counter = 0 
		for v in self.vertices:
			if counter + 1< len(self.vertices):
				edge = edge + (str(v) + ",")
			else:
				edge = edge + (str(v))
			counter = counter + 1
		edge = edge + "}"
		return edge

	# def __copy__(self):
	# 	return HyperEdge(self.size, self.vertices, self.used)

	# def __deepcopy__(self, memo):
	# 	return HyperEdge(copy.deepcopy(self.size, memo), copy.deepcopy(self.vertices, memo), copy.deepcopy(self.used, memo))