import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
import random

"""
part 1
"""

player = pd.read_csv("basketball_players.csv")
master = pd.read_csv("basketball_master.csv")
player_master = pd.merge(player, master, how = "left", left_on = "playerID", right_on = "bioID")

print(master.columns)
print(player.columns)

#1
points_mean = player.points.mean()
print("1) Points mean: {}".format(points_mean))
print()

points_median = player.points.median()
print("1) Points median: {}".format(points_median))
print()

#2
points_highest = player.sort_values(by = "points", ascending = False)
#print(player_master[player_master.playerID == points_highest.iloc[0][0]])
print()
name = player_master[player_master.playerID == points_highest.iloc[0][0]].iloc[0]["useFirst"] ## question
surname = player_master[player_master.playerID == points_highest.iloc[0][0]].iloc[0]["lastName"]
print()
print("2) Point: {}, name: {} {}, playerID: {}, year: {}".format(points_highest.iloc[0][8], name, surname, points_highest.iloc[0][0], points_highest.iloc[0][1]))
print()

#3
three = player[["points", "assists", "rebounds"]]
#three_p = three.points.sum()
#three_a = three.assists.sum()
#three_r = three.rebounds.sum()
#three_total = [[three_p, three_a, three_r]]
#print(three_total)
three.plot(kind = "box", title = "3) Distribution of total points / assists / rebounds")
plt.ylabel("numbers")
plt.show()

#4
points_change = player.groupby("year").points.median()
print(points_change)
points_change.plot(kind = "line", c = "orange", title = "4) Points median time seires", label = "median score")
plt.legend()
plt.xlabel("Year")
plt.ylabel("points median")
plt.show()


"""
part 2
"""
#1

# egAttempted doesn't include ftAttempted
player1 = player[(player.fgAttempted > 0) & (player.ftAttempted)]
player1["points_eff"] = player1.points / (player1.fgAttempted + player1.ftAttempted)
player1 = player1[["playerID", "year", "points_eff", "fgAttempted", "ftAttempted"]]
points_efficient = player1.sort_values(by = "points_eff", ascending  = False).head(10)
print(points_efficient)
print()
print("{} is the most efficient goal maker.".format(points_efficient.iloc[0]["playerID"]))
print()

print("2")
print()

#top_player = []
#for player in player2_in_order:
#    if player.at[0, "playerID"] not in top_player:
#        while len(top_player) <= 10:
#            top_player.append(player.at[0, "playerID"])
#print(top_player)
# print(player2_in_order.iloc[0][0]) iloc doesn't go to index

# good at all area = best palyer

# exceptional accross many categories: PPG, RPG, APG, SPG
# points per game: PPG - points / GP (games played)
# rebound per game: RPG - rebounds / GP
# assists per game: APG - assists / GP
# steal per game: SPG - steals / GP

player["PPG"] = player.points / player.GP
player["RPG"] = player.rebounds / player.GP
player["APG"] = player.assists / player.GP
player["SPG"] = player.steals / player.GP

player2 = player[player.GP > 0]
#player2_in_order = player2.sort_values(by = "SPG", ascending = False)
#player2_in_order = player2_in_order.sort_values(by = "APG", ascending = False)
#player2_in_order = player2_in_order.sort_values(by = "RPG", ascending = False)
#player2_in_order = player2_in_order.sort_values(by = "PPG", ascending = False)
player2 = player2[["playerID", "year", "PPG", "RPG", "APG", "SPG"]]

player2["PPGRank"] = player2.PPG.rank(pct = True)
player2["RPGRank"] = player2.RPG.rank(pct = True)
player2["APGRank"] = player2.APG.rank(pct = True)
player2["SPGRank"] = player2.SPG.rank(pct = True)

print(player2[(player2.PPGRank > 0.95) & (player2.RPGRank > 0.95) & (player2.APGRank > 0.95) & (player2.SPGRank > 0.95)])
#print(player_master[player_master.playerID == player2_in_order.iloc[0][0]].iloc[0]["useFirst"], player_master[player_master.playerID == player2_in_order.iloc[0][0]].iloc[0]["lastName"])
print()

# 3

#three_points = player.groupby("year").threeAttempted.sum()
#three_points_made = player.groupby("year").threeMade.sum()
three_points1 = player[["year", "threeAttempted", "threeMade"]]
print(three_points1)
three_points1 = three_points1.groupby("year").sum()
three_points1.plot(kind  = "line")
#plt.show()

#three_points[three_points.index > 1970].plot(kind = "line")
plt.scatter(1977.8, 53, s = 50, c = "red")
plt.title("Three points attmpts & made trend")
plt.xlabel("Year")
plt.ylabel("counts")
plt.show()

# add who threw the most three attempt
most_three_player = player.groupby("playerID").threeAttempted.sum()
most_three_player = most_three_player.sort_values(ascending = False)
print(most_three_player.head(3))
print()
print("The three players threw that most three points shots are: ")
for i in range(3):
    print("{} {} - {} attempts".format(player_master[player_master.playerID == most_three_player.index[i]].iloc[0]["useFirst"], 
    player_master[player_master.playerID == most_three_player.index[i]].iloc[0]["lastName"], most_three_player[i]))
print()

# which position threw three points the most

print("Part 3 - 3")
positions = []
for i in player_master.pos:
    if i not in positions:
        positions.append(i)
print(positions)
print()
player_master1 = player_master[["pos", "threeAttempted"]]
print(player_master1)
three_positions = player_master1.groupby("pos").threeAttempted.sum()
print(three_positions)
three_positions.plot(kind = "bar")
plt.title("Three points throws by positions")
plt.xlabel("Positions")
plt.ylabel("Throws")
plt.show()
#three_positions = {}
#for i in positions:
#    three_positions[i] = player_master.grouby("pos").threeAteempted.sum()
#print(three_positions)
#for i in []
#three_positions = player_master.sort_values(by = "player_master.pos", ascending).

"""
part 3
"""

# 2 - birth country and position
# want to sort out that sum is bigger than 10 countries.
country = []
for i in master.birthCountry:
    if i not in country:
        country.append(i)
print(country)
print()
country_positions = {}
for i in country:
    country_positions[i] = master[master.birthCountry == i].pos.value_counts()
print(country_positions)
df = pd.DataFrame(country_positions)
df = df.fillna(0)
df1 = df.sum().sort_values(ascending = False)
df1 = df1[df1>=10]
subset_others = df[["YUG", "FRA", "CAN", "GER", "ESP", "AUS"]].drop(["pos", " G"])
subset_USA = df[["USA"]].drop(["pos"," G"])
subset_USA.plot(kind = "bar")
plt.show()
subset_others.plot(kind = "bar")
plt.legend(loc = 'upper center')
plt.show()

#df = df.reset_index()
#print(df)
#df1 = {}
#for i in df:
#    if df[i] >= 10:
#        df1[i] = df[i]
#print(df1)
df.plot()
#plt.show()

subset = player_master[["playerID", "pos", "birthCountry"]]
subset_country = subset.groupby("birthCountry").pos
print(subset_country)

# 1

player["PPG"] = player.points / player.GP
player["RPG"] = player.rebounds / player.GP
player["APG"] = player.assists / player.GP
player["SPG"] = player.steals / player.GP

player2 = player[player.GP > 0]
#player2_in_order = player2.sort_values(by = "SPG", ascending = False)
#player2_in_order = player2_in_order.sort_values(by = "APG", ascending = False)
#player2_in_order = player2_in_order.sort_values(by = "RPG", ascending = False)
#player2_in_order = player2_in_order.sort_values(by = "PPG", ascending = False)
player2 = player2[["playerID", "year", "PPG", "RPG", "APG", "SPG"]]

player2["PPGRank"] = player2.PPG.rank(pct = True)
player2["RPGRank"] = player2.RPG.rank(pct = True)
player2["APGRank"] = player2.APG.rank(pct = True)
player2["SPGRank"] = player2.SPG.rank(pct = True)

player_goat = player2[(player2.PPGRank > 0.90) & (player2.RPGRank > 0.90) & (player2.APGRank > 0.90) & (player2.SPGRank > 0.90)]
player_goat = player_goat.playerID.value_counts().head(5)
print(player_goat)

