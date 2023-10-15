# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Read the csv file into a dataframe
df = pd.read_csv("WeeklyTimePlayingGames.csv")

# Print some basic statistics of the dataframe
print(df.describe())

# Group the dataframe by country and calculate the mean weekly hours
country_hours = df.groupby("country")["weekly_hours"].mean()

# Plot a bar chart of the mean weekly hours by country
country_hours.plot(kind="bar", title="Mean Weekly Hours by Country", xlabel="Country", ylabel="Hours")
plt.show()

# Group the dataframe by gender and calculate the percentage of gamers
gender_count = df.groupby("gender")["percentage_of_gamers"].sum()

# Plot a pie chart of the percentage of gamers by gender
gender_count.plot(kind="pie", title="Percentage of Gamers by Gender", autopct="%1.1f%%")
plt.show()

# Group the dataframe by favorite game and calculate the count of gamers
game_count = df.groupby("favorite_game")["percentage_of_gamers"].count()

# Plot a horizontal bar chart of the count of gamers by favorite game
game_count.plot(kind="bar", title="Count of Gamers by Favorite Game", xlabel="Count", ylabel="Game")
plt.show()
