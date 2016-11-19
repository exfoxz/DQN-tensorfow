import logging
logger = logging.getLogger(__name__)

class DeepQNetwork:
    def __init__(self):
        raise NotImplementedError

    def _createLayers(self, num_actions):
        raise NotImplementedError

    def _setInput(self, states):
        raise NotImplementedError

    def update_target_network(self):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

    def predict(self):
        raise NotImplementedError
