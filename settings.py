WIDTH, HEIGHT = 600, 800
FPS = 60
DELAY_RESPAWN = 2000

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

PLAYER_BASE_SPEED = 6
PLAYER_MAX_SPEED = 12
PLAYER_SHOOT_DELAY = 500
PLAYER_ACCELERATION = 1.5  # Jak szybko przyspiesza (wyższe = mniej zauważalne)
PLAYER_FRICTION = 0.7     # Jak szybko zwalnia (0.7 wydaje się działać dobrze nawet przy boost 100%)

BULLET_SPEED = -10
ENEMY_SPEED = 2
BONUS_SPEED = 4
SPEED_DECAY = 0.0005  #     Speed decay for player boost

# Difficulty settings for each level
DIFFICULTY_SETTINGS = {
    1: {  # Easy
        'max_enemies': 1,
        'enemy_spawn_delay': 2000,
        'enemy_speed_multiplier': 1.0,
        'bonus_spawn_delay': 8000,
        'player_lives': 5,
        'score_multiplier': 1
    },
    2: {  # Medium
        'max_enemies': 2,
        'enemy_spawn_delay': 1500,
        'enemy_speed_multiplier': 1.3,
        'bonus_spawn_delay': 10000,
        'player_lives': 3,
        'score_multiplier': 2
    },
    3: {  # Hard
        'max_enemies': 3,
        'enemy_spawn_delay': 1000,
        'enemy_speed_multiplier': 1.6,
        'bonus_spawn_delay': 12000,
        'player_lives': 2,
        'score_multiplier': 3
    },
    4: {  # Expert
        'max_enemies': 4,
        'enemy_spawn_delay': 800,
        'enemy_speed_multiplier': 2.0,
        'bonus_spawn_delay': 15000,
        'player_lives': 1,
        'score_multiplier': 5
    }
}