from road_simulation.config import real_road, neighbors
import math
from pprint import pprint


class MethodTwo:
    def __init__(self, co_map, ne_map):
        self.co_map = co_map
        self.ne_map = ne_map

    # def simulate(self):

    # the shortest distance
    def find_shortest(self, start, end):
        # org
        org_start = start
        org_end = end

        # set costs inf
        costs = {}
        inf = float("inf")
        costs.setdefault(start, 0)
        for i in list(self.co_map):
            costs.setdefault(i, inf)

        # start find
        process = []
        parens = {"A": None}
        while start != end:
            if end in self.ne_map[start]:
                break
            for i in self.ne_map[start]:
                if i not in process:
                    current_dis = self.compute_dis(self.co_map[start][0], self.co_map[i][0],
                                                   self.co_map[start][1], self.co_map[i][1])
                    if current_dis + costs[start] < costs[i]:
                        costs[i] = current_dis + costs[start]
                        parens.setdefault(i, start)
            process.append(start)
            start = [i[0] for i in sorted(costs.items(), key=lambda x: x[1], reverse=False) if
                     i[0] not in process][0]
            # print(start)
        parens[end] = start
        costs[end] = costs[start] + self.compute_dis(self.co_map[start][0], self.co_map[end][0],
                                                     self.co_map[start][1], self.co_map[end][1])
        # print(order)
        # print(parens)
        print(self.find_path(parens, org_start, org_end))
        pprint(costs)

    def find_path(self, link_dict, start, end):
        path = []
        while end != start:
            path.append(end)
            end = link_dict[end]
        path.append("A")
        path.reverse()
        return path

    @staticmethod
    def compute_dis(start_x, end_x, start_y, end_y):
        return math.sqrt(math.pow(start_x - end_x, 2) + math.pow(start_y - end_y, 2))


if __name__ == "__main__":
    test = MethodTwo(real_road, neighbors)
    test.find_shortest("A", "V")
    # test.compute_dis()
    # cost = {"A": 2, "B": 3, "C": 4}
    # a = sorted(cost.items(), key=lambda x: x[1], reverse=False)[]
    # print(a)
