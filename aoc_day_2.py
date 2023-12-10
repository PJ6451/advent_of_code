import re

f = open("/Users/michaeljohnson/Downloads/input.txt", "r")
color_list = ["red", "green", "blue"]
game_max = []
for line in f:
    game = line.replace("\n", "").split(": ")
    max_colors = []
    for color in color_list:
        nums = re.findall(f"\d+ {color}", game[1])
        nums = [int(num.replace(f" {color}", "")) for num in nums]
        max_colors.append(max(nums))
    game_max.append(max_colors)

# Question 1
valid_game = [12, 13, 14]
valid_games = 0
for ind, game in enumerate(game_max):
    valid_flag = all([game[i] <= valid_game[i] for i in range(3)])
    if valid_flag:
        valid_games += ind + 1
print(valid_games)

# Question 2
power = 0
for game in game_max:
    total = 1
    for num in game:
        total *= num
    power += total
print(power)
