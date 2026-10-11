"""Unit tests for the SwarmRL reward-engineering module."""

import unittest

from reward.rewards import calculate_reward, load_reward_config


class TestRewardConfiguration(unittest.TestCase):
    """Test reward configuration loading."""

    def test_configuration_loads(self):
        config = load_reward_config()

        self.assertIn("coverage_reward", config)
        self.assertIn("collision_penalty", config)
        self.assertIn("boundary_penalty", config)
        self.assertIn("default_reward", config)


class TestCalculateReward(unittest.TestCase):
    """Test reward calculations for different events."""

    def test_no_event(self):
        self.assertEqual(calculate_reward(), 0.0)

    def test_new_cell(self):
        self.assertEqual(
            calculate_reward(discovered_new_cell=True),
            1.0,
        )

    def test_collision(self):
        self.assertEqual(
            calculate_reward(collision=True),
            -100.0,
        )

    def test_boundary_violation(self):
        self.assertEqual(
            calculate_reward(boundary_violation=True),
            -5.0,
        )

    def test_new_cell_and_collision(self):
        self.assertEqual(
            calculate_reward(
                discovered_new_cell=True,
                collision=True,
            ),
            -99.0,
        )

    def test_collision_and_boundary_violation(self):
        self.assertEqual(
            calculate_reward(
                collision=True,
                boundary_violation=True,
            ),
            -105.0,
        )

    def test_all_events(self):
        self.assertEqual(
            calculate_reward(
                discovered_new_cell=True,
                collision=True,
                boundary_violation=True,
            ),
            -104.0,
        )


if __name__ == "__main__":
    unittest.main()