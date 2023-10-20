import pandas as pd
import matplotlib.pyplot as plt

# Read the data from a CSV file
df = pd.read_csv("WeeklyTimePlayingGames_filtered.csv")

# clean data
age = df["age"].tolist()
df = df[df["age"] < 46]
index = pd.read_csv("WeeklyTimePlayingGames_filtered.csv")
df.to_csv('file_output.csv', index=False)
df = pd.read_csv('file_output.csv')

# Create a bar chart
weekly_hours = df["weekly_hours"].tolist()
country = df["country"].tolist()
x_axis = ['country']
y_axis = ['weekly_hours']
plt.figure(figsize=(10, 6))
plt.bar(country, weekly_hours)
plt.title('weekly hours playing video games')
plt.xlabel('country')
plt.ylabel('weekly_hours')
plt.xticks(rotation=90)
plt.show()

# Group by 'favorite_game' and count occurrences
games_counts = df['games'].value_counts()

# Create a pie chart
plt.pie(games_counts, labels=games_counts.index, autopct='%1.1f%%')
plt.axis('equal')  # Ensure the chart is circular
plt.title('Favorite Games by Country')  # Chart title
plt.show()

# Question 1: What is the average age of the gamers?
# Calculate the mean of the age column
avg_age = df["age"].mean()

# Print the average age
print(f"The average age of the gamers is {avg_age:.2f} years.")

# Question 2: Is there any gender predominance in the playing Minecraft, Super Mario Odyssey and The Legend of Zelda: Breath of the Wild?
# Filter the dataframe by the games column and group by the gender column
games = ["Minecraft", "Super Mario Odyssey", "The Legend of Zelda: Breath of the Wild"]
df_games = df[df["games"].isin(games)].groupby("gender")

# Plot a stacked bar chart with the counts of each gender for each game
plt.figure(figsize=(8, 6))
df_games["games"].value_counts().unstack().plot.bar(stacked=True)
plt.ylabel("Count")
plt.title("Gender predominance in playing " + ", ".join(games))
plt.legend(title="Games")
plt.show()

# Question 3: What is the average weekly time spent playing games by all gamers in this data set?
# Calculate the mean of the weekly_hours column
avg_hours = df["weekly_hours"].mean()

# Plot a pie chart with the average weekly hours and the remaining hours in a week
plt.figure(figsize=(6, 6))
plt.pie([avg_hours, 168 - avg_hours], labels=["Average weekly hours", "Remaining hours"], autopct="%1.1f%%")
plt.title("Average weekly time spent playing games by all gamers")
plt.show()

# Question 4: Which country has the highest representation of gamers in this data set?
# Group the dataframe by the country column and count the number of players
df_country = df.groupby("country")["player_id"].count()

# Plot a horizontal bar chart with the counts of each country
plt.figure(figsize=(8, 8))
df_country.sort_values(ascending=True).plot.barh()
plt.xlabel("Count")
plt.title("Representation of gamers by country")
plt.show()

# Question 5: What is the most popular game among female gamers?
# Filter the dataframe by the gender column and group by the games column
df_female = df[df["gender"] == "Female"].groupby("games")

# Plot a pie chart with the counts of each game
plt.figure(figsize=(6, 6))
df_female["player_id"].count().plot.pie(autopct="%1.1f%%")
plt.title("Most popular game among female gamers")
plt.show()

# Question 6: How much time on average do gamers spend playing Grand Theft Auto V per week?
# Filter the dataframe by the games column and calculate the mean of the weekly_hours column
avg_gta = df[df["games"] == "Grand Theft Auto V"]["weekly_hours"].mean()

# Print the average weekly hours for Grand Theft Auto V
print(f"The average weekly time spent playing Grand Theft Auto V is {avg_gta:.2f} hours.")

# Question 7: Which game do gamers from the Philippines play most frequently?
# Filter the dataframe by the country column and group by the games column
df_philippines = df[df["country"] == "Philippines"].groupby("games")

# Plot a pie chart with the counts of each game
plt.figure(figsize=(6, 6))
df_philippines["player_id"].count().plot.pie(autopct="%1.1f%%")
plt.title("Most frequently played game by gamers from the Philippines")
plt.show()

# Question 8: Is there an age group that prefers Super Mario Odyssey over other games?
# Filter the dataframe by the games column and group by the age column
df_smo = df[df["games"] == "Super Mario Odyssey"].groupby("age")

# Plot a histogram with the counts of each age group
plt.figure(figsize=(8, 6))
df_smo["player_id"].count().plot.hist(bins=10)
plt.xlabel("Age (years)")
plt.title("Age distribution of Super Mario Odyssey players")
plt.show()

# Question 9: How many gamers have email addresses registered with .com domain?
# Filter the dataframe by the email column and count the number of players
df_com = df[df["email"].str.endswith(".com")]["player_id"].count()

# Print the count of .com email addresses
print("Number of gamers with .com email addresses:", df_com)

# Question 10: Are there any correlations between the age of gamers and the weekly time they spend playing games?
# Plot a scatter plot with the age and weekly_hours columns
plt.figure(figsize=(8, 6))
plt.scatter(df["age"], df["weekly_hours"])
plt.xlabel("Age (years)")
plt.ylabel("Weekly hours")
plt.title("Correlation between age and weekly time spent playing games")
plt.show()

# Bonus question: How does Fortnite's popularity among female gamers compare to its popularity among male gamers?
# Filter the rows where games column contains Fortnite
df = df[df["games"].str.contains("Fortnite")]

# Group the data by gender and calculate the mean weekly hours
df = df.groupby("gender")["weekly_hours"].mean()

# Plot a bar chart with gender as x-axis and mean weekly hours as y-axis
df.plot(kind="bar", x="gender", y="weekly_hours", title="Average weekly hours of playing Fortnite by gender")
plt.xlabel("Gender")
plt.ylabel("Weekly hours")
plt.show()
