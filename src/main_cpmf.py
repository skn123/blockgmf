import numpy as np
import sys
import pandas
from cpmf import factorize

args=list(sys.argv)
test_input =args[2]
train_input =args[1]
steps = int(args[3])
blocks = int(args[4])

train = pandas.read_csv(train_input).sort_values(by=['user_id','movie_id'])
test = pandas.read_csv(test_input).sort_values(by=['user_id','movie_id'])
users = train['user_id'].astype(int)
movies = train['movie_id'].astype(int)
ratings = train['rating']
test_users = test['user_id'].astype(int)
test_movies = test['movie_id'].astype(int)
test_ratings = test['rating']

factorize(users, movies, ratings, test_users, test_movies, test_ratings, latent=30, blocks=blocks, steps=steps, alpha=0.0002, beta=0.01, delta=0.01)
