from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

class Property:
    def __init__(self, number, name, houses, is_mortgaged, owner, purchase_price, rent, mortgage_value):
        self.number = number
        self.name = name
        self.houses = houses
        self.is_mortgaged = is_mortgaged
        self.owner = owner
        self.purchase_price = purchase_price
        self.rent = rent
        self.mortgage_value = mortgage_value

class Player:
    def __init__(self, name, budget, position):
        self.name = name
        self.budget = budget
        self.position = position
        self.total_purchase_amount = 0
        self.mortgage_value = 0
        self.taxes = 0
        self.go_money = 0
        self.initial_estimated_budget = 0

class Game:
    def __init__(self, properties, players):
        self.properties = properties
        self.players = players
    
    def get_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

def read_file(file_path, prices_path):
    games = []
    with open(file_path, 'r') as file:
        games_lines = file.readlines()

    with open(prices_path, 'r') as file:
        prices_lines = file.readlines()

    for i in range(0, len(games_lines), 32):
        properties = []
        for j in range(i, i + 28):
            game_values = games_lines[j].split(" ")
            prices_values = prices_lines[j % 28].split(" ")
            properties.append(Property(int(game_values[0]), game_values[1], int(game_values[2]), int(game_values[3]), game_values[4].split()[0] if len(game_values) == 5 else 'unowned', \
                              int(prices_values[2]), int(prices_values[3]), int(prices_values[4]))) # Additional data on [purchase cost, rent, amount for mortgage]

        players = []
        for j in range(i + 28, i + 32):
            game_values = games_lines[j].split(" ")
            players.append(Player(game_values[0], int(game_values[1]), int(game_values[2])))

        games.append(Game(properties, players))

    return games

def calculate_fluctuations(game):
    for prop in game.properties:
        # Money spent by each player to buy properties
        calculate_purchase_cost(game, prop)
        # Mortgage received
        calculate_mortgage(game, prop)

    for player in game.players:
        # Tax property
        calculate_taxes(player)
        # Go property
        calculate_go_property(player)

def calculate_purchase_cost(game, prop):
    if prop.owner != "unowned":
        player = game.get_player(prop.owner)
        player.total_purchase_amount += prop.purchase_price

def calculate_mortgage(game, prop):
    if prop.owner != "unowned" and prop.is_mortgaged:
        player = game.get_player(prop.owner)
        player.mortgage_value += prop.mortgage_value

def calculate_taxes(player):
    if player.position == 4:
        player.taxes = 200
    elif player.position == 38:
        player.taxes = 100

def calculate_go_property(player):
    if player.position <= 9:
        player.go_money += 200

def estimate_initial_budget(game):
    for player in game.players:
        # Add the budget after 5 turns
        player.initial_estimated_budget = player.budget

        # Add the purchases made by the player
        player.initial_estimated_budget += player.total_purchase_amount

        # Subtract the received mortgage
        player.initial_estimated_budget -= player.mortgage_value

        # Add the taxes paid at the last position
        player.initial_estimated_budget += player.taxes

        # Subtract the money received from a go property
        player.initial_estimated_budget -= player.go_money

def calculate_average_estimate(games):
    total_estimates = sum(player.initial_estimated_budget for game in games for player in game.players)
    return total_estimates / (len(games) * 4)

def get_estimated_budgets(games):
    budget_list = []
    for game in games:
        for player in game.players:
            budget_list.append(player.initial_estimated_budget)
    return budget_list

def display_estimated_budgets(game):
    for player in game.players:
        print(f"Name: {player.name}, Initial Estimated Budget: {player.initial_estimated_budget}")
    print("\n")
    return None

def main():
    games_path = './in.txt'
    prices_path = './prices.txt'
    game_list = read_file(games_path, prices_path)

    count = 0
    for game in game_list:
        calculate_fluctuations(game)
        estimate_initial_budget(game)

    average_initial_budget = calculate_average_estimate(game_list)

    diff_average = average_initial_budget - 1500

    for game in game_list:
        for player in game.players:
            player.initial_estimated_budget -= diff_average

    write_sum_to_file(game_list)


def write_sum_to_file(games, filename='out.txt'):
    with open(filename, 'w') as file:
        for game in games:
            # Calculate the mean of initial estimated budget for all players in the game
            avg_budget = sum(player.initial_estimated_budget for player in game.players) / 4
            avg_budget -= 250
            if avg_budget < 500:
                avg_budget = 500
            # Write the mean to the file
            file.write(f"{int(avg_budget)}\n")

def min_max_scaling(data, feature_range):
    X_min = np.min(data, axis=0)
    X_max = np.max(data, axis=0)

    scaled_data = feature_range[0] + (data - X_min) * (feature_range[1] - feature_range[0]) / (X_max - X_min)

    return scaled_data

if __name__ == "__main__":
    main()
    

