from hyperEdge import HyperEdge
import sys
import math
import itertools
from random import sample
from sets import Set
import copy

def nChooseR(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

# This is a helper method to check if the graph representation is correct
def printIncidentEdges(incidenceList,edgeList):
	counter = 0
	for edgeRefList in incidenceList:
		print "Vertex labeled " , counter, "has incident edges"
		for edgeIndex in edgeRefList:
			print edgeList[edgeIndex]
		counter = counter + 1

def unusedEdgesAvailable(vertex, incidenceList):
	for edge in incidenceList[vertex]:
		if not edge.used:
			return True
	return False

def getUnusedEdge(vertex, incidenceList):
	for edge in incidenceList[vertex]:
		if not edge.used:
			return edge

def getNextVertex(edge, hamiltonianCycle, currentVertex):
	for vertex in edge.vertices:
		if vertex not in hamiltonianCycle:
			# if not vertex == currentVertex:
				return vertex

def decompose(numOfVertices, incidenceList, hamiltonianEdgeSet, vertexList, hamiltonianVertexSet):

	# This is my implementation of IsCycle
	if len(hamiltonianEdgeSet) == numOfVertices:
		print hamiltonianEdgeSet
		print hamiltonianVertexSet
		print vertexList
		# Do not return true! return is cycle! which returns true only if I have a cycle
		# IsCycle verifies if E(S) describes a Hamilton cycl
		return True

	vertex = vertexList[0]
	if vertex in hamiltonianVertexSet:
		vertexList.pop(0)

	while unusedEdgesAvailable(vertex,incidenceList):
		edge = getUnusedEdge(vertex, incidenceList)
		edge.used = True
		print edge.vertices
		print vertex
		hamiltonianEdgeSet.append(edge.__str__())
		# Now that The cycle we are constructing has the new edge, we must add the corresponding vertices to the vertex set
		for v in edge.vertices:
			hamiltonianVertexSet.append(v)
		if decompose(numOfVertices, copy.deepcopy(incidenceList), copy.deepcopy(hamiltonianEdgeSet), copy.deepcopy(vertexList), copy.deepcopy(hamiltonianVertexSet)):
			return True
		# else:
		# 	hamiltonianEdgeSet.pop(hamiltonianEdgeSet.index(edge.__str__()))
		# 	for v in edge.vertices:
		# 		hamiltonianVertexSet.pop(hamiltonianVertexSet.index(v))
		# 	edge.used = False
	return False


if __name__ == '__main__':
	# The following sets up the graph representation
	sizeOfHyperEdge =  int(sys.argv[1])
	numOfVertices = int(sys.argv[2])
	numOfEdges = nChooseR(numOfVertices, sizeOfHyperEdge)
	degreeOfEachVertex = (2*numOfEdges)/numOfVertices
	counter = 0
	vertexList = []
	# The incidence array will maintain an array of indeces, and incidenceList[vertexLabel] means the vertex denoted
	# by 'vertexLabel' is contained in the hyperEdges whose references are in the array incidenceList[vertexLabel]
	incidenceList = [] 
	# Initialize list
	while counter < numOfVertices:
		incidenceList.append([])
		counter = counter + 1
	edgeList = []
	counter = 0
	while counter < numOfVertices:
		vertexList.append(counter)
		counter = counter + 1

	for edge in list(itertools.combinations(vertexList,sizeOfHyperEdge)):
		newEdge = HyperEdge(sizeOfHyperEdge, edge)
		edgeList.append(newEdge)
		for vertex in newEdge.vertices:
			incidenceList[vertex].append(newEdge)
	if numOfEdges % numOfVertices == 0:
		numberOfCycles = numOfEdges / numOfVertices
		counter = 0
		while counter < numberOfCycles:
			counter = counter + 1
			print decompose(numOfVertices, incidenceList, [], vertexList, [])
	# edge1 = HyperEdge(1, [1,2,3])
	# edge2 = HyperEdge(1, [3,4,5])
	# edgeList = [edge1, edge2]
	# edgeListCopy = copy.deepcopy(edgeList)
	# print edgeList[0].used
	# edgeList[0].used = True
	# print edgeListCopy[0].used






