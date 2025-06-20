import json
import os
from datetime import datetime

SCOREBOARD_FILE = "scores.json"

def load_scores():
    """Load scores from file, return empty list if file doesn't exist"""
    if os.path.exists(SCOREBOARD_FILE):
        try:
            with open(SCOREBOARD_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_scores(scores):
    """Save scores to file"""
    with open(SCOREBOARD_FILE, 'w', encoding='utf-8') as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)

def add_score(name, score):
    """Add new score and keep only top 100"""
    scores = load_scores()
    new_entry = {
        'name': name,
        'score': score,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    scores.append(new_entry)
    scores.sort(key=lambda x: x['score'], reverse=True)
    scores = scores[:100]  # Keep only top 100
    save_scores(scores)
    return scores

def get_top_scores():
    """Get top scores for display"""
    return load_scores()