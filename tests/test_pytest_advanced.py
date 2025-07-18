# More advanced pytest testing techniques applied to game functionality - demonstrates fixtures, mocking, and performance testing
import pytest
import pygame
import tempfile
import os
import sys
from unittest.mock import Mock, patch, MagicMock

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from objects import Player, Enemy, Bullet
from scoreboard import add_score, load_scores, save_scores
from main import spawn_bonus

# Advanced Fixtures with scope and cleanup
@pytest.fixture(scope="session")
def pygame_session():
    """Session-scoped fixture - runs once for entire test session"""
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture(scope="function")
def temp_score_file():
    """Create temporary file for each test"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        temp_path = f.name
    yield temp_path
    os.unlink(temp_path)  # Cleanup

@pytest.fixture
def mock_pygame_time():
    """Mock pygame.time.get_ticks for consistent testing"""
    with patch('pygame.time.get_ticks', return_value=1000) as mock:
        yield mock

# Mocking and Patching
@patch('scoreboard.save_scores')
@patch('scoreboard.load_scores')
def test_add_score_with_mocks(mock_load, mock_save):
    """Test score addition with mocked file operations"""
    # Setup mock return value
    mock_load.return_value = [
        {'name': 'Player1', 'score': 50, 'date': '2024-01-01 10:00:00'}
    ]
    
    # Test the function
    result = add_score("TestPlayer", 100, 1)
    
    # Assertions
    assert result['name'] == "TestPlayer"
    assert result['score'] == 100
    assert 'date' in result
    
    # Verify mocks were called
    mock_load.assert_called_once_with(1)
    mock_save.assert_called_once()

# Property-based testing with hypothesis (if installed)
# pip install hypothesis
try:
    from hypothesis import given, strategies as st
    
    @given(st.integers(min_value=1, max_value=4))
    def test_all_difficulties_valid(pygame_session, difficulty):
        """Property test: all valid difficulties should work"""
        from settings import DIFFICULTY_SETTINGS
        settings = DIFFICULTY_SETTINGS[difficulty]
        assert settings['player_lives'] > 0
        assert settings['max_enemies'] > 0
        
except ImportError:
    # Skip hypothesis tests if not installed
    pass

# Custom Markers
@pytest.mark.slow
def test_performance_collision_detection(pygame_session):
    """Test collision detection performance - marked as slow"""
    import time
    
    bullets = [Bullet(i * 10, 100) for i in range(100)]
    enemies = [Enemy() for _ in range(50)]
    
    start_time = time.time()
    
    # Simulate collision detection
    collisions = 0
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                collisions += 1
                
    end_time = time.time()
    
    # Should complete quickly
    assert end_time - start_time < 0.1  # Less than 100ms
    
@pytest.mark.integration
def test_scoreboard_integration(temp_score_file):
    """Integration test for scoreboard functionality"""
    with patch('scoreboard.SCOREBOARD_FILES', {1: temp_score_file}):
        # Add multiple scores
        add_score("Player1", 100, 1)
        add_score("Player2", 200, 1)
        add_score("Player3", 150, 1)
        
        # Load and verify sorting
        scores = load_scores(1)
        assert len(scores) == 3
        assert scores[0]['score'] == 200  # Highest first
        assert scores[1]['score'] == 150
        assert scores[2]['score'] == 100

# Fixture with parameters
@pytest.fixture(params=[1, 2, 3, 4])
def difficulty_level(request):
    """Parametrized fixture - runs test for each difficulty"""
    return request.param

def test_player_with_all_difficulties(pygame_session, difficulty_level):
    """Test player creation with each difficulty level"""
    from settings import DIFFICULTY_SETTINGS
    multiplier = DIFFICULTY_SETTINGS[difficulty_level]['life_threshold_multiplier']
    player = Player(multiplier)
    
    expected_threshold = int(10 * multiplier)
    assert player.next_life_threshold == expected_threshold

# Testing with context managers
def test_player_movement_context(pygame_session):
    """Test player movement with proper context"""
    player = Player()
    initial_x = player.rect.x
    
    # Mock key presses
    keys = Mock()
    keys.__getitem__ = Mock(return_value=False)
    
    # Test no movement
    player.move(keys)
    assert player.rect.x == initial_x
    
    # Test right movement
    keys.__getitem__ = Mock(side_effect=lambda k: k == 275)  # RIGHT key
    player.move(keys)
    # Player should have some velocity but position might not change immediately
    assert player.velocity_x != 0

# Async testing (if needed for web version)
@pytest.mark.asyncio
async def test_async_bonus_spawn():
    """Test async bonus spawning (example for web version)"""
    # This would be for testing async functions
    bonus = spawn_bonus()  # Not actually async, but shows the pattern
    assert bonus.bonus_type in ["fast_shooting", "boost"]