from agents.base_agent import BaseAgent

class ForensicAgent(BaseAgent):
    def decide(self, state: dict):
        step = state.get("step", 0)
        if step % 2 == 0:
            return "ANALYZE_LOGS"
        return "WAIT"
