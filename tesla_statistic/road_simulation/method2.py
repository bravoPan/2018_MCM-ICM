from road_simulation.config import real_road, neighbors
import math
from pprint import pprint


class MethodTwo:
    def __init__(self, co_map, ne_map):
        self.co_map = co_map
        self.ne_map = ne_map

    def simulate(self, start, end):
        path = self.find_shortest(start, end)
        total_dis = 0
        charge_num = 0
        charge_poi = []
        for i in range(len(path) - 1):
            current_site = path[i]
            next_site = path[i + 1]
            current_dis = self.compute_dis(self.co_map[current_site][0], self.co_map[current_site][1],
                                           self.co_map[next_site][0], self.co_map[next_site][1])
            total_dis += current_dis
            if total_dis >= 30:
                charge_num += 1
                total_dis -= 30
            charge_poi.append((path[i], path[i + 1]))
        # print("Start from %s, end with %s,  The total mile %s" % (start, end, total_dis))
        # print("The num is " + str(charge_num))
        return charge_num

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
        return self.find_path(parens, org_start, org_end)

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

    def simulate_all(self):
        sites = list(self.co_map)
        print("%10s" % sites[0], end="")
        [print("%5s" % i, end="") for i in sites[1:]]
        print("\n")
        for i in sites:
            print("%5s" % i, end="")
            for j in sites:
                print("%5d" % self.simulate(i, j), end="")
            print("\n")


if __name__ == "__main__":
    test = MethodTwo(real_road, neighbors)
    # print(test.simulate("A", "S"))
    test.simulate_all()
    # test.find_shortest("A", "R")
    # test.compute_dis()
    # cost = {"A": 2, "B": 3, "C": 4}
    # a = sorted(cost.items(), key=lambda x: x[1], reverse=False)[]
    # print(a)
