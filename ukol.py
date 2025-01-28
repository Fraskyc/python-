def parse_game_data(game_data):
    """Parse the game data into a structured format."""
    games = []
    for line in game_data.splitlines():
        line = line.strip()
        if not line:  
            continue

        game_id, subsets = line.split(":")
        game_id = int(game_id.split()[1])  
        subsets = subsets.strip().split(";")


        parsed_subsets = []
        for subset in subsets:
            colors = subset.strip().split(", ")
            parsed_subset = {}
            for color in colors:
                count, color_name = color.split()
                parsed_subset[color_name] = int(count)
            parsed_subsets.append(parsed_subset)

        games.append((game_id, parsed_subsets))
    return games

def is_game_possible(game, max_cubes):
    """Check if a game is possible given the maximum cube limits."""
    for subset in game:
        for color, count in subset.items():
            if count > max_cubes.get(color, 0):
                return False
    return True

def sum_possible_game_ids(game_data, max_cubes):
    """Calculate the sum of game IDs that are possible given cube limits."""
    games = parse_game_data(game_data)
    possible_game_ids = []

    for game_id, subsets in games:
        if is_game_possible(subsets, max_cubes):
            possible_game_ids.append(game_id)

    return sum(possible_game_ids)

example_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

result = sum_possible_game_ids(example_data, max_cubes)
print("Sum of possible game IDs:", result)
