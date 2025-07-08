import pandas as pd
import json

def load_game_data():
    """Load game data for testing"""
    difficulties = {
        #'Easy': 'scores_easy.json',
        #'Medium': 'scores_medium.json', 
        'Hard': 'scores_hard.json'#,
        #'Expert': 'scores_expert.json'
    }
    
    all_scores = []
    for diff_name, filename in difficulties.items():
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                scores = json.load(f)
                print(f"🔍 DEBUG: {filename} contains {len(scores)} records")
                for score in scores:
                    score['difficulty'] = diff_name
                    all_scores.append(score)
                print(f"🔍 DEBUG: Added {len(scores)} records, total now: {len(all_scores)}")
        except FileNotFoundError:
            print(f"No data for {diff_name}")
    
    df = pd.DataFrame(all_scores)
    print(f"🔍 DEBUG: Final DataFrame has {len(df)} rows")
    return df

# Data Quality Tests
def test_data_completeness(df):
    """Test that essential columns exist and have data"""
    required_columns = ['name', 'score', 'date', 'difficulty']
    
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"
        assert not df[col].isna().all(), f"Column {col} is completely empty"
    
    print("✅ Data completeness test passed")

def test_data_validity(df):
    """Test that data values make sense"""
    # Scores should be non-negative
    assert df['score'].min() >= 0, f"Found negative score: {df['score'].min()}"
    
    # Scores shouldn't be impossibly high (adjust based on your game)
    assert df['score'].max() <= 10000, f"Suspiciously high score: {df['score'].max()}"
    
    # Valid difficulty levels
    valid_difficulties = ['Easy', 'Medium', 'Hard', 'Expert']
    invalid_diffs = df[~df['difficulty'].isin(valid_difficulties)]
    assert len(invalid_diffs) == 0, f"Invalid difficulties found: {invalid_diffs['difficulty'].unique()}"
    
    print("✅ Data validity test passed")

def test_data_consistency(df):
    """Test for logical consistency"""
    # Check for duplicate entries (same player, same score, same time)
    duplicates = df.duplicated(subset=['name', 'score', 'date'])
    assert not duplicates.any(), f"Found {duplicates.sum()} duplicate entries"
    
    # Names should be consistent (no typos)
    unique_names = df['name'].unique()
    print(f"📊 Found {len(unique_names)} unique player names: {list(unique_names)}")
    
    print("✅ Data consistency test passed")

def test_data_distribution(df):
    """Test data distribution for anomalies"""
    # Check for reasonable score distribution
    q1 = df['score'].quantile(0.25)
    q3 = df['score'].quantile(0.75)
    iqr = q3 - q1
    
    # Find extreme outliers (beyond 3*IQR)
    extreme_outliers = df[(df['score'] < q1 - 3*iqr) | (df['score'] > q3 + 3*iqr)]
    
    if len(extreme_outliers) > 0:
        print(f"⚠️  Found {len(extreme_outliers)} extreme outliers:")
        print(extreme_outliers[['difficulty', 'score', 'date']])
    else:
        print("✅ No extreme outliers found")

def format_scores_with_highlights(current_scores, correct_scores):
    """Format scores with highlighting for misplaced values"""
    result = []
    for i, score in enumerate(current_scores):
        if i < len(correct_scores) and score == correct_scores[i]:
            result.append(f"{score}")  # Correct position
        else:
            result.append(f"🔴{score}")  # Wrong position - red circle
    return "[" + ", ".join(result) + "]"

def test_scoreboard_order(df):
    """Test that scores are ordered correctly (highest first)"""
    for difficulty in df['difficulty'].unique():
        subset = df[df['difficulty'] == difficulty].reset_index(drop=True)
        
        # Check if scores are in descending order
        scores = subset['score'].tolist()
        sorted_scores = sorted(scores, reverse=True)
        
        if scores != sorted_scores:
            print(f"\n❌ {difficulty} SCOREBOARD ORDER ERROR:")
            print("=" * 50)
            print("CURRENT ORDER (what we have):")
            print(format_scores_with_highlights(scores, sorted_scores))
            print("\nCORRECT ORDER (what it should be):")
            print(format_scores_with_highlights(sorted_scores, sorted_scores))
            print("=" * 50)
            assert False, f"{difficulty}: Scoreboard order is incorrect"
    
    print("✅ Scoreboard ordering test passed")

def run_all_tests():
    """Run complete data quality test suite"""
    print("🧪 RUNNING DATA QUALITY TESTS")
    print("=" * 40)
    
    df = load_game_data()
    print(f"📊 Loaded {len(df)} game records")
    
    try:
        test_data_completeness(df)
        test_data_validity(df)
        test_data_consistency(df)
        test_data_distribution(df)
        test_scoreboard_order(df)
        
        print("\n🎉 ALL TESTS PASSED! Data quality looks good.")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    
    return True

if __name__ == "__main__":
    run_all_tests()