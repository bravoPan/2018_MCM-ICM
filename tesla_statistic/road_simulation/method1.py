from pprint import pprint
import math

'''
start with the horizontal status like this
1 2 3
4 5 6
7 8 9
'''
#
road_graph = {
    "A": (0, 0),
    "B": (4, 0),
    "C": (0, 6),
    "D": (0, 7),
    "E": (0, 11),
    "F": (7, 12),
    "G": (6, 8)
}


class MethodOne:
    def __init__(self, start, capacity, end):
        self.start = start
        self.capacity = capacity
        self.end = end

    def compute_dis(self, one, another):
        return math.sqrt(math.pow(road_graph[one][0] - road_graph[another][0], 2) + math.pow(
            road_graph[one][1] - road_graph[another][1], 2))

    def simulation(self):
        select = []
        remains = set(road_graph) - set(self.start)
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
                print("Can not pass through")
                break

        print(select)
        print("The total is %.2f" % total_dis)
        if total_dis == 0:
            print("The rate of waste is 0")
        else:
            print("The rate of waste is %.2f " % ((total_dis - best_choice) / best_choice))

    def compute_all_point_dis(self):
        points = sorted(list(road_graph))
        print("%10s" % points[0], end="")
        [print("%5s" % i, end="") for i in points[1:]]
        print("\n")
        for i in points:
            print("%5s" % i, end="")
            for j in range(len(points)):
                print("%5.1f" % self.compute_dis(i, points[j]), end="")
            print("\n")


if __name__ == "__main__":
    test = MethodOne("A", 3, "G")
    test.simulation()
