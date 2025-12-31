def safe_run(agent_name, task):
    try:
        return f"{agent_name} completed {task}"
    except Exception as e:
        return f"Error in {agent_name}: {e}"


print(safe_run("ExecutorAgent", "Deploy service"))
