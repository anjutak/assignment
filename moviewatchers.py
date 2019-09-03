# Anjuta Khongbantabm, 02.09.2019.
# This code generates Movies title, genres,.....for rating 5.
# It generates top 100 movies based on number of user counts.
# It generates number of ratings on each rating.
# It generates number of ratings on MovieID.
# It generates number of ratings by UserID.

import pandas as pd

def dataset_reader(dataset, columns):
    df = pd.read_csv(dataset, names = columns, sep="::", engine="python")
    return df

movies_columns = ("MovieID", "Title", "Genres")
movies = dataset_reader("movies.dat", movies_columns)

ratings_columns = ("UserID", "MovieID", "Rating", "Timestamp")
ratings = dataset_reader("ratings.dat", ratings_columns)

users_columns = ("UserID", "Gender", "Age", "Occupation", "Zip-code")
users = dataset_reader("users.dat", users_columns)

movies_ratings = pd.merge(movies, ratings, on = "MovieID")
combine = pd.merge(movies_ratings, users, on = "UserID")

# Rating 5 record.
movie_review_5 = ratings[ratings["Rating"] == 5]
movies_ratings_5 = pd.merge(movies, movie_review_5, on = "MovieID")
movies_ratings_5_groupby = movies_ratings_5.groupby(["MovieID", "Title", "Genres", "Rating"], as_index=False)["UserID"].count()
movies_ratings_5_groupby.rename(columns={"UserID":"User_Count"}, inplace=True)
movies_ratings_5_sort_df = movies_ratings_5_groupby.sort_values(["User_Count"], ascending=False)
movies_ratings_5_reindex_df = movies_ratings_5_sort_df.reset_index(drop=True)
movies_ratings_5_reindex_df.to_csv("Ratings_5_movies_records.csv")

# Top 20 movies record.
top_20_movies = movies_ratings_5_reindex_df.head(20)
top_20_movies.to_csv("top_20_movies.csv")

# Number of ratings on each rating.
df = pd.DataFrame(columns=["Rating", "Number of ratings"])
index = 0
for i in range(1,6):
    rating = combine[combine["Rating"]==i].count()[0]
    print(rating)
    df.loc[index, ["Rating"]] = i
    df.loc[index, ["Number of ratings"]] = rating
    index+= 1
df.to_csv("rating_with_number_of_ratings.csv") 

# Number of ratings on MovieID.
movieid_rating = combine.groupby(["MovieID"])["Rating"].count()
movieid_rating.to_frame().to_csv("movieid_rating.csv")

# Number of ratings by UserID.
userid_rating = combine.groupby(["UserID"])["Rating"].count()
userid_rating.to_frame().to_csv("userid_rating.csv")

