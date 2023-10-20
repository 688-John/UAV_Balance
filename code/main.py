
import gym
import numpy as np

continuous_mode = True #if True, after completing one episode the next one will start automatically
random_action = False #if True, the agent will take actions randomly

render_sim = True #if True, a graphic is generated

env = gym.make('UAV_gym_env', render_sim = render_sim, render_path=True, render_shade=True,shade_distance=70,
               n_steps=500, n_fall_steps=10, change_target=True, initial_throw=True)


print("Action space: ", env.action_space)
print("Observation space: ", env.observation_space)
env.render()
