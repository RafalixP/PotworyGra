# conftest.py - Shared pytest configuration and fixtures
import pytest
import pygame
import tempfile
import os

# Global fixtures available to all test files
@pytest.fixture(scope="session", autouse=True)
def pygame_setup():
    """Auto-use fixture that initializes pygame for all tests"""
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def temp_directory():
    """Create temporary directory for test files"""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Cleanup
    import shutil
    shutil.rmtree(temp_dir)

# Custom markers
def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")

# Pytest hooks for custom behavior
def pytest_collection_modifyitems(config, items):
    """Modify test collection - add markers automatically"""
    for item in items:
        # Auto-mark slow tests
        if "performance" in item.name or "collision_detection" in item.name:
            item.add_marker(pytest.mark.slow)
        
        # Auto-mark integration tests
        if "integration" in item.name or "scoreboard" in item.name:
            item.add_marker(pytest.mark.integration)
        else:
            item.add_marker(pytest.mark.unit)