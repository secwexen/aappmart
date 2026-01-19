class BaseAgent:

    def __init__(self, name: str):
        self.name = name

    def decide(self, state: dict):
      
        raise NotImplementedError("decide() must be implemented by subclasses")
