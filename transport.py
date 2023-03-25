#25/03/2023 Model(state-based models: search problem)
import sys
sys.setrecursionlimit(10000)
class TransportationProblem(object):
    def __init__(self,N):
        self.N = N
    def isEnd(self, state):
        return state == self.N
    def startState(self):
        return 1
    def succAndCost(self, state):
        #return a list of  (action,succesor,cost) triplets
        result = []
        if state + 1 <= self.N:
            result.append(('walk', state + 1, 1))
        if state * 2 <= self.N:
            result.append(("tram", state * 2, 2))
        return result
# Algorithms   
def printSolution(solution):
    totalCost, history = solution
    print('Total Cost: {}'.format(totalCost))
    for state in history:
        print(state)


def backtrackingSearch(problem):
    best = {
        'totalCost': float('+inf'),
        'history': None
    }
    def recurse(state,history,totalCost):

        if problem.isEnd(state):
            if totalCost < best['totalCost']:
                best['totalCost'] = totalCost
                best['history'] = history
        for action, succesor, cost in problem.succAndCost(state):
            recurse(succesor, history + [(action, succesor,cost)], totalCost + cost )
    recurse(problem.startState(),history=[], totalCost= 0)
    
    return (best['totalCost'],best['history'])        

def dynamicProgramming(problem):
    cache = {}
    result = 0
    def futureCost(state):
        if problem.isEnd(state):
            return 0
        if state in cache:
            return cache[state]
        result = min(cost + futureCost(succesor) for action, succesor, cost in problem.succAndCost(state))
        cache[state] = result
        return result
    return (futureCost(problem.startState()),[])

####Main
problem = TransportationProblem(100)
print('BackTracking Search: ')
printSolution(backtrackingSearch(problem))
print('DynamicProgramming Search:')
printSolution(dynamicProgramming(problem))