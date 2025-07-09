import pandas as pd
import json
import matplotlib.pyplot as plt

# Load your game scores
def load_game_data():
    difficulties = {
        'Easy': 'data/scores_easy.json',
        'Medium': 'data/scores_medium.json', 
        'Hard': 'data/scores_hard.json',
        'Expert': 'data/scores_expert.json'
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

# Uncomment to see boxplot visualization
# ax = df.boxplot(column='score', by='difficulty', figsize=(10, 6))
# plt.title('Your Game Scores by Difficulty')
# plt.ylabel('Score')
# plt.show()

#Time Analysis ⏰
# Convert dates and analyze playing patterns
df['date'] = pd.to_datetime(df['date'])
df['hour'] = df['date'].dt.hour
df['day_of_week'] = df['date'].dt.day_name()

# When do you play best?
print("\n=== WHEN DO YOU PLAY BEST? ===")
print("Average score by hour:")
print(df.groupby('hour')['score'].mean() ) # Reverse .sort_index(ascending=False)

print("\nAverage score by day:")
print(df.groupby('day_of_week')['score'].mean())

# Performance Trends 📈
print("\n=== PERFORMANCE TRENDS ===")
df['game_number'] = df.groupby('difficulty').cumcount() + 1
print("Game progression by difficulty:")
for difficulty in df['difficulty'].unique():
    subset = df[df['difficulty'] == difficulty]
    print(f"{difficulty}: {subset['game_number'].max()} games") #{subset['game_number'].min()}-

# Statistical Deep Dive 📊
print("\n=== STATISTICAL ANALYSIS ===")
print("Detailed stats by difficulty:")
print(df.pivot_table(values='score', index='difficulty', aggfunc=['mean', 'std', 'min', 'max', 'sum']))

# Outlier Detection
print("\n=== OUTLIER DETECTION ===")
Q1 = df['score'].quantile(0.25)
Q3 = df['score'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['score'] < Q1-1.5*IQR) | (df['score'] > Q3+1.5*IQR)]
print(f"Found {len(outliers)} outlier games:")
if len(outliers) > 0:
    print(outliers[['difficulty', 'score', 'date']].to_string())

# Recent Performance
print("\n=== RECENT PERFORMANCE ===")
recent_games = df[df['date'] > '2025-07-01']
print(f"Games since July 1st: {len(recent_games)}")
if len(recent_games) > 0:
    print(f"Recent average score: {recent_games['score'].mean():.1f}")
    print(f"Overall average score: {df['score'].mean():.1f}")