# 🚀 PotworyGra - Space Invaders Game

A Python-based space invaders game with comprehensive data analysis and quality testing features.

## 🎮 Features

### Game Features
- **4 Difficulty Levels**: Easy, Medium, Hard, Expert
- **Progressive Difficulty**: Enemies get faster and more numerous over time
- **Power-ups**: Speed boost and rapid fire bonuses
- **Persistent Scoreboards**: JSON-based score tracking per difficulty
- **Real-time Statistics**: Lives, score, boost gauge, timer

### Data Analysis Features
- **Performance Analytics**: Score trends, time patterns, difficulty analysis
- **Statistical Insights**: Mean, median, outliers, correlations
- **Data Visualization**: Boxplots, distribution charts
- **Time-based Analysis**: Best playing hours, day-of-week patterns

### Data Quality Testing
- **Automated Validation**: Data completeness, validity, consistency
- **Scoreboard Integrity**: Order verification with visual highlighting
- **Outlier Detection**: Statistical anomaly identification
- **Test-Driven Approach**: Comprehensive test suite with pytest

## 🛠️ Technologies Used

- **Python 3.12**
- **Pygame** - Game engine and graphics
- **Pandas** - Data manipulation and analysis
- **Matplotlib/Seaborn** - Data visualization
- **Pytest** - Testing framework
- **JSON** - Data persistence

## 📁 Project Structure

```
PotworyGra/
├── src/                    # Source code
│   ├── main.py            # Main game loop
│   ├── objects.py         # Game objects (Player, Enemy, Bullet)
│   ├── ui.py              # User interface and menus
│   ├── settings.py        # Game configuration
│   └── assets.py          # Game assets and graphics
├── data/                  # Data files
│   ├── scores_easy.json   # Easy mode scores
│   ├── scores_medium.json # Medium mode scores
│   ├── scores_hard.json   # Hard mode scores
│   └── scores_expert.json # Expert mode scores
├── analysis/              # Data analysis scripts
│   ├── analyze_scores.py  # Main analysis script
│   └── data_testing.py    # Data quality tests
├── tests/                 # Test suite
│   ├── test_game.py       # Game logic tests
│   ├── test_pytest_*.py   # Pytest examples
│   └── conftest.py        # Test configuration
└── docs/                  # Documentation
    └── screenshots/       # Game screenshots
```

## 🚀 Quick Start

### Prerequisites
```bash
pip install pygame pandas matplotlib seaborn pytest
```

### Run the Game
```bash
python src/main.py
```

### Run Data Analysis
```bash
python analysis/analyze_scores.py
```

### Run Tests
```bash
pytest tests/ -v
```

### Run Data Quality Tests
```bash
python analysis/data_testing.py
```

## 📊 Data Analysis Examples

### Performance Trends
```python
# Analyze playing patterns
df.groupby('hour')['score'].mean()  # Best playing hours
df.groupby('day_of_week')['score'].mean()  # Best days
```

### Statistical Analysis
```python
# Outlier detection using IQR method
Q1 = df['score'].quantile(0.25)
Q3 = df['score'].quantile(0.75)
outliers = df[(df['score'] < Q1-1.5*IQR) | (df['score'] > Q3+1.5*IQR)]
```

## 🧪 Testing Features

### Data Quality Tests
- **Completeness**: Verify all required fields exist
- **Validity**: Check data ranges and formats
- **Consistency**: Detect duplicates and naming issues
- **Order Verification**: Ensure scoreboards are properly sorted

### Game Logic Tests
- **Unit Tests**: Individual component testing
- **Integration Tests**: Full game flow testing
- **Performance Tests**: Collision detection optimization

## 🎯 Game Controls

- **Arrow Keys**: Move player
- **Spacebar**: Shoot
- **ESC**: Pause/Exit
- **1-4**: Select difficulty (main menu)

## 📈 Difficulty Progression

| Difficulty | Enemies | Lives | Score Multiplier | Progression Rate |
|------------|---------|-------|------------------|------------------|
| Easy       | 1       | 5     | 1x               | None             |
| Medium     | 2       | 3     | 2x               | Slow             |
| Hard       | 3       | 2     | 3x               | Medium           |
| Expert     | 4       | 1     | 5x               | Fast             |

## 🔧 Configuration

Game settings can be modified in `src/settings.py`:
- Screen dimensions
- Player speed and acceleration
- Enemy spawn rates
- Bonus frequencies
- Difficulty parameters

## 📝 Development Notes

This project demonstrates:
- **Game Development**: Object-oriented design, game loops, collision detection
- **Data Engineering**: ETL processes, data validation, quality testing
- **Data Analysis**: Statistical analysis, visualization, trend identification
- **Software Testing**: Unit tests, integration tests, test-driven development
- **Code Organization**: Modular design, separation of concerns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🎮 Screenshots

*Add screenshots of the game, data analysis charts, and test results here*

---

**Built with ❤️ as a learning project combining game development, data analysis, and software engineering best practices.**