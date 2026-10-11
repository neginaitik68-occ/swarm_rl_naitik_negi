"""
SwarmRL Reward Engineering Module

Calculates rewards for individual drones searching
a simulated disaster zone.
"""

from pathlib import Path

import yaml


# Locate the configuration file relative to this Python file.
CONFIG_PATH = Path(__file__).with_name("reward_config.yaml")


def load_reward_config():
    """
    Load reward values from reward_config.yaml.

    Returns
    -------
    dict
        Reward configuration dictionary.
    """
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("Reward configuration must be a YAML mapping.")

    rewards = config.get("rewards")

    if not isinstance(rewards, dict):
        raise ValueError("Configuration must contain a 'rewards' mapping.")

    required_keys = {
        "coverage_reward",
        "collision_penalty",
        "boundary_penalty",
        "default_reward",
    }

    missing_keys = required_keys - rewards.keys()

    if missing_keys:
        raise ValueError(
            f"Missing reward configuration keys: {sorted(missing_keys)}"
        )

    for key in required_keys:
        value = rewards[key]

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"Reward value '{key}' must be numeric.")

    if rewards["collision_penalty"] > 0:
        raise ValueError("Collision penalty must be zero or negative.")

    if rewards["boundary_penalty"] > 0:
        raise ValueError("Boundary penalty must be zero or negative.")

    return rewards


def calculate_reward(
    discovered_new_cell=False,
    collision=False,
    boundary_violation=False,
):
    """
    Calculate a drone's reward for one time step.

    Parameters
    ----------
    discovered_new_cell : bool
        Whether the drone discovered a previously unexplored cell.

    collision : bool
        Whether a collision occurred.

    boundary_violation : bool
        Whether the drone violated the permitted boundary.

    Returns
    -------
    float
        Total reward for the time step.
    """
    config = load_reward_config()

    reward = config["default_reward"]

    if discovered_new_cell:
        reward += config["coverage_reward"]

    if collision:
        reward += config["collision_penalty"]

    if boundary_violation:
        reward += config["boundary_penalty"]

    return float(reward)