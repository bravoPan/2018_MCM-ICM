import json
from pprint import pprint

dest_chargers = eval(json.load(open("super_chargers.json", "r")))

charger_type = set()
city_distribute = {}
for i in dest_chargers:
    for j in i[1]:
        charger_type.add(j[1])

type_list = list(charger_type)
for i in dest_chargers:
    city_distribute.setdefault(i[0], [])
    for j in i[1]:
        for type in type_list:
            if type == j[1]:
                city_distribute[i[0]].append(j[0])
            else:
                city_distribute[i[0]].append(0)

# print(type_list)
# print("%20s" * len(type_list) % type_list)



# pprint(city_distribute)
if __name__ == "__main__":
    with open("super_chargers.txt", "w") as f:
        f.write("%50s" % "Dest")
        for i in type_list:
            f.write("%10s" % i)
        f.write("\n")
        for i in city_distribute:
            f.write("%50s" % i)
            for j in city_distribute[i]:
                f.write("%10s" % j)
            f.write("\n")
