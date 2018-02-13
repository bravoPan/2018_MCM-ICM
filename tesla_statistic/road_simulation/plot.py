import matplotlib.pyplot as ply
from road_simulation.method1 import MethodOne
from road_simulation.config import real_road
from road_simulation.method2 import MethodTwo
from road_simulation.config import neighbors, real_road, expanded_graph, au_graph
from PIL import Image, ImageDraw, ImageFont
from pprint import pprint

font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 20)


def draw_charge_station(start, end, scale=25, size=1500):
    background = draw_network(scale, size)
    draw = ImageDraw.Draw(background)
    method2 = MethodTwo(real_road, neighbors)
    best_path = method2.find_shortest(start, end)
    large_graph = expanded_graph(real_road, scale)

    # draw best way
    linked_relations = []
    for i in range(len(best_path) - 1):
        linked_relations.append((best_path[i], best_path[i + 1]))
    for i in linked_relations:
        current_point_co = large_graph[i[0]]
        next_point_co = large_graph[i[1]]
        current_x = current_point_co[0]
        current_y = current_point_co[1]
        next_x = next_point_co[0]
        next_y = next_point_co[1]
        # draw.line((current_x, current_y, next_x, next_y), fill=(255, 255, 255, 100), width=4)
        draw.line((current_x, current_y, next_x, next_y), fill=(255, 255, 0, 100), width=5)

    # draw text
    for city in large_graph:
        city_co = large_graph[city]
        # print(city_co)
        draw.text(city_co, city, fill=(0, 0, 255), font=font)
    draw.text(large_graph[start], start, fill=(0, 255, 0), font=font)
    draw.text(large_graph[end], end, fill=(255, 0, 0), font=font)

    # draw charge station
    stations = method2.find_station(start, end)
    # print(stations)
    r = 10 * scale
    for circle in stations:
        # print(circle)
        large_x = circle[0] * scale
        large_y = circle[1] * scale
        draw.ellipse((large_x - 1, large_y - 1, large_x + 1, large_y + 1), fill=(0, 0, 255))
        # draw.ellipse((large_x - r, large_y - r, large_x + r, large_y + r), fill=(255, 255, 255, 255), outline=(0, 255, 255))

    background.show()
    # best_path
    # background.show()


def draw_network(scale=10, size=500):
    img = Image.new("RGBA", (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    pos = [[(real_road[host], real_road[neighbor]) for neighbor in neighbors[host]] for host in real_road]
    # names = [[(host, neighbor) for neighbor in neighbors[host]] for host in real_road]

    for city in pos:
        for j in city:
            first_point = j[0]
            next_point = j[1]
            first_point_x = first_point[0] * scale
            first_point_y = first_point[1] * scale
            next_point_x = next_point[0] * scale
            next_point_y = next_point[1] * scale
            draw.line((first_point_x, first_point_y, next_point_x, next_point_y), fill=(0, 0, 0, 50), width=4)

    return img
    # img.show()


def draw_md1(start, graph):
    method1 = MethodOne(graph)
    waste_result = method1.simulate_point(start, 10, 273)
    # print(waste_result)
    # print(waste_result)

    end_dis = sorted(["%d" % i[1] for i in waste_result])
    waste = ["%.2f" % i[2] for i in waste_result]
    ply.plot(end_dis, waste)
    ply.xlabel("d / km", fontsize=15)
    ply.ylabel("waste rate / %", fontsize=17)
    ply.title("EV starts with " + start)
    ply.show()


if __name__ == "__main__":
    start = ["A", "H", "E", "O"]
    draw_charge_station("D", "S")
    # draw_network(scale=25, size=1000)
    # draw_charge_station(scale=25, size=1000)
    # test_list = [("K", "S"), ("V", "H"), ("B", "V")]
    # draw_charge_station(test_list[2][0], test_list[2][1])
