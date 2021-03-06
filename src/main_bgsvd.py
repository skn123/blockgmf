import numpy as np
import sys
import pandas
from bgsvd import factorize

args=list(sys.argv)
test_input =args[2]
train_input =args[1]
blocks=int(args[3])
steps = int(args[4])
gpu_steps = int(args[5])

train = pandas.read_csv(train_input).sort_values(by=['user_id','movie_id'])
test = pandas.read_csv(test_input).sort_values(by=['user_id','movie_id'])
users = train['user_id'].astype(int)
movies = train['movie_id'].astype(int)
ratings = train['rating']
test_users = test['user_id'].astype(int)
test_movies = test['movie_id'].astype(int)
test_ratings = test['rating']

factorize(users, movies, ratings, test_users, test_movies, test_ratings,blocks=blocks, latent=12, steps=steps, gpu_steps=gpu_steps, debug=2)
