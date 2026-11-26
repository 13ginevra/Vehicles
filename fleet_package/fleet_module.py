# Toy nested dictionary data using direct shorthand keys
vehicles = {
    "moto": {
        "ITALIA NORD-OCCIDENTALE": {
            "Fino a 125": {"0": 198580, "1": 48882},
            "126 - 250": {"0": 134064, "1": 60332},
            "251 - 750": {"0": 178233, "1": 55234},
            "Oltre 750": {"0": 51039, "1": 39103}
        },
        "ITALIA NORD-ORIENTALE": {
            "Fino a 125": {"0": 159880, "1": 38063},
            "126 - 250": {"0": 95346, "1": 36822},
            "251 - 750": {"0": 135378, "1": 38650},
            "Oltre 750": {"0": 43082, "1": 35582}
        }
    },
    "bus": {
        "ITALIA NORD-OCCIDENTALE": {
            "Noleggio": {"0": 240, "1": 51, "5B": 120, "6B": 45},
            "Privato": {"0": 433, "1": 83},
            "Pubblico": {"0": 404, "1": 31},
            "Altri usi": {"0": 53, "1": 2}
        },
        "ITALIA NORD-ORIENTALE": {
            "Noleggio": {"0": 270, "1": 81},
            "Privato": {"0": 278, "1": 59},
            "Pubblico": {"0": 272, "1": 19},
            "Altri usi": {"0": 19, "1": 7}
        }
    }
}

def get_top_vehicle_counts_by_euro_limit(vehicle_type, max_euro_standard, top_n):
    """Print the top N vehicle counts up to a maximum Euro standard.

    Keyword arguments:
    vehicle_type -- type of vehicle, e.g. "moto" or "bus"
    max_euro_standard -- highest Euro standard to include, e.g. "1"
    top_n -- number of records to print

    Records of every area and category are filtered by vehicle type and
    Euro standard, then sorted by vehicle count in descending order.

    If fewer than top_n records match, all of them are printed.
    """

    limit = euro_rank(max_euro_standard)
    records = []

    for area, categories in vehicles[vehicle_type].items():
        for category, counts in categories.items():
            for standard, count in counts.items():
                if euro_rank(standard) <= limit:
                    records.append((count, area, category, standard))

    records.sort(reverse=True)  # the count is first, so it sorts by count

    for count, area, category, standard in records[:top_n]:
        print(f"There are {count} {vehicle_type} vehicles in {area} "
              f"(category: {category}, Euro std: EURO {standard}).")