# Simulation Brain (CORE)

The CORE subsystem orchestrates the entire AAPP-MART framework.  
It manages execution flow, global state, and agent coordination.

---

## 1. Overview

CORE is responsible for:

- Running AAPP  
- Initializing MART agents  
- Managing the Knowledge Graph  
- Executing simulation loops  
- Generating final reports  

---

## 2. Components

### 2.1 Orchestrator (`orchestrator.py`)
Controls the full workflow:

1. Load input  
2. Run AAPP  
3. Initialize agents  
4. Execute simulation  
5. Collect results  
6. Generate reports  

---

### 2.2 Simulation Engine (`simulation_engine.py`)
Runs the main loop:

- Iterates through agents  
- Executes actions  
- Updates Knowledge Graph  
- Detects simulation end conditions  

---

### 2.3 Knowledge Graph (`knowledge_graph.py`)
Stores global state:

- Hosts  
- Services  
- Vulnerabilities  
- Credentials  
- Agent findings  
- Attack paths  

Acts as shared memory for all agents.

---

### 2.4 Utils (`utils.py`)
Provides helper functions:

- Logging  
- Formatting  
- Data validation  

---

## 3. Simulation Flow

```
Input → AAPP → Initialize Agents → Simulation Loop → Reports
```

---

## 4. End Conditions

Simulation ends when:

- No new actions are possible  
- All agents are idle  
- Maximum depth is reached  
- Orchestrator terminates execution  

---

## 5. Extensibility

You can extend CORE by:

- Adding new simulation modes  
- Adding new orchestrator logic  
- Adding new Knowledge Graph fields  

---

## 6. Summary

The CORE subsystem is the brain of AAPP-MART.  
It ensures coordinated, autonomous, and intelligent simulation across all components.
