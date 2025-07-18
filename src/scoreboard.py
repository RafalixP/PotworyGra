import json
import os
from datetime import datetime

# Get absolute paths to data files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

SCOREBOARD_FILES = {
    1: os.path.join(DATA_DIR, "scores_easy.json"),
    2: os.path.join(DATA_DIR, "scores_medium.json"), 
    3: os.path.join(DATA_DIR, "scores_hard.json"),
    4: os.path.join(DATA_DIR, "scores_expert.json")
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