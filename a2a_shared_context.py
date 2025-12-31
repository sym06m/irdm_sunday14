class SharedContext:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)


context = SharedContext()

context.set("budget", "low")
context.set("city", "Almaty")

print(context.get("city"))
