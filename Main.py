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


def evalPath(sol,graph):
    s=0
    crt=0
    visited=[0]
    for _ in range(len(sol)):
        s+=graph[crt][sol[crt]]
        crt=sol[crt]
        if crt not in visited:
            visited.append(crt)
    return s+len(graph)*100-len(visited)*100

def main():
    graph = readGraph("exemplu.txt")
    print(graph)
    # initialise de GA parameters
    gaParam = {'popSize': 50, 'noGen': 200, 'pc': 0.8, 'pm': 0.1}
    # problem parameters
    problParam = {'noNodes': len(graph),'graph':graph, 'function': evalPath}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    bestChromosomes = []

    for g in range(gaParam['noGen']):
        # logic alg
        #ga.oneGeneration()
        ga.oneGenerationElitism()
        # ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        bestChromosomes.append(bestChromo)
        print('Best solution in generation ' + str(g) + ' is: x = ' + str(
            bestChromo.repres) + ' f(x) = ' + str(
            bestChromo.fitness))



main()