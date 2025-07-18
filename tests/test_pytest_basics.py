# Basic pytest testing techniques applied to game functionality - demonstrates fixtures, assertions, and parametrization
import pytest
import pygame
import sys
import os

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from objects import Player, Enemy, Bullet, FastShootingBonus, BoostBonus
from scoreboard import add_score, load_scores
from settings import DIFFICULTY_SETTINGS

# Pytest Fixtures - setup/teardown code that runs before/after tests
@pytest.fixture
def pygame_init():
    """Initialize pygame for tests"""
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def player(pygame_init):
    """Create a player instance for testing"""
    return Player()

@pytest.fixture
def enemy(pygame_init):
    """Create an enemy instance for testing"""
    return Enemy()

# Basic Tests
def test_player_creation(player):
    """Test player is created with correct initial values"""
    assert player.lives == 3
    assert player.score == 0
    assert player.speed == 6  # PLAYER_BASE_SPEED

def test_bullet_moves_upward(pygame_init):
    """Test bullet moves in correct direction"""
    bullet = Bullet(100, 100)
    initial_y = bullet.rect.y
    bullet.update()
    assert bullet.rect.y < initial_y  # Bullet should move up (negative Y)

def test_enemy_spawns_within_bounds(enemy):
    """Test enemy spawns within screen boundaries"""
    assert 20 <= enemy.rect.x <= 670  # Within game boundaries

# Parametrized Tests - run same test with different inputs
@pytest.mark.parametrize("difficulty,expected_lives", [
    (1, 5),  # Easy
    (2, 3),  # Medium  
    (3, 2),  # Hard
    (4, 1),  # Expert
])
def test_difficulty_settings(difficulty, expected_lives):
    """Test each difficulty has correct settings"""
    settings = DIFFICULTY_SETTINGS[difficulty]
    assert settings['player_lives'] == expected_lives
    assert settings['max_enemies'] >= 1
    assert settings['score_multiplier'] >= 1

# Testing Exceptions
def test_invalid_difficulty_raises_error():
    """Test invalid difficulty level handling"""
    with pytest.raises(KeyError):
        invalid_settings = DIFFICULTY_SETTINGS[99]

# Bonus Type Tests
@pytest.mark.parametrize("bonus_class,expected_type", [
    (FastShootingBonus, "fast_shooting"),
    (BoostBonus, "boost"),
])
def test_bonus_types(pygame_init, bonus_class, expected_type):
    """Test bonus objects have correct types"""
    bonus = bonus_class()
    assert bonus.bonus_type == expected_type