from pprint import pprint

'''
start with the horizontal status like this
1 2 3
4 5 6
7 8 9
'''

road_graph = {}
counter = 0
for i in range(3):
    for j in range(3):
        road_graph.setdefault(str(counter), (i, j))
        counter += 1

class MethodOne:
    def __init__(self):
        print("Waiting...")