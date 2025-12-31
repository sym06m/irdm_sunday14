def a2a_message(sender, receiver, payload):
    return {
        "from": sender,
        "to": receiver,
        "payload": payload
    }


msg = a2a_message(
    sender="PlannerAgent",
    receiver="ExecutorAgent",
    payload="Select best location"
)

print(msg)
