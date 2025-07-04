import pytest

@pytest.fixture
def setup_demo():
    """Demo fixture to show setup/cleanup"""
    print("\n🔧 SETUP: Preparing test environment")
    yield "test_data"  # This value goes to your test
    print("🧹 CLEANUP: Cleaning up after test")

def test_with_fixture(setup_demo):
    """Test that uses the fixture"""
    print(f"🧪 TEST RUNNING: Got data = {setup_demo}")
    assert setup_demo == "test_data"

def test_without_fixture():
    """Test without fixture"""
    print("🧪 SIMPLE TEST: No setup needed")
    assert True