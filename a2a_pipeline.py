class Planner:
    def run(self):
        return "Business plan created"


class Validator:
    def run(self, plan):
        return f"Validated: {plan}"


class Executor:
    def run(self, validated_plan):
        return f"Executed: {validated_plan}"


planner = Planner()
validator = Validator()
executor = Executor()

plan = planner.run()
validated = validator.run(plan)
result = executor.run(validated)

print(result)
