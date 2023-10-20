from setuptools import setup, find_packages
import os


setup(
    name='UAV_gym_env',
    version='1.3.2',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data = True,
    install_requires=['gym', 'pygame', 'pymunk', 'numpy', 'stable-baselines3[extra]'],
    keywords=['reinforcement learning', 'gym environment', 'StableBaselines3', 'OpenAI Gym']
)
