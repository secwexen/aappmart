from agents.base_agent import BaseAgent

class NetworkAgent(BaseAgent):
    def decide(self, state: dict):
        step = state.get("step", 0)
        if step % 3 == 0:
            return "SCAN_NETWORK"
        return "MONITOR"
