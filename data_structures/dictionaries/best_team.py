# Best team
# Your task is to write a function named team_with_best_average_score() that returns the team with the highest average score over a season.

# The function should accept a list of dictionaries named games as a parameter. Each dictionary represents data from a game, including the "team_name", and the "score" they achieved in that game. The function calculates the average score for each team across all games and returns the team with the highest average score.

def team_with_best_average_score(games):

    scores = {}
    for game in games:

        if game["team_name"] not in scores:
            scores[game["team_name"]] = []

        scores[game["team_name"]].append(game["score"])

    avg_scores = {team_name: (sum(score)/len(score)) for team_name, score in scores.items()}
    return max(avg_scores, key=avg_scores.get)
    

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]

print(team_with_best_average_score(games))