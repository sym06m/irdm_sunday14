class Agent:
    def __init__(self, name):
        self.name = name

    def handle(self, message):
        return f"{self.name} processed: {message}"


agent_a = Agent("PlannerAgent")
agent_b = Agent("ExecutorAgent")

message = agent_a.handle("Create a plan")
response = agent_b.handle(message)

print(response)
