# Simple DQN training with OpenAI Gym and Atari games and Tensorflow
import logging
logger.setLevel(logging.INFO)

import gym

num_episodes = 20
num_steps = 1000

def main():
    # instantiate logger
    logger = logging.getLogger(__name__)

    env = gym.make('SpaceInvaders-v0')
    for i_episode in range(num_episodes):
        observation = env.reset()
        for t in range(num_steps):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break

if __name__ == '__main__':
    main()