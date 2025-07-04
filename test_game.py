import unittest
import pygame
from unittest.mock import Mock, patch
from objects import Player, Enemy, Bullet, FastShootingBonus, BoostBonus
from scoreboard import add_score, load_scores
from settings import DIFFICULTY_SETTINGS

class TestGameObjects(unittest.TestCase):
    def setUp(self):
        pygame.init()
        
    def test_player_movement_boundaries(self):
        player = Player()
        player.rect.x = 0
        keys = Mock()
        keys.__getitem__ = Mock(side_effect=lambda k: k == 276)  # LEFT key
        
        player.move(keys)
        self.assertGreaterEqual(player.rect.x, 0)
        
    def test_bullet_movement(self):
        bullet = Bullet(100, 100)
        initial_y = bullet.rect.y
        bullet.update()
        self.assertLess(bullet.rect.y, initial_y)
        
    def test_enemy_spawning(self):
        enemy = Enemy()
        self.assertGreaterEqual(enemy.rect.x, 20)
        self.assertLessEqual(enemy.rect.x, 670)
        
    def test_bonus_effects(self):
        player = Player()
        initial_delay = player.shoot_delay
        
        # Test fast shooting bonus
        bonus = FastShootingBonus()
        self.assertEqual(bonus.bonus_type, "fast_shooting")
        
        # Test boost bonus
        boost = BoostBonus()
        self.assertEqual(boost.bonus_type, "boost")

class TestScoreboard(unittest.TestCase):
    @patch('scoreboard.save_scores')
    @patch('scoreboard.load_scores')
    def test_add_score(self, mock_load, mock_save):
        mock_load.return_value = []
        
        result = add_score("Test", 100, 1)
        
        self.assertEqual(result['name'], "Test")
        self.assertEqual(result['score'], 100)
        self.assertIn('date', result)
        
    def test_difficulty_settings(self):
        for difficulty in [1, 2, 3, 4]:
            settings = DIFFICULTY_SETTINGS[difficulty]
            self.assertIn('max_enemies', settings)
            self.assertIn('player_lives', settings)
            self.assertGreater(settings['player_lives'], 0)

if __name__ == '__main__':
    unittest.main()