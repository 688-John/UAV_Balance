from UAV_env import UAVEnv
from gym.envs.registration import register

register(
    id='UAV_gym_env',
    entry_point='UAV_gym_env:UAVEnv',
    kwargs={'render_sim': False, 'render_path': True, 'render_shade': True,
            'shade_distance': 100, 'n_steps': 500, 'n_fall_steps': 10, 'change_target': False,
            'initial_throw': True}
)
