import pandas as pd

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

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('Cleaned_WeeklyTimePlayingGames.csv', index=False)

print("CSV file cleaned and saved as Cleaned_WeeklyTimePlayingGames.csv")
