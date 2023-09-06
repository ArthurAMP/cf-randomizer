import requests
import sys
import argparse
import random

url = 'https://codeforces.com/api/problemset.problems'

response = requests.get(url)
problems = response.json()['result']['problems']

def byRating(x):
    if 'rating' in x.keys():
        return x['rating'] == rating
    return False

if len(sys.argv) > 1:

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rating", help = "problem rating", type=int)

    args = parser.parse_args()
    rating = args.rating
    
    problems_filtered = list(filter(byRating, problems))
    problem_index = random.randint(0, len(problems_filtered)-1)
    print(problems_filtered[problem_index])
else:
    problem_index = random.randint(0, len(problems)-1)
    print(problems[problem_index])



