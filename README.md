
# Movie watchers assignment.
The assignment reads three datasets - movies.dat, ratings.dat, users.dat - from the MovieLens dataset. The python code generates different reports based on Movie Ratings.

# Generated metrics.
## Top 20 movies list.
First, merge the three datasets - movies, users, ratings - into one dataset called “combine” and select all the records where movie rating is 5. The records are grouping on “MovieID” and count the number of users who rated 5 per movie. Then the records are sorted in descending order based on the number of users count and select the first 20 movies. 

The graph for the top 20 movies is below.
![top_20_movies.png](attachment:top_20_movies.png)


## The number of ratings on each rating.
First, create a new DataFrame with two columns - Rating, Number of ratings. From the combine DataFrame, select the records for each rating and count the number of ratings by using a For loop. The values for rating and number of ratings are inserted into the new DataFrame. 

The data in the visual form is below.
![ratingvsnumberofratings.png](attachment:ratingvsnumberofratings.png)


## The number of ratings on MovieID.
From the combine DataFrame, the records are grouping on “MovieID” and count the number of rating records. 

The graph for the number of ratings on MovieID is below.
![movieid_rating.png](attachment:movieid_rating.png)


## The number of ratings by UserID.
From the combine DataFrame, the records are grouping on “UserID” and count the number of rating records. 

The graph for the number of ratings by UserID is below.
![userid_rating.png](attachment:userid_rating.png)


# Dataset
https://grouplens.org/datasets/movielens/1m/ 

# Author
Anjuta Khongbantabam

# References
http://rpubs.com/Jango/486734



```python

```
# assignment
# assignment
