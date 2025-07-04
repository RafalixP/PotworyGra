import unittest
import pygame
import tempfile
import os
from unittest.mock import Mock, patch
from main import spawn_bonus
from scoreboard import add_score, load_scores, save_scores

class TestGameIntegration(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.temp_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        pygame.quit()
        
    def test_bonus_spawning(self):
        """Test that bonus spawning returns valid bonus objects"""
        bonus = spawn_bonus()
        self.assertIn(bonus.bonus_type, ["fast_shooting", "boost"])
        
    def test_scoreboard_persistence(self):
        """Test complete scoreboard save/load cycle"""
        with patch('scoreboard.SCOREBOARD_FILES', {1: os.path.join(self.temp_dir, 'test_scores.json')}):
            # Add score
            entry = add_score("TestPlayer", 150, 1)
            
            # Load scores
            scores = load_scores(1)
            
            self.assertEqual(len(scores), 1)
            self.assertEqual(scores[0]['name'], "TestPlayer")
            self.assertEqual(scores[0]['score'], 150)
            
    def test_score_sorting(self):
        """Test that scores are properly sorted"""
        with patch('scoreboard.SCOREBOARD_FILES', {1: os.path.join(self.temp_dir, 'test_scores2.json')}):
            add_score("Player1", 100, 1)
            add_score("Player2", 200, 1)
            add_score("Player3", 150, 1)
            
            scores = load_scores(1)
            
            self.assertEqual(scores[0]['score'], 200)
            self.assertEqual(scores[1]['score'], 150)
            self.assertEqual(scores[2]['score'], 100)

class TestPerformance(unittest.TestCase):
    def test_collision_detection_performance(self):
        """Test collision detection with many objects"""
        from objects import Player, Bullet, Enemy
        
        player = Player()
        bullets = [Bullet(i * 10, 100) for i in range(50)]
        enemies = [Enemy() for _ in range(20)]
        
        # Simulate collision detection loop
        start_time = pygame.time.get_ticks()
        
        for bullet in bullets:
            for enemy in enemies:
                bullet.rect.colliderect(enemy.rect)
                
        end_time = pygame.time.get_ticks()
        
        # Should complete in reasonable time (< 10ms)
        self.assertLess(end_time - start_time, 10)

if __name__ == '__main__':
    unittest.main()