import pandas as pd
import matplotlib.pyplot as plt

# Read the data from a CSV file
df = pd.read_csv("WeeklyTimePlayingGames.csv")

# clean data
age = df["age"].tolist()
df = df[df["age"] < 60]
index = pd.read_csv("WeeklyTimePlayingGames.csv")
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
games_counts = df['favorite_game'].value_counts()

# Create a pie chart
plt.pie(games_counts, labels=games_counts.index, autopct='%1.1f%%')
plt.axis('equal')  # Ensure the chart is circular
plt.title('Favorite Games by Country')  # Chart title
plt.show()

