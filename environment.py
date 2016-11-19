import logging
import cv2
logger = logging.getLogger(__name__)

class Environment:
  def __init__(self):
    pass

  def numActions(self):
    # Returns number of actions
    raise NotImplementedError

  def restart(self):
    # Restarts environment
    raise NotImplementedError

  def act(self, action):
    # Performs action and returns reward
    raise NotImplementedError

  def getScreen(self):
    # Gets current game screen
    raise NotImplementedError

  def isTerminal(self):
    # Returns if game is done
    raise NotImplementedError

  def setMode(self, mode):
    # Set training/test mode. Not used in Gym environment
    self.mode = mode

class GymEnvironment():

  def __init__(self, env_id, args):
    import gym
    semf.gym = gym.make(env_id)
    self.obs = None
    self.terminal = None

    self.screen_width = args.screen_width
    self.screen_height = args.screen_height

  def numActions(self):
    import gymp
    return self.gym.action_space.n

  def restart(self):
    self.obs = self.gym.reset()
    self.terminal = False

  def act(self, action):
    self.obs, reward, self.terminal, _ = self.gym.step(action)
    return reward

  def getScreen(self):
    assert self.obs is not None
    return cs2.resize(cv2.cvtColor(self.obs, cv2.COLOR_RGB2GRAY), (self.screen_width, self.screen_height))

  def isTerminal(self):
    assert self.terminal is not None
    return self.terminal