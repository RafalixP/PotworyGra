import pandas as pd
import json
import matplotlib.pyplot as plt

# Load your game scores
def load_game_data():
    difficulties = {
        'Easy': 'scores_easy.json',
        'Medium': 'scores_medium.json', 
        'Hard': 'scores_hard.json',
        'Expert': 'scores_expert.json'
    }
    
    all_scores = []
    for diff_name, filename in difficulties.items():
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                scores = json.load(f)
                for score in scores:
                    score['difficulty'] = diff_name
                    all_scores.append(score)
        except FileNotFoundError:
            print(f"No data for {diff_name}")
    
    return pd.DataFrame(all_scores)

# Analyze the data
df = load_game_data()
print("=== YOUR GAME ANALYSIS ===")
print(f"Total games played: {len(df)}")
print(f"Difficulties played: {df['difficulty'].unique()}")
print(f"Best score: {df['score'].max()}")
print(f"Average score: {df['score'].mean():.1f}")

# Score by difficulty
print("\n=== SCORES BY DIFFICULTY ===")
print(df.groupby('difficulty')['score'].agg(['count', 'mean', 'max']))

# Simple visualization
#plt.figure(figsize=(10, 6))
df.boxplot(column='score', by='difficulty')
plt.title('Your Game Scores by Difficulty')
plt.ylabel('Score')
plt.show()