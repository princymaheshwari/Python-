# Update Score 
# Write a function update_score() that takes in a dictionary scores that maps player names to current scores, a string player, and an integer points as parameters. The function adds the points to the current score of player in the dictionary and returns the updated dictionary. If the player does not exist in scores, then add them.

def update_score(scores, player: str, points: int):

    scores[player] = scores.get(player, 0) + points
    return scores
    

scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
update_score(scores, "Calvin", 20)
print(scores)
update_score(scores, "Calvin", 5)
print(scores)