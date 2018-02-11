import matplotlib.pyplot as ply
from road_simulation.method1 import MethodOne
from road_simulation.config import real_road


def draw_md1(start):
    method1 = MethodOne(real_road)
    waste_result = method1.simulate_point(start, 10, 10)
    end_dis = ["%d" % i[1] for i in waste_result]
    waste = ["%.2f" % i[2] for i in waste_result]
    ply.plot(end_dis, waste)
    ply.xlabel("d / km", fontsize=15)
    ply.ylabel("waste rate / %", fontsize=17)
    ply.title("EV starts with " + start)
    ply.show()


if __name__ == "__main__":
    start = ["A", "H", "E", "O"]
    for i in start:
        draw_md1(i)
