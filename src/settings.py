WIDTH, HEIGHT = 690, 800
FPS = 60
DELAY_RESPAWN = 1000

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
SPEED_DECAY = 0.0005  #     Speed decay for player boost - jak szybko "znika" speed boost

# Difficulty settings for each level
DIFFICULTY_SETTINGS = {
    1: {  # Easy - No progression
        'max_enemies': 1,
        'enemy_spawn_delay': 2000,
        'enemy_speed_multiplier': 1.0,
        'bonus_spawn_delay': 8000,
        'player_lives': 5,
        'score_multiplier': 1,
        'progression_rate': 0.0,  # No progression on easy
        'life_threshold_multiplier': 1.0
    },
    2: {  # Medium - Slow progression
        'max_enemies': 2,
        'enemy_spawn_delay': 1500,
        'enemy_speed_multiplier': 1.3,
        'bonus_spawn_delay': 10000,
        'player_lives': 3,
        'score_multiplier': 2,
        'progression_rate': 0.002,  # Slow progression
        'life_threshold_multiplier': 1.5
    },
    3: {  # Hard - Medium progression
        'max_enemies': 3,
        'enemy_spawn_delay': 1000,
        'enemy_speed_multiplier': 1.6,
        'bonus_spawn_delay': 12000,
        'player_lives': 2,
        'score_multiplier': 3,
        'progression_rate': 0.004,  # Medium progression
        'life_threshold_multiplier': 2.0
    },
    4: {  # Expert - Fast progression
        'max_enemies': 4,
        'enemy_spawn_delay': 800,
        'enemy_speed_multiplier': 2.0,
        'bonus_spawn_delay': 15000,
        'player_lives': 1,
        'score_multiplier': 5,
        'progression_rate': 0.006,  # Fast progression
        'life_threshold_multiplier': 3.0
    }
}