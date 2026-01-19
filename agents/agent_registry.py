from agents.forensic_agent import ForensicAgent
from agents.network_agent import NetworkAgent
from agents.system_agent import SystemAgent

class AgentRegistry:

    @staticmethod
    def get_all_agents():
        return [
            ForensicAgent("ForensicAgent"),
            NetworkAgent("NetworkAgent"),
            SystemAgent("SystemAgent")
        ]
