import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('WeeklyTimePlayingGames.csv')

# Handle missing values (replace NaN with mean for numeric columns)
df.fillna(df.mean(), inplace=True)

# Remove unnecessary columns (if any)
columns_to_keep = ['player_id', 'first_name', 'last_name', 'age', 'email', 'country', 'gender', 'favorite_game', 'weekly_hours']
df_cleaned = df[columns_to_keep]

# Rename columns
new_column_names = {'player_id': 'Player ID', 'first_name': 'First Name', 'last_name': 'Last Name',
                    'age': 'Age', 'email': 'Email', 'country': 'Country',
                    'gender': 'Gender', 'favorite_game': 'Favorite Game', 'weekly_hours': 'Weekly Hours'}
df_cleaned.rename(columns=new_column_names, inplace=True)

# Group by the "Favorite Game" column and calculate the total weekly hours
game_popularity = df.groupby("Favorite Game")["Weekly Hours"].sum()

# Create a 3D pie chart
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Plot the pie chart
ax.pie(game_popularity, labels=game_popularity.index, autopct="%1.1f%%", startangle=90)

# Set title and labels
ax.set_title("Popularity of Games")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

