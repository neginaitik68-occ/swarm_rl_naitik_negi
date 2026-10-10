import unittest

from reward.rewards import calculate_reward


class TestRewardFunction(unittest.TestCase):

    def test_no_event(self):
        reward = calculate_reward()

        self.assertEqual(reward, 0.0)

    def test_new_cell_discovered(self):
        reward = calculate_reward(
            discovered_new_cell=True
        )

        self.assertEqual(reward, 1.0)

    def test_collision(self):
        reward = calculate_reward(
            collision=True
        )

        self.assertEqual(reward, -100.0)

    def test_boundary_violation(self):
        reward = calculate_reward(
            boundary_violation=True
        )

        self.assertEqual(reward, -5.0)

    def test_discovery_and_collision(self):
        reward = calculate_reward(
            discovered_new_cell=True,
            collision=True
        )

        self.assertEqual(reward, -99.0)


if __name__ == "__main__":
    unittest.main()