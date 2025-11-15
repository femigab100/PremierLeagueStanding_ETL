import pandas as pd

def transform_data(raw_json):
    #Transform raw API response into a clean DataFrame
    
    standings = raw_json["standings"][0]["table"]

    rows = []
    for team in standings:
        rows.append({
            "position": team["position"],
            "team": team["team"]["name"],
            "played_games": team["playedGames"],
            "won": team["won"],
            "draw": team["draw"],
            "lost": team["lost"],
            "points": team["points"],
            "goals_for": team["goalsFor"],
            "goals_against": team["goalsAgainst"],
            "goal_difference": team["goalDifference"]
        })

    df = pd.DataFrame(rows)
    return df
