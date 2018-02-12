from pprint import pprint
import math
from road_simulation.config import real_road, au_graph, expanded_graph

'''
start with the horizontal status like this
1 2 3
4 5 6
7 8 9
'''


class MethodOne:
    def __init__(self, map):
        self.map = map

    def compute_dis(self, one, another):
        return math.sqrt(math.pow(self.map[one][0] - self.map[another][0], 2) + math.pow(
            self.map[one][1] - self.map[another][1], 2))

    def simulation(self, start, end, capacity):
        self.capacity = capacity
        self.start = start
        self.end = end
        select = []
        remains = set(self.map) - set(self.start)
        total_dis = 0
        best_choice = self.compute_dis(self.start, self.end)
        while self.start != self.end:
            next_point = ""
            longest = 0
            for i in remains:
                current_dis = self.compute_dis(self.start, i)
                current_to_end = self.compute_dis(self.start, self.end)
                if current_to_end <= self.capacity:
                    total_dis += current_to_end
                    self.start = self.end
                    select.append(self.end)
                    select.append(current_to_end)
                    break
                elif current_dis <= self.capacity:
                    if current_dis > longest:
                        longest = current_dis
                        next_point = i
            if self.start != self.end:
                select.append(next_point)
                select.append(longest)
                total_dis += longest
                self.start = next_point
                remains -= set(self.start)
            if self.start == "":
                # print("Can not pass through")
                break

        # pprint(select)
        # print("The total is %.2f" % total_dis)
        waste_rate = (total_dis - best_choice) / best_choice
        if total_dis == 0:
            return None
            # print("The rate of waste is 0")
            # else:
            # print("The rate of waste is %.2f " % (waste_rate))
        return end, best_choice * 9.375, waste_rate

    def compute_all_point_dis(self):
        points = sorted(list(self.map))
        print("%10s" % points[0], end="")
        [print("%5s" % i, end="") for i in points[1:]]
        print("\n")
        for i in points:
            print("%5s" % i, end="")
            for j in range(len(points)):
                print("%5.1f" % self.compute_dis(i, points[j]), end="")
            print("\n")

    def compute_shortest(self, start, size):
        points = sorted(list(self.map))
        shortest = {}
        for i in points:
            shortest.setdefault(i, self.compute_dis(start, i))
        final = [i[0] for i in sorted(shortest.items(), key=lambda x: x[1], reverse=True)[:size] if i[0]]
        return final

    def simulate_point(self, start, end_size, capacity):
        longest = self.compute_shortest(start, size=end_size)
        result = []
        for long in longest:
            result.append(self.simulation(start, long, capacity))
        return result


if __name__ == "__main__":
    real_graph = expanded_graph(au_graph, 10)
    test = MethodOne(real_graph)
    # print(test.simulate_point("A", 10, 273))
    # test.simulation("A", 10, "E")
    # test.compute_all_point_dis()
    # shortest = test.compute_shortest("A", 273)
    # print(shortest)
    # for i in shortest:
    #     print(test.simulation("A", i, 10))
    # test.simulate_point("B", 10, 10)
    # test.compute_all_point_dis()

# a_test = ["V", "M", "L", "O", "U", "T", "S", "R", "N", "H"]
