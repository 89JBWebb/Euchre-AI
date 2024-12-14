import DecisionTree

def isOdd(x):
    return x%2


a = DecisionTree.Node()
a.yes = 999
a.no = -1
a.d = isOdd

print(a.eval(3))
