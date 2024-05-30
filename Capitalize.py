# Complete the solve function below.
def solve(s):
    x = s.split(" ")
    capitalized_words = [word.capitalize() for word in x]
    return ' '.join(capitalized_words)