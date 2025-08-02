def calculate_print_cost(pages, copies, color, paper):
    base_rate = 0.01  # Grundkosten pro Seite
    color_multiplier = 1.5 if color == "Farbe" else 1.0
    paper_multiplier = {
        "Normal": 1.0,
        "Hochglanz": 1.2,
        "Recycling": 0.9
    }.get(paper, 1.0)

    return round(pages * copies * base_rate * color_multiplier * paper_multiplier, 2)
