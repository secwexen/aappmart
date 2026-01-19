import logging

class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        logging.info(f"Task added: {task}")

    def get_tasks(self):
        return self.tasks
