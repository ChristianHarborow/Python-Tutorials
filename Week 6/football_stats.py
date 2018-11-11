wins = 0
draws = 0
losses = 0
team = input("Enter the Team Name: ")

for match in range(1, 6):
    while True:
        try:
            scored = int(input("Goals scored in match #" + str(match) + ":  "))
            if scored >= 0:
                break
            else:
                print("Goals scored cannot be negative, try again")
        except ValueError:
            print("Goals scored must be an integer, try again")

    while True:
        try:
            conceded = int(input("Goals conceded in match #" + str(match) + ": "))
            if conceded >= 0:
                break
            else:
                print("Goals conceded cannot be negative, try again")
        except ValueError:
            print("Goals conceded must be an integer, try again")

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
