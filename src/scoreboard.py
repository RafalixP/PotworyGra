import json
import os
from datetime import datetime

SCOREBOARD_FILES = {
    1: "../data/scores_easy.json",
    2: "../data/scores_medium.json", 
    3: "../data/scores_hard.json",
    4: "../data/scores_expert.json"
}

DIFFICULTY_NAMES = {
    1: "Łatwy",
    2: "Średni",
    3: "Trudny", 
    4: "Expert"
}

def load_scores(difficulty):
    """Load scores from file for specific difficulty"""
    filename = SCOREBOARD_FILES.get(difficulty, SCOREBOARD_FILES[2])
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_scores(scores, difficulty):
    """Save scores to file for specific difficulty"""
    filename = SCOREBOARD_FILES.get(difficulty, SCOREBOARD_FILES[2])
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)

def add_score(name, score, difficulty):
    """Add new score and keep only top 100 for specific difficulty"""
    scores = load_scores(difficulty)
    new_entry = {
        'name': name,
        'score': score,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    scores.append(new_entry)
    scores.sort(key=lambda x: x['score'], reverse=True)
    scores = scores[:100]  # Keep only top 100
    save_scores(scores, difficulty)
    return new_entry

def get_top_scores(difficulty):
    """Get top scores for display for specific difficulty"""
    return load_scores(difficulty)