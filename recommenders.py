"""
Here we define our function for the recommender system
"""

from utils import MOVIES
import random

def hello_recommender():
    print('hello')

def get_random_recommendations(n):
    if n <= len(MOVIES):
        random.shuffle(MOVIES)
        top_n = MOVIES[:n]
        return top_n
    else:
        print(f"n cannot be larger than {len(MOVIES)}\nbut equal or smaller")
        return []

        
if __name__ == "__main__":
    top_3 = get_random_recommendations(3)
    print(top_3)
