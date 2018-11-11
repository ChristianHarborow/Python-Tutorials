wins = 0
draws = 0
losses = 0
team = input("Enter the Team Name: ")

for match in range(1, 6):
    scored = int(input("Goals scored in match #" + str(match) + ":  "))
    conceded = int(input("Goals against in match #" + str(match) + ": "))
    if scored > conceded:
        wins += 1
    elif scored == conceded:
        draws += 1
    else:
        losses += 1

points = wins * 3 + draws
print("\n" + team)
print("Wins:   " + str(wins))
print("Draws:  " + str(draws))
print("Losses: " + str(losses))
print("Points: " + str(points))
