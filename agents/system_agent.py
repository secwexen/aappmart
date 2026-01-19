from agents.base_agent import BaseAgent

class SystemAgent(BaseAgent):
    def decide(self, state: dict):
        step = state.get("step", 0)
        if step % 2 == 1:
            return "CHECK_SYSTEM"
        return "IDLE"
