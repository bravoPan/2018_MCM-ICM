import numpy as np
from PIL import Image, ImageFont, ImageDraw
from pprint import pprint

img = Image.open("Australia.png")
img = img.convert("RGBA")
pixels = np.array(img)
rows, columns = pixels.shape[0:2]
new_map = Image.new("RGBA", (columns, rows), (255, 255, 255))
draw = ImageDraw.Draw(new_map)

cities = []
for row in range(rows):
    for col in range(columns):
        # print(pixels[row][col])
        dot_rgb = list(pixels[row][col])
        if dot_rgb[0] > 240 and dot_rgb[1] > 240 and dot_rgb[2] > 240:
            # if l == [0, 0, 0, 255]:
            cities.append((col, row))
            # print("%2s %2s" % (row, col))


def get_repeat():
    start = 0
    # the same row
    clean_cities = set(cities)
    dif_rows = set([city[0] for city in cities])
    delete_points = []
    for i in dif_rows:
        check_points = [city[1] for city in cities if city[0] == i]
        same = 0
        check_number = len(check_points) - 1
        group = {}
        group_num = 0
        for point in range(check_number):
            print(check_points[point + 1][2])
            if check_points[point + 1][2] == check_points[point][1] + 1:
                delete_points.append(check_points[point])
                same += 1
            else:
                group[group_num] = same
                if check_points[point][1] + 1 < columns:
                    same = 0
                    group_num += 1
        if same >= 5:
            delete_points.append(check_points[check_number + 1])
            clean_cities -= set(delete_points)

    print(clean_cities)


def filter_road(pixels):
    def delete_same_y(y_axis):
        line_point = [i for i in pixels if i[1] == y_axis]
        for i in line_point:
            pixels.remove(i)

    different_y = set([i[1] for i in pixels])

    for i in different_y:
        same_line_pixel = len([j for j in pixels if j[1] == i])
        if same_line_pixel > 10:
            delete_same_y(i)


# fill every white pixel with .
for city in cities:
    draw.text((city[0], city[1]), ".", fill=(255, 0, 0))


def draw_grid_line():
    # draw horizontal line
    gap = 20
    count = 1
    for i in range(int(img.height / 10)):
        draw.line((0, gap * count, img.width, gap * count), fill=(0, 0, 0))
        count += 1

    # draw vertical line
    count = 1
    for j in range(int(img.width / 10)):
        draw.line((gap * count, 0, count * gap, img.height), fill=(0, 0, 0))
        count += 1

def square_recognize(city_list):
    for city in city_list:


pprint(cities)
new_map.show()
