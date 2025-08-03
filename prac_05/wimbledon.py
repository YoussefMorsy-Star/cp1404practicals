"""
Wimbledon Champions
"""

FILENAME = "wimbledon.csv"

def main():
    champions_to_wins, countries = process_wimbledon_data(FILENAME)
    print("Wimbledon Champions:")
    for champion, wins in champions_to_wins.items():
        print(f"{champion:20} {wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def process_wimbledon_data(filename):
    """Process the Wimbledon data and return champions with win counts and unique countries."""
    champions_to_wins = {}
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]

            champions_to_wins[champion] = champions_to_wins.get(champion, 0) + 1
            countries.add(country)

    return champions_to_wins, countries


if __name__ == '__main__':
    main()
