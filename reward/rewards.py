"""
SwarmRL Reward Engineering Module

Initial reward function for a drone swarm searching
a simulated disaster zone.
"""
#initial reward values

COVERAGE_REWARD = 1.0
COLLISION_PENALTY = -100.0
BOUNDARY_PENALTY = -5.0

def calculate_reward(
        discovered_new_cell = False,
        collision = False,
        boundary_violation=False
):

    """
    Calculate the reward for a single drone's time step.

    Parameters
    ----------
    discovered_new_cell : bool
        True if the drone discovers a previously unexplored cell.

    collision : bool
        True if the drone experiences a collision.

    boundary_violation : bool
        True if the drone violates the permitted boundary.

    Returns
    -------
    float
        The total reward for the time step.
    """


    reward = 0.0

    #reward exploration

    if discovered_new_cell:
        reward += COVERAGE_REWARD

    #penalize collision

    if collision:
        reward += COLLISION_PENALTY


    #penalize boundary violations

    if boundary_violation:
        reward += BOUNDARY_PENALTY

    return reward
