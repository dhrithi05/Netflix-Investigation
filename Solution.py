# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# You'll want to subset the DataFrame to keep only the movies and then filter the years so that you are working with rows where the release year is between 1990 and 1999.

movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] <= 1999)]


# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

print("Duration of most frequent movie in the 1990s was " + str(duration))

# the filtering condition for action movies
action_movies = movies_1990s[movies_1990s["genre"] == "Action"]
short_movie_count = 0

#the iteration over DataFrame rows
for index, row in action_movies.iterrows():
    if row["duration"] <= 90:
        short_movie_count += 1

print("The number of short movies less than 90 minutes in 1990s is " + str(short_movie_count))
