import time

def run_with_metrics(agent, task):
    start = time.time()
    result = agent.run(task)
    latency = time.time() - start
    return {
        "result": result,
        "latency": latency
    }


agent = StarterAgent("OpsAgent")
print(run_with_metrics(agent, "Health check"))
