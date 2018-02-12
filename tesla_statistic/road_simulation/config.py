real_road = {
    "A": (6, 4),
    "B": (4, 6),
    "C": (7, 6),
    "D": (10, 5),
    "E": (9, 17),
    "F": (7, 8),
    "G": (7, 10),
    "H": (9, 8),
    "I": (12, 8),
    "J": (16, 7),
    "K": (12, 19),
    "L": (19, 18),
    "M": (20, 20),
    "N": (6, 22),
    "O": (24, 24),
    "P": (13, 25),
    "Q": (5, 29),
    "R": (3, 34),
    "S": (13, 34),
    "T": (18, 32),
    "U": (22, 20),
    "V": (26, 31),
    "W": (4, 12)
}

road_graph = {
    "A": (0, 0),
    "B": (4, 0),
    "C": (0, 6),
    "D": (0, 7),
    "E": (0, 11),
    "F": (7, 12),
    "G": (6, 8)
}

neighbors = {
    "A": ("B", "C"),
    "B": ("A", "C", "F", "G"),
    "C": ("A", "B", "D", "F"),
    "D": ("C", "H", "I"),
    "F": ("B", "C", "G", "H"),
    "H": ("C", "D", "F", "G", "I"),
    "I": ("D", "H", "J"),
    "J": ("I", "L"),
    "G": ("W", "E", "B", "F", "H"),
    "W": ("G", "E"),
    "L": ("M", "K", "J"),
    "M": ("L", "K", "P", "O"),
    "E": ("G", "I", "W", "K", "N"),
    "N": ("E", "P", "Q"),
    "K": ("E", "P", "L", "M"),
    "P": ("K", "N", "M", "O", "S", "U"),
    "O": ("M", "U", "P", "V"),
    "U": ("O", "P", "V", "T"),
    "V": ("O", "U"),
    "T": ("U", "S"),
    "S": ("T", "P", "Q", "R"),
    "Q": ("N", "R", "S"),
    "R": ("Q", "S")
}
