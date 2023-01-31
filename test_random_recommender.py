"""TODO
We want to write a program that checks wether 
our random_recommender works as we expect

We will use pytest

TDD (Test Driven Decvelopment) cycle:

0. Hypothesis: the random recommender works
1. we write test functions that 
make our program fails (disprove Hypothesis)
2. recode our random recommender 
so that our Hypothesis is proved
3. repeat

"""
from recommenders import get_random_recommendations

def test_2_movies():
    top_2 = get_random_recommendations(n=2)
    assert len(top_2) == 2


def test_20_movies():
    top_20 = get_random_recommendations(n=20)
    assert len(top_20) == 0


def test_is_movie_a_string():
    top_4 = get_random_recommendations(n=4)
    for movie in top_4:
        assert isinstance(movie,str)

