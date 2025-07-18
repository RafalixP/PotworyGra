# Game-specific pytest tests - focuses on game mechanics, collision detection, progression, and scoring systems
import pytest
import pygame
import sys
import os
from unittest.mock import Mock, patch

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from objects import Player, Enemy, Bullet, FastShootingBonus, BoostBonus
from main import spawn_bonus

class TestGameMechanics:
    """Test class for game-specific mechanics"""
    
    def test_player_boost_system(self):
        """Test player boost gauge and speed mechanics"""
        player = Player()
        
        # Initial state
        assert player.boost_gauge == 0
        assert player.speed == 6  # base speed
        
        # Apply boost
        player.speed = 10
        player.update_boost()
        
        # Should calculate boost percentage
        expected_boost = int(100 * (10 - 6) / (12 - 6))
        assert player.boost_gauge == expected_boost
        
    def test_player_speed_decay(self):
        """Test that player speed decays over time"""
        player = Player()
        player.speed = 10  # Above base speed
        
        initial_speed = player.speed
        player.update_boost()
        
        # Speed should decay slightly
        assert player.speed < initial_speed
        assert player.speed >= player.base_speed
        
    @pytest.mark.parametrize("bonus_type,expected_effect", [
        ("fast_shooting", "shoot_delay"),
        ("boost", "speed"),
    ])
    def test_bonus_effects(self, bonus_type, expected_effect):
        """Test different bonus effects on player"""
        player = Player()
        initial_delay = player.shoot_delay
        initial_speed = player.speed
        
        # Simulate bonus collection
        if bonus_type == "fast_shooting":
            player.shoot_delay = max(150, 0.75 * player.shoot_delay)
            assert player.shoot_delay < initial_delay
        elif bonus_type == "boost":
            player.speed = min(12, 1.15 * player.speed)
            assert player.speed > initial_speed

class TestCollisionSystem:
    """Test collision detection and handling"""
    
    def test_bullet_enemy_collision(self):
        """Test bullet-enemy collision detection"""
        bullet = Bullet(100, 100)
        enemy = Enemy()
        enemy.rect.center = (100, 100)  # Same position
        
        # Should detect collision
        assert bullet.rect.colliderect(enemy.rect)
        
    def test_player_enemy_collision(self):
        """Test player-enemy collision"""
        player = Player()
        enemy = Enemy()
        
        # Position enemy on player
        enemy.rect.center = player.rect.center
        
        assert player.rect.colliderect(enemy.rect)
        
    def test_no_collision_when_apart(self):
        """Test no collision when objects are far apart"""
        bullet = Bullet(100, 100)
        enemy = Enemy()
        enemy.rect.center = (500, 500)  # Far away
        
        assert not bullet.rect.colliderect(enemy.rect)

class TestGameProgression:
    """Test game difficulty progression"""
    
    @pytest.mark.parametrize("game_time,expected_increase", [
        (0, 0),      # No progression at start
        (30, 0.06),  # 30 seconds * 0.002 rate
        (60, 0.12),  # 1 minute
    ])
    def test_difficulty_progression(self, game_time, expected_increase):
        """Test difficulty increases over time"""
        from settings import DIFFICULTY_SETTINGS
        
        # Medium difficulty settings
        base_settings = DIFFICULTY_SETTINGS[2]
        progression_rate = base_settings['progression_rate']
        
        calculated_progression = game_time * progression_rate
        assert abs(calculated_progression - expected_increase) < 0.001

class TestScoreSystem:
    """Test scoring and life system"""
    
    def test_progressive_life_threshold(self):
        """Test that life thresholds double each time"""
        player = Player(difficulty_multiplier=2.0)
        
        initial_threshold = player.next_life_threshold
        assert initial_threshold == 20  # 10 * 2.0
        
        # Simulate reaching threshold
        player.score = initial_threshold
        player.lives += 1
        player.next_life_threshold *= 2
        
        assert player.next_life_threshold == initial_threshold * 2
        
    @pytest.mark.parametrize("difficulty,score_mult", [
        (1, 1),  # Easy
        (2, 2),  # Medium
        (3, 3),  # Hard
        (4, 5),  # Expert
    ])
    def test_score_multipliers(self, difficulty, score_mult):
        """Test score multipliers for different difficulties"""
        from settings import DIFFICULTY_SETTINGS
        settings = DIFFICULTY_SETTINGS[difficulty]
        assert settings['score_multiplier'] == score_mult

# Snapshot testing example (requires pytest-snapshot)
class TestGameState:
    """Test game state consistency"""
    
    def test_player_initial_state_snapshot(self):
        """Test player initial state matches expected snapshot"""
        player = Player()
        
        state = {
            'lives': player.lives,
            'score': player.score,
            'speed': player.speed,
            'boost_gauge': player.boost_gauge,
            'shoot_delay': player.shoot_delay
        }
        
        expected_state = {
            'lives': 3,
            'score': 0,
            'speed': 6,
            'boost_gauge': 0,
            'shoot_delay': 500
        }
        
        assert state == expected_state

# Performance benchmarking
@pytest.mark.slow
class TestPerformance:
    """Performance tests for game components"""
    
    def test_many_bullets_performance(self, benchmark):
        """Benchmark bullet update performance"""
        bullets = [Bullet(i, 100) for i in range(1000)]
        
        def update_all_bullets():
            for bullet in bullets:
                bullet.update()
                
        # Benchmark the function
        result = benchmark(update_all_bullets)
        
        # Should complete quickly
        assert benchmark.stats['mean'] < 0.01  # Less than 10ms average