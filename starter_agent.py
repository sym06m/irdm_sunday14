class StarterAgent:
    def __init__(self, name):
        self.name = name

    def run(self, task):
        return f"{self.name} completed task: {task}"


agent = StarterAgent("BusinessAgent")
print(agent.run("Market analysis"))
