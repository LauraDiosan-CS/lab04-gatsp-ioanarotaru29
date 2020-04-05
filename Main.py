import math
import numpy as np
from matplotlib import pyplot as plt

from GA import GA


def readGraph(file):
    f = open(file, "r")
    n = int(f.readline())
    graph = []
    for i in range(0, n):
        str = f.readline()
        values = str.split(",")
        edges = []
        for j in range(0, n):
            edges.append(int(values[j]))
        graph.append(edges)
    return graph


class Graph:
    def __init__(self, dist, n):
        self.distance = dist
        self.n = n
        self.intensity = [[1 / (n * n) for _ in range(n)] for _ in range(n)]
        self.quantity = [[0 for _ in range(n)] for _ in range(n)]


class Node:
    def __init__(self, i, x, y):
        self.id = i
        self.x = x
        self.y = y


def distance(n1, n2):
    return math.sqrt((n1.x-n2.x)*(n1.x-n2.x) + (n1.y-n2.y)*(n1.y-n2.y))


def read_graph(file):
    nodes = []
    f = open(file, "r")
    lines = f.readlines()
    for line in lines:
        args = line.split(" ")
        nodes.append(Node(args[0], float(args[1]), float(args[2])))
    n = len(nodes)
    adj = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(distance(nodes[i], nodes[j]))
        adj.append(row)
    return adj


def evalPath(sol,graph):
    pathDistance = 0
    for i in range(0, len(sol)):
        fromCity = sol[i]
        toCity = None
        if i + 1 < len(sol):
            toCity = sol[i + 1]
        else:
            toCity = sol[0]
        pathDistance += graph[fromCity][toCity]
    return 1/pathDistance

def main():
    graph = read_graph("exemplu.txt")
    print(graph)
    # initialise de GA parameters
    gaParam = {'popSize': 5, 'noGen': 3000, 'pc': 0.8, 'pm': 0.1}
    # problem parameters
    problParam = {'noNodes': len(graph),'graph':graph, 'function': evalPath}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    bestChromosomes = []
    bestFitness=[]

    for g in range(gaParam['noGen']):
        # logic alg
        #ga.oneGeneration()
        ga.oneGenerationElitism()
        #ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        bestChromosomes.append(bestChromo)
        bestFitness.append(bestChromo.fitness)
        print('Best solution in generation ' + str(g) + ' is:  f(x) = ' + str(
            1/bestChromo.fitness))

    x=[]
    y=[]
    for i in range(len(bestFitness)):
        x.append(i)
        y.append(bestFitness[i])
    plt.plot(x,y)
    plt.show()



main()