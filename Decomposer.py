from hyperEdge import HyperEdge
import sys
import 

def nChooseR(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

if __name__ == '__main__':
	sizeOfHyperEdge =  sys.argv[1]
	numOfVertices = sys.argv[2]
	numOfEdges = nChooseR(numOfVertices, sizeOfHyperEdge)
	degreeOfEachVertex = (2*numOfEdges)/numOfVertices